"""

CUE 2d routines source code

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
import matplotlib.pyplot as plt
import pandas as pd
import backend
import inp
from time import sleep


def map_places_traits(grd_ids, df_places):
    grd_traits = np.zeros(shape=np.shape(grd_ids), dtype="float32")
    for i in range(len(df_places)):
        grd_traits = grd_traits + (df_places["Place_Trait"].values[i] * (grd_ids == df_places["Id"].values[i]))
    return grd_traits


def play(df_agents, df_places, grd_ids, n_steps, b_tui=False, b_return=False, b_trace=True):

    # first get unique places found in the ids map
    df_places_grd = pd.DataFrame(
        {
            "Id": np.unique(grd_ids)
        }
    )
    # merge places dataframes
    df_places = pd.merge(
        how='left',
        left=df_places_grd,
        right=df_places[["Id", "Trait", "D"]],
        left_on="Id",
        right_on="Id"
    )

    # start up
    s_dtype = "float32"
    n_agents = len(df_agents)
    n_places = len(df_places)
    n_rows = np.shape(grd_ids)[0]
    n_cols = np.shape(grd_ids)[1]

    # scanning window parameters set up
    #
    # get unique beta (radius size) values
    lst_unique_beta = list(df_agents["Beta"].unique())
    dct_window = dict()
    for n_beta in lst_unique_beta:
        # get scanning window parameters
        vct_window_rows, vct_window_cols = backend.get_window_ids(
            n_rows=n_rows,
            n_cols=n_cols,
            n_rsize=n_beta,
            b_flat=True
        )

        # remove the origin from window
        lst_aux_rows = list()
        lst_aux_cols = list()
        for i in range(len(vct_window_rows)):
            if vct_window_rows[i] == 0 and vct_window_cols[i] == 0:
                pass
            else:
                lst_aux_rows.append(vct_window_rows[i])
                lst_aux_cols.append(vct_window_cols[i])

        # get window base ids
        vct_rows_base_ids = np.array(lst_aux_rows, dtype="uint16")
        vct_cols_base_ids = np.array(lst_aux_cols, dtype="uint16")

        # deploy recyclable window dataframe
        n_window_size = len(vct_rows_base_ids)
        df_window = pd.DataFrame(
            {
                "rows": vct_rows_base_ids,
                "cols": vct_cols_base_ids,
                "x": np.zeros(n_window_size, dtype="uint16"),
                "y": np.zeros(n_window_size, dtype="uint16"),
                "Id": np.zeros(n_window_size, dtype="int16"),
                "Discrepancy": np.zeros(n_window_size, dtype=s_dtype),
                "Interac_score": np.zeros(n_window_size, dtype=s_dtype),
                "Interac_prob": np.zeros(n_window_size, dtype=s_dtype),
            }
        )
        # append to dict
        dct_window[str(n_beta)] = {
            "df": df_window
        }

    # define random seeds prior to simulation loop
    np.random.seed(backend.get_seed())
    grd_seeds = np.random.randint(
        low=100,
        high=999,
        size=(n_steps, n_agents),
        dtype="uint16"
    )

    plt.imshow(grd_ids, origin='lower', cmap='jet')
    plt.scatter(df_agents['x'], df_agents['y'], c=df_agents["Trait"], vmin=0, vmax=10, edgecolors='white')
    plt.show()

    # main loop:
    for t in range(n_steps):
        print("\n\n:::::: Step {} ::::::\n".format(t + 1))
        sleep(1)
        for a in range(len(df_agents)):
            # get agents attributes
            a_id = df_agents["Id"].values[a]
            a_x = df_agents["x"].values[a]
            a_y = df_agents["y"].values[a]
            a_trait = df_agents["Trait"].values[a]
            a_alpha = df_agents["Alpha"].values[a]
            a_beta = df_agents["Beta"].values[a]
            a_c = df_agents["C"].values[a]

            print("\n\n\t:::::: Agent {} ::::::\n".format(a_id))
            sleep(1)
            print("agent location x={} y={}".format(a_x, a_y))
            print("agent id = {}".format(a_id))
            print("agent trait = {}".format(a_trait))
            print("agent alpha = {}".format(a_alpha))
            print("agent beta = {}".format(a_beta))
            print("agent c = {}".format(a_c))


            # get window dataframe
            df_window = dct_window[str(a_beta)]["df"]
            # update window
            df_window["x"] = (a_x + df_window["cols"].values) % n_cols
            df_window["y"] = (a_y + df_window["rows"].values) % n_rows
            # get ids
            for i in range(len(df_window)):
                lcl_x = df_window["x"].values[i]
                lcl_y = df_window["y"].values[i]
                df_window["Id"].values[i] = grd_ids[lcl_y][lcl_x]

            # todo move this to conditonal to get move efficient

            df_window = pd.merge(
                how='left',
                left=df_window,
                right=df_places,
                left_on="Id",
                right_on="Id"
            )
            df_window["Discrepancy"] = np.abs(
                a_trait - df_window["Trait"].values
            )

            # compute selection Interac_score
            df_window["Interac_score"] = (
                    df_window["Discrepancy"].max() - df_window["Discrepancy"] + 1
            )
            # normalize
            # set score = zero where place is beyond alpha threshold
            df_window["Interac_score"] = df_window["Interac_score"].values * (
                    df_window["Discrepancy"].values <= a_alpha
            )
            # compute probabilistic weights
            if df_window["Interac_score"].sum() == 0:
                # uniform distribution when all scores == 0:
                df_window["Interac_prob"] = 1 / len(df_window)
            else:
                df_window["Interac_prob"] = (
                        df_window["Interac_score"] / df_window["Interac_score"].sum()
                )


            print(df_window.to_string())

            # get agent's place id based on its location
            p_id = grd_ids[a_y][a_x]
            if p_id == 0:
                print('\t\t->> move to indoors randomly but weighted')
                df_window_move = df_window.query("Id != 0")
            else:
                print('\t\t->> interact and move to outdoors randomly')
                df_window_move = df_window.query("Id == 0")
                if len(df_window_move) == 0:
                    df_window_move = df_window.copy()
                # get place trait
                p_trait = df_places.query("Id == {}".format(p_id))["Trait"].values[0]
                # get place d
                p_d = df_places.query("Id == {}".format(p_id))["D"].values[0]

                print("place id = {}".format(p_id))
                print("place trait = {}".format(p_trait))
                print("place D = {}".format(p_d))
            print('\n')
            print(df_window_move.to_string())




if __name__ == "__main__":
    print('ok')
    n_steps = 3
    n_agents = 3

    # create agents dataframe (read from table)
    df_agents = pd.DataFrame(
        {
            "Id": np.arange(1, n_agents + 1),
            "x": [12, 12, 12],
            "y": [5, 10, 15],
            "Trait": [5, 5, 5],
            "Alpha": [3, 3, 3],
            "Beta": [1, 2, 3],
            "C": [0.01, 0.02, 0.0]
        }
    )

    # read places parameters table
    df_places_input = pd.read_csv("C:/gis/bin/places_params.csv", sep=";")
    df_places_input["D"] = 0.1
    print(df_places_input.head())

    # read ID map
    meta, grd_ids = inp.asc_raster(file="C:/gis/bin/places_demo_5m.asc")
    print(np.shape(grd_ids))


    #grd_traits = map_places_traits(grd_ids=grd_ids, df_places=df_places)




    play(
        df_agents=df_agents,
        df_places=df_places_input,
        grd_ids=grd_ids,
        n_steps=n_steps
    )