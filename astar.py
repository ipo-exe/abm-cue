"""

A-Star algorithm source code for 2D-CUE ABM

Copyright (C) 2022 Iporã Brito Possantti

References:


************ GNU GENERAL PUBLIC LICENSE ************

https://www.gnu.org/licenses/gpl-3.0.en.html

Permissions:
 - Commercial use
 - Distribution
 - Modification
 - Patent use
 - Private use

Conditions:
 - Disclose source
 - License and copyright notice
 - Same license
 - State changes

Limitations:
 - Liability
 - Warranty

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------------------------------------
# utils


def get_benchmark_grid():
    n_size = 100
    grd = np.random.randint(1, 10000, size=(n_size, n_size), dtype="uint32")

    grd[int(n_size / 2) - 1] = 0
    grd[int(n_size / 2)] = 0
    grd[int(n_size / 2) + 1] = 0

    grd = grd.transpose()

    for i in range(1, len(grd) - 1, 5):
        grd[i - 1] = 0
        grd[i] = 0
        grd[i+ 1] = 0

    return grd

def get_benchmark_grid_2():
    lst_grid = [
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 4, 6],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    grd = np.array(lst_grid, dtype="uint32")
    return grd

def get_benchmark_grid_3():
    np.random.seed(666)
    n_size = 20
    grd1 = np.random.randint(1, 10000, size=(n_size, n_size), dtype="uint32")
    grd2 = np.random.randint(0, 100, size=(n_size, n_size), dtype="uint32")
    grd = grd1 * (1 * (grd2 > 70))
    return grd


def path_to_wkt(vct_i, vct_j, metadata):
    '''
    convert a path to WKT given Raster Metadata
    :param vct_i: numpy array of i coordinates (rows)
    :param vct_j: numpy array of j coordinates (cols)
    :param metadata: dict of raster metadata
    :return: string of WTK path
    '''
    n_cols = metadata["ncols"]
    n_rows = metadata["nrows"]
    n_scale = metadata["cellsize"]
    vct_x = metadata["xllcorner"] + ((vct_j * n_scale) + (n_scale / 2))
    vct_y = metadata["yllcorner"] + ((n_rows - vct_i) * n_scale) - (n_scale / 2)
    lst_vertex = list()
    for i in range(len(vct_x)):
        lst_vertex.append("{} {}".format(vct_x[i], vct_y[i]))
    s_vertex = ", ".join(lst_vertex)
    return "LineString({})".format(s_vertex)


def node_to_wkt(node_i, node_j, metadata):
    """
    convert a node to WKT given Raster Metadata
    :param node_i: i coordinate
    :type node_i: int
    :param node_j: j coordinate
    :type node_j: int
    :param metadata: raster metadata
    :type metadata: dict
    :return: WKT of node
    :rtype: str
    """
    n_cols = metadata["ncols"]
    n_rows = metadata["nrows"]
    n_scale = metadata["cellsize"]
    vct_x = metadata["xllcorner"] + ((node_j * n_scale) + (n_scale / 2))
    vct_y = metadata["yllcorner"] + ((n_rows - node_i) * n_scale) - (n_scale / 2)
    return "Point ({} {})".format(vct_x, vct_y)


def get_nodes_wkt(df_nodes, metadata):
    df_nodes = df_nodes.copy()
    df_nodes["Geom"] = "-"
    for i in range(len(df_nodes)):
        vct_i = df_nodes["i"].values[i]
        vct_j = df_nodes["j"].values[i]
        df_nodes["Geom"].values[i] = node_to_wkt(node_i=vct_i, node_j=vct_j, metadata=metadata)
    return df_nodes


def get_network_wkt(df_network, metadata):
    '''
    compute WTK for paths in Network dataframe
    :param df_network: pandas dataframe of network
    :param metadata: dict metadata from
    :return: new dataframe with WKT
    '''
    df_network = df_network.copy()
    df_network["Geom"] = "-"
    for i in range(len(df_network)):
        vct_i = np.array(list(map(int, df_network["Path_i"].values[i].split("-"))))
        vct_j = np.array(list(map(int, df_network["Path_j"].values[i].split("-"))))
        df_network["Geom"].values[i] = path_to_wkt(vct_i, vct_j, metadata)
    return df_network


# traceback
def traceback(src_i, src_j, par_df, closed_df):
    """
    trace back path from closed queue
    :param src_i: int source i
    :param src_j: int source j
    :param par_df: parents dataframe
    :param closed_df: closed nodes dataframe
    :return: dict of path
    """
    lst_i = []
    lst_j = []
    lst_i.insert(0, par_df["i"].values[0])
    lst_j.insert(0, par_df["j"].values[0])
    while True:
        par_i = par_df["ip"].values[0]
        par_j = par_df["jp"].values[0]
        if par_i == src_i and par_j == src_j:
            lst_i.insert(0, par_i)
            lst_j.insert(0, par_j)
            break
        par_df = closed_df.query("i == {} and j == {}".format(par_i, par_j))
        lst_i.insert(0, par_df["i"].values[0])
        lst_j.insert(0, par_df["j"].values[0])

    return {
        "i": np.array(lst_i),
        "j": np.array(lst_j),
    }


# window
def get_window(cell_i, cell_j, rows, cols, size=1):
    """
    get window dict for 2d grid
    :param cell_i: int i
    :param cell_j: int j
    :param rows: int number of grid rows
    :param cols: int number of grid cols
    :param size: int window size
    :return: dict of grid window
    """
    factors = np.arange(-size, size + 1)
    window_i = []
    window_j = []
    for r in range(len(factors)):
        for c in range(len(factors)):
            lcl_i = cell_i + factors[r]
            lcl_j = cell_j + factors[c]
            if lcl_i == cell_i and lcl_j == cell_j:
                pass
            elif lcl_i < 0 or lcl_j < 0:
                pass
            elif lcl_i >= rows or lcl_j >= cols:
                pass
            else:
                window_i.append(lcl_i)
                window_j.append(lcl_j)
    return {"i": window_i, "j": window_j}


# -----------------------------------------------------------------------------------------------------------
# Distance functions

def get_xy_distance(x1, y1, x2, y2):
    """
    get Euclidean distance
    :param x1: point 1 x
    :param y1: point 1 y
    :param x2: point 2 x
    :param y2: point 2 y
    :return: number distance
    """
    dx = x2 - x1
    dy = y2 - y1
    return np.sqrt(np.square(dx) + np.square(dy))


def get_path_distance(vct_x, vct_y):
    """
    compute path distance
    :param vct_x: numpy x of points
    :param vct_y: numpy y of points
    :return: path distance
    """
    n_d = 0
    for i in range(1, len(vct_x)):
        n_d = n_d + get_xy_distance(
            x1=vct_x[i - 1], y1=vct_y[i - 1], x2=vct_x[i], y2=vct_y[i]
        )
    return n_d


def get_astar_path(grid_maze, grid_h, src_i, src_j, dst_i, dst_j):
    """
    compute A-Star distance (path)
    :param grid_maze: numpy grid maze
    :param grid_h: numpy grid of Heuristics map
    :param src_i: int source place i
    :param src_j: int source place j
    :param dst_i: int destiny place i
    :param dst_j: int destiny place j
    :return:
    """
    # set params
    # get grid params
    n_rows = len(grid_maze)
    n_cols = len(grid_maze)
    # ----------------------------------------------------------------------
    # deploy dataframes queues

    # open queue
    open_df = pd.DataFrame(
        {
            'i': [src_i],
            'j': [src_j],
            'h': [0],
            'g': [0],
            'f': [0],
            'ip': [src_i],
            'jp': [src_j],
        }
    )
    # closed queue
    closed_df = open_df.copy()

    # ----------------------------------------------------------------------
    # search loop
    while len(open_df) > 0:

        # ------------------------------------------------------------------
        # sort open queue by f
        open_df = open_df.sort_values(by='f').reset_index(drop=True)
        #print(open_df.to_string())

        # ------------------------------------------------------------------
        # select top parent node
        par_df = open_df.iloc[[0]]
        # get parent location
        par_i = par_df['i'].values[0]
        par_j = par_df['j'].values[0]

        # ------------------------------------------------------------------
        # check halting criteria
        if par_i == dst_i and par_j == dst_j:
            #print('Path Found -- initiate trace back procedure')
            break

        # ------------------------------------------------------------------
        # expand parent node:

        # ------------------------------------------------------------------
        # find node neighborhood
        window_dct = get_window(
            cell_i=par_i,
            cell_j=par_j,
            rows=n_rows,
            cols=n_cols,
            size=1
        )

        # ------------------------------------------------------------------
        # set child dataframe
        child_df = pd.DataFrame(window_dct)
        # add fields
        child_df['h'] = 0
        child_df['g'] = 0
        child_df['f'] = 0
        child_df['ip'] = par_i
        child_df['jp'] = par_j

        # ------------------------------------------------------------------
        # filter node neighborhood

        # ------- remove grand-parent node
        gpar_i = par_df['ip'].values[0]
        gpar_j = par_df['jp'].values[0]
        aux_df = child_df.query(' i == {} and j == {}'.format(gpar_i, gpar_j))
        if len(aux_df) > 0:
            n_index = aux_df.index[0]  # get index
            child_df = child_df.drop(n_index).reset_index(drop=True)  # drop

        # ------- remove maze-obstacle nodes
        lst_to_drop = []
        for i in range(len(child_df)):
            # get location
            lcl_i = child_df['i'].values[i]
            lcl_j = child_df['j'].values[i]
            if lcl_i == dst_i and lcl_j == dst_j:
                pass
            else:
                # get maze value
                lcl_value = grid_maze[lcl_i][lcl_j]
                if lcl_value == 0:  # is obstacle
                    lst_to_drop.append(i)
        child_df = child_df.drop(lst_to_drop).reset_index(drop=True)  # drop

        # ------- remove closed nodes
        lst_to_drop = []
        for i in range(len(child_df)):
            # get location
            lcl_i = child_df['i'].values[i]
            lcl_j = child_df['j'].values[i]
            aux_df = closed_df.query(' i == {} and j == {}'.format(lcl_i, lcl_j))
            if len(aux_df) > 0:  # is closed
                lst_to_drop.append(i)
        child_df = child_df.drop(lst_to_drop).reset_index(drop=True)  # drop

        # ------------------------------------------------------------------
        # assess child nodes values
        lcl_g = par_df['g'].values[0]  # get local parent g
        for i in range(len(child_df)):
            # get location
            lcl_i = child_df['i'].values[i]
            lcl_j = child_df['j'].values[i]
            # set local h
            child_df['h'].values[i] = grid_h[lcl_i][lcl_j]
            # get local g
            if par_i == lcl_i or par_j == lcl_j:
                child_df['g'].values[i] = 10
            else:
                child_df['g'].values[i] = 14
        child_df['f'] = child_df['h'] + child_df['g'] + lcl_g

        # ------------------------------------------------------------------
        # concat child nodes to open queue
        open_df = pd.concat([open_df, child_df], ignore_index=True)
        # ------------------------------------------------------------------
        # dequeue (drop) parent node from open queue
        aux_df = open_df.query('i == {} and j == {}'.format(par_i, par_j))
        open_df = open_df.drop(aux_df.index)

        # ------------------------------------------------------------------
        # enqueue (append) parent node to closed queue
        closed_df = pd.concat([closed_df, par_df], ignore_index=True)

    # ----------------------------------------------------------------------
    # traceback route
    dct_traceback = traceback(
        src_i=src_i,
        src_j=src_j,
        par_df=par_df,
        closed_df=closed_df
    )
    route_df = pd.DataFrame(dct_traceback)
    '''
    print(route_df.to_string())
    plt.imshow(grd_places)
    plt.plot(route_df["j"], route_df["i"], "-o")
    plt.show()
    '''
    return route_df


def get_network(grd_places, df_places):
    from scipy import ndimage
    # -----------------------------------------------------------------------------------------------------------
    # get NODES dataframe

    # Scanning loop to find nodes

    n_rows = len(grd_places)
    n_cols = len(grd_places[0])
    lst_nodes = []
    lst_i = []
    lst_j = []
    lst_place = []
    n_id = 0
    for i in range(len(grd_places)):
        for j in range(len(grd_places[i])):
            n_lcl_value = grd_places[i][j]
            if n_lcl_value == 0:  # is outdoor
                pass
            elif n_lcl_value in lst_place:  # already assessed
                pass
            else:
                # get cell window
                dct_window = get_window(cell_i=i, cell_j=j, rows=n_rows, cols=n_cols, size=1)
                df_window = pd.DataFrame(dct_window)
                # collect cell window values
                df_window["Value"] = 0.0
                for k in range(len(df_window)):
                    lcl_i = df_window["i"].values[k]
                    lcl_j = df_window["j"].values[k]
                    df_window["Value"].values[k] = grd_places[lcl_i][lcl_j]
                # check if there is a way out
                if df_window["Value"].min() == 0:
                    # append node to lists
                    lst_nodes.append(n_id)
                    lst_i.append(i)
                    lst_j.append(j)
                    lst_place.append(n_lcl_value)
                    # update id
                    n_id = n_id + 1

    df_nodes = pd.DataFrame(
        {
            "Id_node": lst_nodes,
            "j": lst_j,
            "i": lst_i,
            "Id_place": lst_place,
        }
    )

    #df_nodes = df_nodes.sample(100)

    # -----------------------------------------------------------------------------------------------------------
    # network parameters

    # get maze grid
    grd_maze = grd_places == 0

    # compute map attributes
    n_indoors = len(df_nodes)

    # number of paths to compute
    n_paths = int((n_indoors * (n_indoors - 1)) / 2)

    #print("Number of paths to find: {}".format(n_paths))

    '''
    plt.imshow(grd_maze, "Greys")
    plt.scatter(df_nodes["j"], df_nodes["i"], marker='.', color="orange")
    plt.show()
    '''

    # -----------------------------------------------------------------------------------------------------------
    # get NETWORK dataframe

    df_network = pd.DataFrame(
        {
            "Id_node_src": np.zeros(n_paths, dtype="uint16"),
            "i_src": np.zeros(n_paths, dtype="uint16"),
            "j_src": np.zeros(n_paths, dtype="uint16"),
            "Id_node_dst": np.zeros(n_paths, dtype="uint16"),
            "i_dst": np.zeros(n_paths, dtype="uint16"),
            "j_dst": np.zeros(n_paths, dtype="uint16"),
            "Euclidean": np.zeros(n_paths, dtype="float32"),
            "AStar": np.zeros(n_paths, dtype="float32"),
        }
    )
    df_network["Path_i"] = "-"
    df_network["Path_j"] = "-"

    c = 0
    for n in range(len(df_nodes)):
        for m in range(len(df_nodes)):
            if n >= m:
                pass
            else:
                # print("{} to {}".format(n, m))
                df_network["Id_node_src"].values[c] = df_nodes["Id_node"].values[n]
                df_network["Id_node_dst"].values[c] = df_nodes["Id_node"].values[m]
                # set coordinates
                df_network["i_src"].values[c] = df_nodes["i"].values[n]
                df_network["i_dst"].values[c] = df_nodes["i"].values[m]
                df_network["j_src"].values[c] = df_nodes["j"].values[n]
                df_network["j_dst"].values[c] = df_nodes["j"].values[m]
                c = c + 1

    # compute euclidean distance
    df_network["Euclidean"] = get_xy_distance(
        x1=df_network["j_src"].values,
        y1=df_network["i_src"].values,
        x2=df_network["j_dst"].values,
        y2=df_network["i_dst"].values
    )

    # compute AStar distance and path

    # instantiate heuristics grid
    grid_h_blank = np.ones(shape=np.shape(grd_places), dtype='uint32')

    print("processing A-Star distance...")
    for i in range(len(df_network)):
        print("computing iteration {} of {}".format(i + 1, len(df_network)))
        n_dst_id = df_network["Id_node_dst"].values[i]
        n_src_j = df_network["j_src"].values[i]
        n_src_i = df_network["i_src"].values[i]
        n_dst_j = df_network["j_dst"].values[i]
        n_dst_i = df_network["i_dst"].values[i]
        print("from ({},{}) to ({},{})".format(n_src_i, n_src_j, n_dst_i, n_dst_j))

        # get distance heuristic grid for each node
        grd_h_distance = grid_h_blank.copy()
        grd_h_distance[n_dst_i][n_dst_j] = 0
        # get distance image
        grd_h_distance = 10 * ndimage.distance_transform_edt(grd_h_distance)

        df_path = get_astar_path(
            grid_maze=grd_maze,
            grid_h=grd_h_distance,
            src_i=n_src_i,
            src_j=n_src_j,
            dst_i=n_dst_i,
            dst_j=n_dst_j
        )

        n_dist = get_path_distance(
            vct_x=df_path["j"].values,
            vct_y=df_path["i"].values,
        )
        df_network["AStar"].values[i] = n_dist
        s_path_i = "-".join(df_path["i"].astype(str))
        s_path_j = "-".join(df_path["j"].astype(str))
        df_network["Path_i"].values[i] = s_path_i
        df_network["Path_j"].values[i] = s_path_j

    # append inverse network
    df_network_inv = df_network.copy()
    df_network_inv["Id_node_src"] = df_network["Id_node_dst"].values
    df_network_inv["Id_node_dst"] = df_network["Id_node_src"].values
    df_network_inv["i_src"] = df_network["i_dst"].values
    df_network_inv["i_dst"] = df_network["i_src"].values
    df_network_inv["j_src"] = df_network["j_dst"].values
    df_network_inv["j_dst"] = df_network["j_src"].values
    df_network = pd.concat([df_network, df_network_inv], ignore_index=True)

    # merge Places attributes in src
    df_network = df_network.merge(df_nodes[["Id_node", "Id_place"]], how="left", left_on="Id_node_src", right_on="Id_node")
    df_network = df_network.drop(columns=["Id_node"])
    df_network = df_network.rename(columns={"Id_place": "Id_place_src"})
    df_network = df_network.merge(df_places, how="left", left_on="Id_place_src", right_on="Id")
    df_network = df_network.drop(columns=["Id"])
    df_network = df_network.rename(
        columns={
            "Trait": "Trait_src",
            "C": "C_src",
            "Name": "Name_src",
        }
    )

    # merge Places attributes in dst
    df_network = df_network.merge(df_nodes[["Id_node", "Id_place"]], how="left", left_on="Id_node_dst",
                                  right_on="Id_node")
    df_network = df_network.drop(columns=["Id_node"])
    df_network = df_network.rename(columns={"Id_place": "Id_place_dst"})
    df_network = df_network.merge(df_places, how="left", left_on="Id_place_dst", right_on="Id")
    df_network = df_network.drop(columns=["Id"])
    df_network = df_network.rename(
        columns={
            "Trait": "Trait_dst",
            "C": "C_dst",
            "Name": "Name_dst",
        }
    )

    return df_network, df_nodes


if __name__ == "__main__":
    import inp, out
    # -----------------------------------------------------------------------------------------------------------
    # set random state

    np.random.seed(662)

    #
    # i = y = row coordinate
    # j = x = column coordinate
    #
    # -----------------------------------------------------------------------------------------------------------
    # Load or create maze


    # ------------------------------------------------------
    # load map

    dct_meta, grd_places = inp.asc_raster(file="./demo/benchmark1/benchmark1.asc", dtype="float32")
    #grd_places = grd_places.astype("uint32")
    #print(dct_meta)


    #grd_places = get_benchmark_grid_3() #get_benchmark_grid_2()
    vct_uniques = np.unique(grd_places)




    # -----------------------------------------------------------------------------------------------------------
    # Load or create places data frame
    df_places = pd.read_csv("./demo/benchmark1/benchmark1_places.txt", sep=";")

    # -----------------------------------------------------------------------------------------------------------
    # Compute network
    df_net, df_nodes = get_network(grd_places=grd_places, df_places=df_places)


    df_wkt = get_nodes_wkt(df_nodes=df_nodes, metadata=dct_meta)
    df_wkt.to_csv("./demo/benchmark1/benchmark1_nodes.txt", sep=";", index=False)

    df_wkt = get_network_wkt(df_network=df_net, metadata=dct_meta)
    df_wkt.to_csv("./demo/benchmark1/benchmark1_network.txt", sep=";", index=False)


    # -----------------------------------------------------------------------------------------------------------







