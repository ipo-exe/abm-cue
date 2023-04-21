"""

Tools scripts source code

Copyright (C) 2022 Iporã Brito Possantti

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
import os.path

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import inp, backend
import visuals
from backend import status
from analyst import shannon_entropy


def run_cue1d(s_fsim, b_wkplc=True, s_dir_out="C:/bin"):
    """
    tool for the CUE1d model
    :param s_fsim: string file path of simulation parameters
    :param b_wkplc: boolean to consider workplace or not
    :param s_dir_out: string path to output dictionary
    :return:
    """
    import cue1d

    # ------------------------------------------------------------------------------------------
    # import param_simulation.txt
    dct_fsim = inp.import_data_table(s_table_name="param_simulation_1d", s_filepath=s_fsim)
    df_param_sim = dct_fsim["df"]

    # ------------------------------------------------------------------------------------------
    # update timestamp value
    df_param_sim.loc[
        df_param_sim["Metadata"] == "Timestamp", "Value"
    ] = backend.timestamp_log()

    # ------------------------------------------------------------------------------------------
    # get run folder
    if b_wkplc:
        s_workplace = (
            df_param_sim.loc[df_param_sim["Metadata"] == "Run Folder", "Value"]
            .values[0]
            .strip()
        )
        s_dir_out = backend.create_rundir(label="CUE1d", wkplc=s_workplace)

    # ------------------------------------------------------------------------------------------
    # get places file
    f_places = (
        df_param_sim.loc[df_param_sim["Metadata"] == "Places File", "Value"]
        .values[0]
        .strip()
    )

    # ------------------------------------------------------------------------------------------
    # get agents file
    f_agents = (
        df_param_sim.loc[df_param_sim["Metadata"] == "Agents File", "Value"]
        .values[0]
        .strip()
    )

    # ------------------------------------------------------------------------------------------
    # get simulation parameters
    #
    # number of steps
    n_steps = int(
        df_param_sim.loc[df_param_sim["Metadata"] == "Steps", "Value"].values[0].strip()
    )
    # string for weighting methods
    s_weighting = df_param_sim.loc[df_param_sim["Metadata"] == "Weighting", "Value"].values[0].strip()

    # string boolean return agents to original position
    s_return = (
        df_param_sim.loc[df_param_sim["Metadata"] == "Return Agents", "Value"]
        .values[0]
        .strip()
    )
    # string boolean trace back simulation
    s_trace = (
        df_param_sim.loc[df_param_sim["Metadata"] == "Trace Back", "Value"]
        .values[0]
        .strip()
    )
    # string boolean plot simulation
    s_plot = (
        df_param_sim.loc[df_param_sim["Metadata"] == "Plot Steps", "Value"]
        .values[0]
        .strip()
    )

    # ------------------------------------------------------------------------------------------
    # convert to boolean
    b_return = False
    b_trace = False
    b_plot = False
    if s_trace == "True":
        b_trace = True
    if s_return == "True":
        b_return = True
    if s_plot == "True":
        b_plot = True

    # ------------------------------------------------------------------------------------------
    # import places file
    dct_places = inp.import_data_table(s_table_name="param_places_1d", s_filepath=f_places)
    df_places = dct_places["df"]
    df_places["Trait"] = df_places["Trait"].astype("float64")

    # ------------------------------------------------------------------------------------------
    # import agents file
    dct_agents = inp.import_data_table(s_table_name="param_agents_1d", s_filepath=f_agents)
    df_agents = dct_agents["df"]
    df_agents["Trait"] = df_agents["Trait"].astype("float64")

    # ------------------------------------------------------------------------------------------
    # extra params
    n_agents = len(df_agents)
    n_places = len(df_places)
    n_traits = int(max([df_agents["Trait"].max(), df_places["Trait"].max()]))

    # ------------------------------------------------------------------------------------------
    # run model
    dct_out = cue1d.play(
        df_agents=df_agents.copy(),
        df_places=df_places.copy(),
        n_steps=n_steps,
        s_weight=s_weighting,
        b_tui=True,
        b_return=b_return,
        b_trace=b_trace,
    )

    # ------------------------------------------------------------------------------------------
    # retrieve outputs
    df_agents_end = dct_out["Agents"]
    df_places_end = dct_out["Places"]

    # ------------------------------------------------------------------------------------------
    # run analyst
    n_shannon_agents_start = shannon_entropy(grd=df_agents['Trait'].values)
    n_shannon_agents_end = shannon_entropy(grd=df_agents_end['Trait'].values)
    n_shannon_places_start = shannon_entropy(grd=df_places['Trait'].values)
    n_shannon_places_end = shannon_entropy(grd=df_places_end['Trait'].values)
    dct_analyst = {
        'Step': ['Start', 'End'],
        'H_agents': [n_shannon_agents_start, n_shannon_agents_end],
        'H_places': [n_shannon_places_start, n_shannon_places_end],
    }
    df_analyst = pd.DataFrame(dct_analyst)

    # ------------------------------------------------------------------------------------------
    # export results
    status("exporting start/end results datasets")
    df_agents.to_csv(
        "{}/param_agents_1d_start.txt".format(s_dir_out), sep=";", index=False
    )
    df_agents_end.to_csv(
        "{}/param_agents_1d_end.txt".format(s_dir_out), sep=";", index=False
    )
    df_places.to_csv(
        "{}/param_places_1d_start.txt".format(s_dir_out), sep=";", index=False
    )
    df_places_end.to_csv(
        "{}/param_places_1d_end.txt".format(s_dir_out), sep=";", index=False
    )
    status("exporting start/end analyst")
    df_analyst.to_csv(
        "{}/analyst_start_end.txt".format(s_dir_out), sep=";", index=False
    )
    # set aux lists
    lst_df = [df_agents, df_agents_end, df_places, df_places_end]
    lst_nms = [
        "hist_agents_start",
        "hist_agents_end",
        "hist_places_start",
        "hist_places_end",
    ]
    lst_ttl = [
        "Agents Histogram | Start",
        "Agents Histogram | End",
        "Places Histogram | Start",
        "Places Histogram | End",
    ]

    # ------------------------------------------------------------------------------------------
    # VISUALS
    # export histograms
    from visuals import plot_trait_histogram
    for i in range(len(lst_df)):
        df_lcl = lst_df[i]
        vct_hist, vct_bins = np.histogram(
            a=df_lcl["Trait"].values, bins=n_traits, range=(0, n_traits)
        )
        df_hist = pd.DataFrame({"Trait": vct_bins[1:], "Count": vct_hist})
        df_hist.to_csv("{}/{}.txt".format(s_dir_out, lst_nms[i]), sep=";", index=False)
        plot_trait_histogram(
            df_data=df_lcl,
            n_traits=n_traits,
            n_bins=n_traits,
            s_ttl=lst_ttl[i],
            s_dir_out=s_dir_out,
            s_file_name="view_" + lst_nms[i],
            n_dpi=100,
            b_show=False,
        )

    if b_trace:
        import os
        from visuals import plot_cue_1d_pannel
        from out import export_gif

        status("exporting traced results datasets")

        # transpose grids
        grd_traced_places_traits_t = dct_out["Simulation"]["Places_traits"].transpose()
        grd_traced_agents_x_t = dct_out["Simulation"]["Agents_x"].transpose()
        grd_traced_agents_traits_t = dct_out["Simulation"]["Agents_traits"].transpose()

        # get fill size
        n_fill = int(np.log10(n_steps)) + 1

        # deploy agents dataframes
        df_traced_agents_x = pd.DataFrame({"Step": np.arange(0, n_steps)})
        df_traced_agents_traits = pd.DataFrame({"Step": np.arange(0, n_steps)})

        # loop to append fields to dataframe
        for i in range(n_agents):
            s_lcl_agent_x = "{}_{}_x".format(df_agents["Alias"].values[i], df_agents["Id"].values[i])
            s_lcl_agent_trait = "{}_{}_Trait".format(df_agents["Alias"].values[i], df_agents["Id"].values[i])
            df_traced_agents_x[s_lcl_agent_x] = grd_traced_agents_x_t[i]
            df_traced_agents_traits[s_lcl_agent_trait] = grd_traced_agents_traits_t[i]

        # deploy places dataframes
        df_traced_places_traits = pd.DataFrame({"Step": np.arange(0, n_steps)})

        # loop to append fields to dataframe
        for i in range(n_places):
            s_lcl_place_trait = "{}_{}_Trait".format(df_places["Alias"].values[i], df_places["Id"].values[i])
            df_traced_places_traits[s_lcl_place_trait] = grd_traced_places_traits_t[i]
        #
        # ------------------------------
        #
        # run series analyst
        # set H field for agents
        vct_h = np.zeros(len(df_traced_agents_traits), dtype='float32')
        for t in range(len(df_traced_agents_traits)):
            # get local traits
            vct_lcl_traits = df_traced_agents_traits.values[t][1:]
            # compute H
            vct_h[t] = shannon_entropy(grd=vct_lcl_traits)
        df_traced_agents_traits['H'] = vct_h
        # set H field for places
        vct_h = np.zeros(len(df_traced_places_traits), dtype='float32')
        for t in range(len(df_traced_places_traits)):
            # get local traits
            vct_lcl_traits = df_traced_places_traits.values[t][1:]
            # compute H
            vct_h[t] = shannon_entropy(grd=vct_lcl_traits)
        df_traced_places_traits['H'] = vct_h

        # export csv files
        df_traced_agents_x.to_csv(
            "{}/traced_agents_x.txt".format(s_dir_out), sep=";", index=False
        )
        df_traced_agents_traits.to_csv(
            "{}/traced_agents_traits.txt".format(s_dir_out), sep=";", index=False
        )
        df_traced_places_traits.to_csv(
            "{}/traced_places_traits.txt".format(s_dir_out), sep=";", index=False
        )

        # plot series
        from visuals import plot_traced_traits, plot_traced_positions, plot_traced_h

        # agents
        plot_traced_traits(
            df_data=df_traced_agents_traits,
            df_params=df_agents,
            n_traits=n_traits,
            s_dir_out=s_dir_out,
            s_file_name="view_traced_agents_traits",
            s_ttl="Agents Traits",
            b_dark=False,
            b_show=False,
        )
        plot_traced_positions(
            df_data=df_traced_agents_x,
            df_params=df_agents,
            n_positions=len(df_places),
            s_dir_out=s_dir_out,
            s_file_name="view_traced_agents_x",
            s_ttl="Agents Positions",
            b_dark=False,
            b_show=False
        )
        plot_traced_h(
            df_data=df_traced_agents_traits,
            s_dir_out=s_dir_out,
            s_file_name="view_traced_agents_H",
            s_ttl="Agents H",
            b_dark=False,
            b_show=False
        )
        # places
        plot_traced_traits(
            df_data=df_traced_places_traits,
            df_params=df_places,
            s_dir_out=s_dir_out,
            n_traits=n_traits,
            s_file_name="view_traced_places_traits",
            s_ttl="Places Traits",
            b_dark=False,
            b_show=False,
        )
        plot_traced_h(
            df_data=df_traced_places_traits,
            s_dir_out=s_dir_out,
            s_file_name="view_traced_places_H",
            s_ttl="Places H",
            b_dark=False,
            b_show=False
        )
        # plot animation frames
        if b_plot:
            s_dir_frames = "{}/frames".format(s_dir_out)
            os.mkdir(path=s_dir_frames)
            # call sub routine
            animate_frames_1d(
                s_param_agents=f_agents,
                s_param_places=f_places,
                s_traced_agents_x="{}/traced_agents_x.txt".format(s_dir_out),
                s_traced_agents_traits="{}/traced_agents_traits.txt".format(s_dir_out),
                s_traced_places_traits="{}/traced_places_traits.txt".format(s_dir_out),
                s_dir_frames=s_dir_frames,
                s_dir_out=s_dir_out
            )
    return {"Output folder": s_dir_out, "Error Status": "OK"}


def run_cue2d(s_fsim, b_wkplc=True, b_network=False, s_dir_out="C:/bin", b_tui=True):
    """
    run CUE 2-D model
    :param s_fsim: simulation parameter file
    :type s_fsim: str
    :param b_wkplc: workplace flag
    :type b_wkplc: bool
    :param b_network: network model flag
    :type b_network: bool
    :param s_dir_out: output directory
    :type s_dir_out: str
    :param b_tui: display flag
    :type b_tui: bool
    :return: None
    :rtype:
    """
    import cue2d
    # ------------------------------------------------------------------------------------------
    # import param_simulation_2d.txt
    dct_fsim = inp.import_data_table(s_table_name="param_simulation_2d", s_filepath=s_fsim)
    df_param_sim = dct_fsim["df"]

    # ------------------------------------------------------------------------------------------
    # update timestamp value
    df_param_sim.loc[
        df_param_sim["Metadata"] == "Timestamp", "Value"
    ] = backend.timestamp_log()

    # ------------------------------------------------------------------------------------------
    # get run folder
    if b_wkplc:
        s_workplace = (
            df_param_sim.loc[df_param_sim["Metadata"] == "Run Folder", "Value"]
                .values[0]
                .strip()
        )
        s_dir_out = backend.create_rundir(label="CUE2d", wkplc=s_workplace)

    # ------------------------------------------------------------------------------------------
    # get places file
    f_places = (
        df_param_sim.loc[df_param_sim["Metadata"] == "Places File", "Value"]
            .values[0]
            .strip()
    )

    # ------------------------------------------------------------------------------------------
    # get places map
    f_places_map = (
        df_param_sim.loc[df_param_sim["Metadata"] == "Places Map", "Value"]
            .values[0]
            .strip()
    )

    # ------------------------------------------------------------------------------------------
    # get agents file
    f_agents = (
        df_param_sim.loc[df_param_sim["Metadata"] == "Agents File", "Value"]
            .values[0]
            .strip()
    )

    # ------------------------------------------------------------------------------------------
    # get files for network simulation
    if b_network:
        # --------------------------------------------------------------------------------------
        # get nodes file
        f_nodes = (
            df_param_sim.loc[df_param_sim["Metadata"] == "Nodes File", "Value"]
            .values[0]
            .strip()
        )
        # --------------------------------------------------------------------------------------
        # get network file
        f_network = (
            df_param_sim.loc[df_param_sim["Metadata"] == "Network File", "Value"]
            .values[0]
            .strip()
        )

    # ------------------------------------------------------------------------------------------
    # get simulation parameters
    #
    # number of steps
    n_steps = int(
        df_param_sim.loc[df_param_sim["Metadata"] == "Steps", "Value"].values[0].strip()
    )
    # string for weighting methods
    s_weighting = df_param_sim.loc[df_param_sim["Metadata"] == "Weighting", "Value"].values[0].strip()

    # ------------------------------------------------------------------------------------------
    # string boolean return agents to original position
    s_return = (
        df_param_sim.loc[df_param_sim["Metadata"] == "Return Agents", "Value"]
            .values[0]
            .strip()
    )

    # ------------------------------------------------------------------------------------------
    # string boolean trace back simulation
    s_trace = (
        df_param_sim.loc[df_param_sim["Metadata"] == "Trace Back", "Value"]
            .values[0]
            .strip()
    )

    # ------------------------------------------------------------------------------------------
    # string boolean plot simulation
    s_plot = (
        df_param_sim.loc[df_param_sim["Metadata"] == "Plot Steps", "Value"]
            .values[0]
            .strip()
    )

    # ------------------------------------------------------------------------------------------
    # convert to boolean
    b_return = False
    b_trace = False
    b_plot = False
    if s_trace == "True":
        b_trace = True
    if s_return == "True":
        b_return = True
    if s_plot == "True":
        b_plot = True

    # ------------------------------------------------------------------------------------------
    # import places file
    dct_places = inp.import_data_table(s_table_name="param_places_2d", s_filepath=f_places)
    df_places = dct_places["df"]
    df_places["Trait"] = df_places["Trait"].astype("float64")

    #-------------------------------------------------------------------------------------------
    # import agents file
    dct_agents = inp.import_data_table(s_table_name="param_agents_2d", s_filepath=f_agents)
    df_agents = dct_agents["df"]
    df_agents["Trait"] = df_agents["Trait"].astype("float64")

    # -------------------------------------------------------------------------------------------
    # import places map
    meta, grd_ids = inp.asc_raster(file=f_places_map)

    # -------------------------------------------------------------------------------------------
    # import file for network simulation
    if b_network:
        # ------------------------------------------------------------------------------------------
        # import nodes file
        dct_nodes = inp.import_data_table(s_table_name="nodes_places", s_filepath=f_nodes)
        df_nodes = dct_nodes["df"]
        # ------------------------------------------------------------------------------------------
        # import network file
        dct_network = inp.import_data_table(s_table_name="network_places", s_filepath=f_network)
        df_network = dct_network["df"]
        # filter
        df_network_filter = df_network[["Id_node_src", "Id_node_dst", "AStar", "Id_place_src", "Id_place_dst"]]

    #-------------------------------------------------------------------------------------------
    # extra params
    n_agents = len(df_agents)
    n_traits = int(max([df_agents["Trait"].max(), df_places["Trait"].max()]))

    #--------------------------------------------------------------------------------------------
    # run model
    if b_network:
        dct_out = cue2d.play_network(
            df_agents=df_agents,
            df_places=df_places,
            grd_ids=grd_ids,
            df_nodes=df_nodes,
            df_network=df_network,
            n_steps=n_steps,
            s_weight=s_weighting,
            b_tui=b_tui,
            b_return=b_return,
            b_trace=b_trace
        )

    else:
        dct_out = cue2d.play(
            df_agents=df_agents,
            df_places=df_places,
            grd_ids=grd_ids,
            n_steps=n_steps,
            s_weight=s_weighting,
            b_tui=b_tui,
            b_return=b_return,
            b_trace=b_trace
        )

    #--------------------------------------------------------------------------------------------
    # retrieve outputs
    df_agents_start = dct_out["Agents_Start"]
    df_places_start = dct_out["Places_Start"]
    df_agents_end = dct_out["Agents_End"]
    df_places_end = dct_out["Places_End"]
    n_places = len(df_places_end)

    #--------------------------------------------------------------------------------------------
    # run analyst
    n_shannon_agents_start = shannon_entropy(grd=df_agents['Trait'].values)
    n_shannon_agents_end = shannon_entropy(grd=df_agents_end['Trait'].values)
    n_shannon_places_start = shannon_entropy(grd=df_places['Trait'].values)
    n_shannon_places_end = shannon_entropy(grd=df_places_end['Trait'].values)
    dct_analyst = {
        'Step': ['Start', 'End'],
        'H_agents': [n_shannon_agents_start, n_shannon_agents_end],
        'H_places': [n_shannon_places_start, n_shannon_places_end],
    }
    df_analyst = pd.DataFrame(dct_analyst)

    #--------------------------------------------------------------------------------------------
    # export results
    if b_tui:
        status("exporting start/end results datasets")
    df_agents_start.to_csv(
        "{}/param_agents_2d_start.txt".format(s_dir_out), sep=";", index=False
    )
    df_agents_end.to_csv(
        "{}/param_agents_2d_end.txt".format(s_dir_out), sep=";", index=False
    )
    df_places_start.to_csv(
        "{}/param_places_2d_start.txt".format(s_dir_out), sep=";", index=False
    )
    df_places_end.to_csv(
        "{}/param_places_2d_end.txt".format(s_dir_out), sep=";", index=False
    )
    if b_tui:
        status("exporting start/end analyst")
    df_analyst.to_csv(
        "{}/analyst_start_end.txt".format(s_dir_out), sep=";", index=False
    )

    # --------------------------------------------------------------------------------------------
    # VISUALS
    # set aux lists
    lst_df = [df_agents_start, df_agents_end, df_places_start, df_places_end]
    lst_nms = [
        "hist_agents_2d_start",
        "hist_agents_2d_end",
        "hist_places_2d_start",
        "hist_places_2d_end",
    ]
    lst_ttl = [
        "Agents 2D Histogram | Start",
        "Agents 2D Histogram | End",
        "Places 2D Histogram | Start",
        "Places 2D Histogram | End",
    ]

    # --------------------------------------------------------------------------------------------
    # export histograms loop
    from visuals import plot_trait_histogram
    for i in range(len(lst_df)):
        df_lcl = lst_df[i]
        vct_hist, vct_bins = np.histogram(
            a=df_lcl["Trait"].values, bins=n_traits, range=(0, n_traits)
        )
        df_hist = pd.DataFrame({"Trait": vct_bins[1:], "Count": vct_hist})
        df_hist.to_csv("{}/{}.txt".format(s_dir_out, lst_nms[i]), sep=";", index=False)

        # ----------------------------------------------------------------------------------------
        # plot traits histograms
        plot_trait_histogram(
            df_data=df_lcl,
            n_traits=n_traits,
            n_bins=n_traits,
            s_ttl=lst_ttl[i],
            s_dir_out=s_dir_out,
            s_file_name="view_" + lst_nms[i],
            n_dpi=100,
            b_show=False,
        )
    # --------------------------------------------------------------------------------------------
    # plot traced variables
    if b_trace:
        if b_tui:
            status("exporting traced results datasets")

        # ----------------------------------------------------------------------------------------
        # transpose grids
        grd_traced_places_traits_t = dct_out["Simulation"]["Places_traits"].transpose()
        grd_traced_agents_x_t = dct_out["Simulation"]["Agents_x"].transpose()
        grd_traced_agents_y_t = dct_out["Simulation"]["Agents_y"].transpose()
        grd_traced_agents_traits_t = dct_out["Simulation"]["Agents_traits"].transpose()

        # ----------------------------------------------------------------------------------------
        # get fill size
        n_fill = int(np.log10(n_steps)) + 1

        # ----------------------------------------------------------------------------------------
        # deploy agents dataframes
        df_traced_agents_x = pd.DataFrame({"Step": np.arange(0, n_steps)})
        df_traced_agents_y = pd.DataFrame({"Step": np.arange(0, n_steps)})
        df_traced_agents_traits = pd.DataFrame({"Step": np.arange(0, n_steps)})

        # ----------------------------------------------------------------------------------------
        # loop to append fields to dataframe
        for i in range(n_agents):
            s_lcl_agent_x = "{}_{}_x".format(df_agents["Alias"].values[i], df_agents["Id"].values[i])
            s_lcl_agent_y = "{}_{}_y".format(df_agents["Alias"].values[i], df_agents["Id"].values[i])
            s_lcl_agent_trait = "{}_{}_Trait".format(
                df_agents["Alias"].values[i],
                df_agents["Id"].values[i]
            )
            df_traced_agents_x[s_lcl_agent_x] = grd_traced_agents_x_t[i]
            df_traced_agents_y[s_lcl_agent_y] = grd_traced_agents_y_t[i]
            df_traced_agents_traits[s_lcl_agent_trait] = grd_traced_agents_traits_t[i]

        # ----------------------------------------------------------------------------------------
        # deploy places dict
        dct_traced_places_traits = {
            "Step": np.arange(0, n_steps)
        }

        # ----------------------------------------------------------------------------------------
        # loop to append fields to dataframe
        for i in range(n_places):
            s_lcl_place_trait = "{}_{}_Trait".format(
                df_places_end["Alias"].values[i],
                int(df_places_end["Id"].values[i])
            )
            dct_traced_places_traits[s_lcl_place_trait] = grd_traced_places_traits_t[i]
        df_traced_places_traits = pd.DataFrame(dct_traced_places_traits)
        # ----------------------------------------------------------------------------------------
        # run series analyst
        # set H field for agents
        vct_h = np.zeros(len(df_traced_agents_traits), dtype='float32')
        for t in range(len(df_traced_agents_traits)):
            # get local traits
            vct_lcl_traits = df_traced_agents_traits.values[t][1:]
            # compute H
            vct_h[t] = shannon_entropy(grd=vct_lcl_traits)
        df_traced_agents_traits['H'] = vct_h
        # set H field for places
        vct_h = np.zeros(len(df_traced_places_traits), dtype='float32')
        for t in range(len(df_traced_places_traits)):
            # get local traits
            vct_lcl_traits = df_traced_places_traits.values[t][1:]
            # compute H
            vct_h[t] = shannon_entropy(grd=vct_lcl_traits)
        df_traced_places_traits['H'] = vct_h

        # ----------------------------------------------------------------------------------------
        # export csv files
        df_traced_agents_x.to_csv(
            "{}/traced_agents_x.txt".format(s_dir_out), sep=";", index=False
        )
        df_traced_agents_y.to_csv(
            "{}/traced_agents_y.txt".format(s_dir_out), sep=";", index=False
        )
        df_traced_agents_traits.to_csv(
            "{}/traced_agents_traits.txt".format(s_dir_out), sep=";", index=False
        )
        df_traced_places_traits.to_csv(
            "{}/traced_places_traits.txt".format(s_dir_out), sep=";", index=False
        )

        # ----------------------------------------------------------------------------------------
        # retrieve paths
        if b_network:
            df_paths = retrieve_paths(
                df_network=df_network,
                df_traced_agents_x=df_traced_agents_x,
                df_traced_agents_y=df_traced_agents_y
            )
            df_paths.to_csv(
                "{}/traced_agents_paths.txt".format(s_dir_out), sep=";", index=False
            )

        # ----------------------------------------------------------------------------------------
        # plot series
        from visuals import plot_traced_traits, plot_traced_positions, plot_traced_h
        # agents
        plot_traced_traits(
            df_data=df_traced_agents_traits,
            df_params=df_agents_start,
            n_traits=n_traits,
            s_dir_out=s_dir_out,
            s_file_name="view_traced_agents_traits",
            s_ttl="Agents Traits",
            b_dark=False,
            b_show=False,
        )
        plot_traced_positions(
            df_data=df_traced_agents_x,
            df_params=df_agents_start,
            n_positions=np.shape(grd_ids)[1],
            s_dir_out=s_dir_out,
            s_file_name="view_traced_agents_x",
            s_ttl="Agents X Positions",
            s_position="x",
            b_dark=False,
            b_show=False
        )
        plot_traced_positions(
            df_data=df_traced_agents_y,
            df_params=df_agents_start,
            n_positions=np.shape(grd_ids)[0],
            s_dir_out=s_dir_out,
            s_file_name="view_traced_agents_y",
            s_ttl="Agents Y Positions",
            s_position="y",
            b_dark=False,
            b_show=False
        )
        plot_traced_h(
            df_data=df_traced_agents_traits,
            s_dir_out=s_dir_out,
            s_file_name="view_traced_agents_H",
            s_ttl="Agents H",
            b_dark=False,
            b_show=False
        )
        # places
        plot_traced_traits(
            df_data=df_traced_places_traits,
            df_params=df_places_start,
            s_dir_out=s_dir_out,
            n_traits=n_traits,
            s_file_name="view_traced_places_traits",
            s_ttl="Places Traits",
            b_dark=False,
            b_show=False,
        )
        plot_traced_h(
            df_data=df_traced_places_traits,
            s_dir_out=s_dir_out,
            s_file_name="view_traced_places_H",
            s_ttl="Places H",
            b_dark=False,
            b_show=False
        )
        # plot animation frames
        if b_plot:
            s_dir_frames = "{}/frames".format(s_dir_out)
            os.mkdir(path=s_dir_frames)
            # call sub routine
            animate_frames_2d(
                s_param_agents="{}/param_agents_2d_start.txt".format(s_dir_out),
                s_param_places="{}/param_places_2d_start.txt".format(s_dir_out),
                s_places_map=f_places_map,
                s_traced_agents_x="{}/traced_agents_x.txt".format(s_dir_out),
                s_traced_agents_y="{}/traced_agents_y.txt".format(s_dir_out),
                s_traced_agents_traits="{}/traced_agents_traits.txt".format(s_dir_out),
                s_traced_places_traits="{}/traced_places_traits.txt".format(s_dir_out),
                s_dir_frames=s_dir_frames,
                s_dir_out=s_dir_out,
                b_tui=b_tui
            )


def compute_network(f_map, f_places, s_dir_out="C:/bin"):
    """

    :param f_map: map file
    :type f_map: str
    :param f_places: places parameter file
    :type f_places: str
    :param s_dir_out: output directory
    :type s_dir_out: str
    :return:
    :rtype:
    """
    import astar

    # -----------------------------------------------------------------------------------------------------------
    # Load map
    dct_meta, grd_places = inp.asc_raster(file=f_map, dtype="float32")

    # -----------------------------------------------------------------------------------------------------------
    # Load places data frame
    dct_places = inp.import_data_table(s_table_name="param_places_2d", s_filepath=f_places)
    df_places = dct_places["df"]
    df_places["Trait"] = df_places["Trait"].astype("float64")

    # -----------------------------------------------------------------------------------------------------------
    # Compute network
    df_net, df_nodes = astar.get_network(grd_places=grd_places, df_places=df_places, tui=True)

    # -----------------------------------------------------------------------------------------------------------
    # Compute Geometries
    df_wkt_nodes = astar.get_nodes_wkt(df_nodes=df_nodes, metadata=dct_meta)
    df_wkt_net = astar.get_network_wkt(df_network=df_net, metadata=dct_meta)

    # -----------------------------------------------------------------------------------------------------------
    # Export
    df_wkt_nodes.to_csv("{}/nodes.txt".format(s_dir_out), sep=";", index=False)
    df_wkt_net.to_csv("{}/network.txt".format(s_dir_out), sep=";", index=False)


def retrieve_paths(df_network, df_traced_agents_x, df_traced_agents_y):
    """
    Auxiliar function for retrieving the paths from traced agents
    :param df_network: network dataframe
    :type df_network: pandas.DataFrame
    :param df_traced_agents_x: x coordinates dataframe
    :type df_traced_agents_x: pandas.DataFrame
    :param df_traced_agents_y: y coordinates dataframe
    :type df_traced_agents_y: pandas.DataFrame
    :return: paths dataframe
    :rtype: pandas.DataFrame
    """
    df_network = df_network.copy()

    df_traced_agents_x = df_traced_agents_x.set_index("Step")
    df_traced_agents_y = df_traced_agents_y.set_index("Step")

    lst_agent = list()
    lst_step = list()
    lst_geoms = list()
    lst_path_i = list()
    lst_path_j = list()
    lst_euclid = list()
    lst_astar = list()

    for a in df_traced_agents_x.columns:
        s_agent = a[:-2]
        a_x = df_traced_agents_x["{}_x".format(s_agent)].values
        a_y = df_traced_agents_y["{}_y".format(s_agent)].values
        for t in range(1, len(a_x)):

            src_x = a_x[t - 1]
            src_y = a_y[t - 1]
            dst_x = a_x[t]
            dst_y = a_y[t]
            s_query = "y_src == {} and x_src == {} and y_dst == {} and x_dst == {}".format(
                src_y, src_x, dst_y, dst_x)
            #print(s_query)
            df_query = df_network.query(s_query)
            if len(df_query) > 0:
                #print("{} - step {}".format(s_agent, t))
                s_path_i = df_query["Path_y"].values[0]
                s_path_j = df_query["Path_x"].values[0]
                s_geom = df_query["Geom"].values[0]
                n_euclidean = df_query["Euclidean"].values[0]
                n_astar = df_query["AStar"].values[0]
                # append
                lst_step.append(t)
                lst_agent.append(s_agent)
                lst_geoms.append(s_geom)
                lst_path_i.append(s_path_i)
                lst_path_j.append(s_path_j)
                lst_euclid.append(n_euclidean)
                lst_astar.append(n_astar)

    df_out = pd.DataFrame(
        {
            "Agent": lst_agent,
            "Step": lst_step,
            "Euclidean": lst_euclid,
            "AStar": lst_astar,
            "Path_x": lst_path_j,
            "Path_y": lst_path_i,
            "Geom": lst_geoms
        }
    )

    return df_out


def animate_frames_1d(
        s_param_agents,
        s_param_places,
        s_traced_agents_x,
        s_traced_agents_traits,
        s_traced_places_traits,
        s_dir_frames,
        s_dir_out='C:/'
):
    """
    tool for a posteriori plotting of the CUE1d model
    :param s_param_agents: string filepath
    :param s_param_places: string filepath
    :param s_traced_agents_x: string filepath
    :param s_traced_agents_traits: string filepath
    :param s_traced_places_traits: string filepath
    :param s_dir_frames: string folder path (where frames are going to be saved)
    :param s_dir_out: string folder path
    :return:
    """
    from visuals import plot_cue_1d_pannel
    from out import export_gif

    # import places file
    dct_places = inp.import_data_table(s_table_name="param_places_1d", s_filepath=s_param_places)
    df_places = dct_places["df"]
    df_places["Trait"] = df_places["Trait"].astype("float64")
    # import agents file
    dct_agents = inp.import_data_table(s_table_name="param_agents_1d", s_filepath=s_param_agents)
    df_agents = dct_agents["df"]
    df_agents["Trait"] = df_agents["Trait"].astype("float64")

    # get params
    n_agents = len(df_agents)
    n_places = len(df_places)
    n_traits = int(max([df_agents["Trait"].max(), df_places["Trait"].max()]))

    status("exporting traced results datasets")

    df_traced_agents_x = pd.read_csv(s_traced_agents_x, sep=';', index_col='Step')
    df_traced_agents_traits = pd.read_csv(s_traced_agents_traits, sep=';', index_col='Step')
    df_traced_places_traits = pd.read_csv(s_traced_places_traits, sep=';', index_col='Step')

    # transpose grids
    grd_traced_places_traits_t = df_traced_places_traits.values.transpose()
    grd_traced_agents_x_t = df_traced_agents_x.values.transpose()
    grd_traced_agents_traits_t = df_traced_agents_traits.values.transpose()

    n_steps = len(df_traced_agents_traits)
    # get fill size
    n_fill = int(np.log10(n_steps)) + 1

    # check dir
    if os.path.isdir(s_dir_frames):
        pass
    else:
        os.mkdir(s_dir_frames)

    # plot animation frames
    status("plotting frames", process=True)
    s_cmap = "viridis"  # 'tab20c'
    for t in range(n_steps):
        status(
            "CUE1d :: plotting step {} [{:.2f}%]".format(
                t, 100 * (t + 1) / n_steps
            )
        )
        plot_cue_1d_pannel(
            n_step=t,
            n_traits=n_traits,
            n_places=n_places,
            n_agents=n_agents,
            grd_places_traits_t=grd_traced_places_traits_t,
            grd_agents_traits_t=grd_traced_agents_traits_t,
            grd_agents_x_t=grd_traced_agents_x_t,
            s_ttl="Step = {}".format(t),
            s_dir_out=s_dir_frames,
            s_file_name="frame_{}".format(str(t).zfill(n_fill)),
            b_show=False,
            b_dark=False,
        )
    # export animation
    status("generating gif animation", process=True)
    export_gif(
        dir_output=s_dir_out,
        dir_images=s_dir_frames,
        nm_gif="animation",
        kind="png",
        suf="", #
    )


def animate_frames_2d(
        s_param_agents,
        s_param_places,
        s_places_map,
        s_traced_agents_x,
        s_traced_agents_y,
        s_traced_agents_traits,
        s_traced_places_traits,
        s_dir_frames,
        s_dir_out='C:/',
        b_tui=True
):
    """
    tool for a posteriori plotting of the CUE1d model
    :param s_param_agents: string filepath
    :param s_param_places: string filepath
    :param s_traced_agents_x: string filepath
    :param s_traced_agents_y: string filepath
    :param s_traced_agents_traits: string filepath
    :param s_traced_places_traits: string filepath
    :param s_dir_frames: string folder path (where frames are going to be saved)
    :param s_dir_out: string folder path
    :return:
    """
    import matplotlib.pyplot as plt
    import cue2d
    from visuals import plot_cue_2d_pannel
    from out import export_gif

    # --------------------------------------------------------------------------------------------
    # import places file
    dct_places = inp.import_data_table(s_table_name="param_places_2d", s_filepath=s_param_places)
    df_places = dct_places["df"]
    df_places["Trait"] = df_places["Trait"].astype("float64")
    # --------------------------------------------------------------------------------------------
    # import agents file
    dct_agents = inp.import_data_table(s_table_name="param_agents_2d", s_filepath=s_param_agents)
    df_agents = dct_agents["df"]
    df_agents["Trait"] = df_agents["Trait"].astype("float64")

    # -------------------------------------------------------------------------------------------
    # import places map
    meta, grd_ids = inp.asc_raster(file=s_places_map)

    # -------------------------------------------------------------------------------------------
    # extra params
    n_agents = len(df_agents)
    n_places = len(df_places)
    n_traits = int(max([df_agents["Trait"].max(), df_places["Trait"].max()]))

    # -------------------------------------------------------------------------------------------
    # traced datasets
    df_traced_agents_x = pd.read_csv(s_traced_agents_x, sep=';', index_col='Step')
    df_traced_agents_y = pd.read_csv(s_traced_agents_y, sep=';', index_col='Step')
    df_traced_agents_traits = pd.read_csv(s_traced_agents_traits, sep=';', index_col='Step')
    df_traced_places_traits = pd.read_csv(s_traced_places_traits, sep=';', index_col='Step')

    # -------------------------------------------------------------------------------------------
    # extra params
    n_steps = len(df_traced_agents_traits)
    # get fill size
    n_fill = int(np.log10(n_steps)) + 1

    # -------------------------------------------------------------------------------------------
    # check dir
    if os.path.isdir(s_dir_frames):
        pass
    else:
        os.mkdir(s_dir_frames)

    # -------------------------------------------------------------------------------------------
    # plot animation frames
    if b_tui:
        status("plotting frames", process=True)
    s_cmap = "viridis"  # 'tab20c'
    for t in range(n_steps):
        if b_tui:
            status(
                "CUE2d :: plotting step {} [{:.2f}%]".format(
                    t, 100 * (t + 1) / n_steps
                )
            )
        # --------------------------------------------------------------------------------------
        # map traits
        grd_traits = cue2d.map_traits(
            grd_ids=grd_ids,
            vct_ids=df_places["Id"].values,
            vct_traits=df_traced_places_traits.values[t][:-1]
        )
        grd_traits[grd_ids == 0] = np.nan

        plot_cue_2d_pannel(
            grd_traits=grd_traits,
            n_step=t,
            n_traits=n_traits,
            n_agents=n_agents,
            n_places=n_places,
            vct_places_traits=df_traced_places_traits.values[t][:-1],
            vct_agents_traits=df_traced_agents_traits.values[t][:-1],
            vct_agents_x=df_traced_agents_x.values[t],
            vct_agents_y=df_traced_agents_y.values[t],
            s_ttl="Step = {}".format(t),
            s_dir_out=s_dir_frames,
            s_file_name="frame_{}".format(str(t).zfill(n_fill)),
            b_show=False,
            b_dark=False,
        )
    # export animation
    if b_tui:
        status("generating gif animation", process=True)
    export_gif(
        dir_output=s_dir_out,
        dir_images=s_dir_frames,
        nm_gif="animation",
        kind="png",
        suf="", #
    )



def sal_agents_cue2dnet(s_fsim, s_fbat, s_dir_out="C:/bin", b_wkplc=True):
    """
    SAL batch for agents (network 2D model)
    :param s_fsim: simulation file
    :type s_fsim: str
    :param s_fbat: batch file
    :type s_fbat: str
    :param s_dir_out: output directory
    :type s_dir_out: str
    :param b_wkplc: workplace flag
    :type b_wkplc: bool
    :return:
    :rtype:
    """
    from analyst import shannon_entropy


    # ------------------------------------------------------------------------------------------
    # import reference simulation param_simulation_2d.txt
    dct_fsim = inp.import_data_table(s_table_name="param_simulation_network_2d", s_filepath=s_fsim)
    df_param_sim = dct_fsim["df"]

    # ------------------------------------------------------------------------------------------
    # get agents file
    f_agents = (
        df_param_sim.loc[df_param_sim["Metadata"] == "Agents File", "Value"]
            .values[0]
            .strip()
    )

    # -------------------------------------------------------------------------------------------
    # import agents file
    dct_agents = inp.import_data_table(s_table_name="param_agents_2d", s_filepath=f_agents)
    df_agents = dct_agents["df"]
    df_agents["Trait"] = df_agents["Trait"].astype("float64")

    # ------------------------------------------------------------------------------------------
    # import batch file
    dct_fbat = inp.import_data_table(s_table_name="param_batch_simulation", s_filepath=s_fbat)
    df_batch = dct_fbat["df"]

    # ------------------------------------------------------------------------------------------
    # parameter 1
    p1_name = df_batch["Parameter"].values[0].strip()
    p1_min = df_batch["Min"].values[0]
    p1_max = df_batch["Max"].values[0]
    p1_grid = df_batch["Grid"].values[0]

    # ------------------------------------------------------------------------------------------
    # parameter 2
    p2_name = df_batch["Parameter"].values[1].strip()
    p2_min = df_batch["Min"].values[1]
    p2_max = df_batch["Max"].values[1]
    p2_grid = df_batch["Grid"].values[1]
    p1_values = np.linspace(p1_min, p1_max, p1_grid)
    p2_values = np.linspace(p2_min, p2_max, p2_grid)

    # ------------------------------------------------------------------------------------------
    # number of runs
    n_runs = len(p2_values) * len(p1_values)
    grd_h_delta_agents = np.zeros(shape=(len(p1_values), len(p2_values)))
    grd_h_delta_places = np.zeros(shape=(len(p1_values), len(p2_values)))

    # ------------------------------------------------------------------------------------------
    # get run folder
    if b_wkplc:
        s_workplace = (
            df_param_sim.loc[df_param_sim["Metadata"] == "Run Folder", "Value"]
            .values[0]
            .strip()
        )
        s_dir_out = backend.create_rundir(label="Batch_CUE2d_NET", wkplc=s_workplace)
    s_dir_runs = backend.create_rundir(label="Batch_runs", wkplc=s_dir_out, b_timestamp=False)

    # ------------------------------------------------------------------------------------------
    # main batch loop
    c = 1
    for i in range(len(p1_values)):
        p1 = p1_values[i]
        if p1 >= 1:
            p1_sval = str(int(p1))
        else:
            p1_sval = str(int(100 * p1))
        for j in range(len(p2_values)):
            p2 = p2_values[j]
            if p2 >= 1:
                p2_sval = str(int(p2))
            else:
                p2_sval = str(int(100 * p2))
            # ------------------------------------------------------------------------------------------
            # set local simulation dir
            s_label = "Batch_{}{}_{}{}".format(p1_name, p1_sval, p2_name, p2_sval)
            backend.status("{}\t\tStep {} of {}\t[{:.2f} %]".format(s_label, c, n_runs, 100 * c /n_runs))
            s_dir = backend.create_rundir(label=s_label, b_timestamp=False, wkplc=s_dir_runs)

            # ------------------------------------------------------------------------------------------
            # set local simulation parameters
            df_param_sim_lcl = df_param_sim.copy()

            # ------------------------------------------------------------------------------------------
            # update timestamp value
            df_param_sim_lcl.loc[
                df_param_sim["Metadata"] == "Timestamp", "Value"
            ] = backend.timestamp_log()

            # ------------------------------------------------------------------------------------------
            # update run dir value
            df_param_sim_lcl.loc[
                df_param_sim["Metadata"] == "Run Folder", "Value"
            ] = s_dir

            # ------------------------------------------------------------------------------------------
            # set local agents file
            df_agents_lcl = df_agents.copy()
            # scale values to the grid reference value
            df_agents_lcl[p1_name] = p1 * (df_agents_lcl[p1_name] / df_agents_lcl[p1_name].min())
            df_agents_lcl[p2_name] = p2 * (df_agents_lcl[p2_name] / df_agents_lcl[p2_name].min())

            # ------------------------------------------------------------------------------------------
            # update agents file
            f_agents_lcl = "{}/param_agents_2d_input.txt".format(s_dir)
            df_agents_lcl.to_csv(f_agents_lcl, sep=";", index=False)
            # update
            df_param_sim_lcl.loc[
                df_param_sim["Metadata"] == "Agents File", "Value"
            ] = f_agents_lcl

            # ------------------------------------------------------------------------------------------
            # export simulation network
            fsim_lcl = "{}/param_simulation_network_2d.txt".format(s_dir)
            df_param_sim_lcl.to_csv(fsim_lcl, sep=";", index=False)

            # ------------------------------------------------------------------------------------------
            # run tool
            run_cue2d(s_fsim=fsim_lcl, b_network=True, s_dir_out=s_dir, b_wkplc=False, b_tui=False)

            # ------------------------------------------------------------------------------------------
            # collect analyst data

            # agents analysis
            df_agents_start = pd.read_csv("{}/param_agents_2d_start.txt".format(s_dir), sep=";")
            df_agents_end = pd.read_csv("{}/param_agents_2d_end.txt".format(s_dir), sep=";")
            h_agents_start = shannon_entropy(grd=df_agents_start["Trait"].values)
            h_agents_end = shannon_entropy(grd=df_agents_end["Trait"].values)
            h_agents_delta = h_agents_end - h_agents_start
            grd_h_delta_agents[i][j] = h_agents_delta

            # places analysis
            df_places_start = pd.read_csv("{}/param_places_2d_start.txt".format(s_dir), sep=";")
            df_places_end = pd.read_csv("{}/param_places_2d_end.txt".format(s_dir), sep=";")
            h_places_start = shannon_entropy(grd=df_places_start["Trait"].values)
            h_places_end = shannon_entropy(grd=df_places_end["Trait"].values)
            h_places_delta = h_places_end - h_places_start
            grd_h_delta_places[i][j] = h_places_delta

            # update counter
            c = c + 1

    # plot batch visuals

    vmax = np.max(np.abs([grd_h_delta_agents, grd_h_delta_places]))

    p1_decimals = 1
    if p1_name == "C":
        p1_decimals = 2
    p2_decimals = 1
    if p2_name == "C":
        p2_decimals = 2

    visuals.plot_sal_grid(
        grd=grd_h_delta_places,
        p1_values=np.round(p1_values, p1_decimals),
        p2_values=np.round(p2_values, p2_decimals),
        p1_name=p1_name,
        p2_name=p2_name,
        s_dir_out=s_dir_out,
        v_max=vmax,
        s_file_name="DeltaH-SAL_places_{}_{}".format(p1_name, p2_name),
        s_ttl="Delta H of Places Traits | Variables: {} and {}".format(p1_name, p2_name),
        b_show=False
    )

    visuals.plot_sal_grid(
        grd=grd_h_delta_agents,
        p1_values=np.round(p1_values, p1_decimals),
        p2_values=np.round(p2_values, p2_decimals),
        p1_name=p1_name,
        p2_name=p2_name,
        s_dir_out=s_dir_out,
        v_max=vmax,
        s_file_name="DeltaH-SAL_agents_{}_{}".format(p1_name, p2_name),
        s_ttl="Delta H of Agents Traits | Variables: {} and {}".format(p1_name, p2_name),
        b_show=False
    )

    return s_dir_out

if __name__ == "__main__":

    # --------------------------------------------------------------------------------------------
    # run 1d
    #run_cue1d(s_fsim="./samples/param_simulation_1d.txt")

    # --------------------------------------------------------------------------------------------
    # run 2d
    #run_cue2d(s_fsim="./samples/param_simulation_2d.txt")

    # --------------------------------------------------------------------------------------------
    # run 2d network
    fsim = "./demo/benchmark1/benchmark1_param_simulation.txt"
    #fsim = "./demo/saoleo/saoleo_param_simulation.txt"
    run_cue2d(s_fsim=fsim, b_network=True)

    # --------------------------------------------------------------------------------------------
    # run network analyst
    #fmap = "./demo/benchmark1/benchmark1.asc"
    #fmap = "./demo/saoleo/saoleo_small_map.asc"
    #fplaces = "./demo/saoleo/saoleo_small_places.txt"
    #compute_network(f_map=fmap, f_places=fplaces, s_dir_out="C:/bin")

    # --------------------------------------------------------------------------------------------
    # run batch
    #fbat = "./samples/param_batch_simulation.txt"
    #fsim = "./demo/benchmark1/benchmark1_param_simulation.txt"
    #sal_agents_cue2dnet(
    #    s_fsim=fsim,
    #    s_fbat=fbat
    #)


