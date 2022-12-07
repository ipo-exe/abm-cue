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
    # import param_simulation.txt
    dct_fsim = inp.import_data_table(s_table_name="param_simulation", s_filepath=s_fsim)
    df_param_sim = dct_fsim["df"]

    # update timestamp value
    df_param_sim.loc[
        df_param_sim["Metadata"] == "Timestamp", "Value"
    ] = backend.timestamp_log()

    # get run folder
    if b_wkplc:
        s_workplace = (
            df_param_sim.loc[df_param_sim["Metadata"] == "Run Folder", "Value"]
            .values[0]
            .strip()
        )
        s_dir_out = backend.create_rundir(label="CUE1d", wkplc=s_workplace)

    # get places file
    f_places = (
        df_param_sim.loc[df_param_sim["Metadata"] == "Places File", "Value"]
        .values[0]
        .strip()
    )
    # get agents file
    f_agents = (
        df_param_sim.loc[df_param_sim["Metadata"] == "Agents File", "Value"]
        .values[0]
        .strip()
    )

    # get simulation parameters
    #
    # number of steps
    n_steps = int(
        df_param_sim.loc[df_param_sim["Metadata"] == "Steps", "Value"].values[0].strip()
    )
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

    # import places file
    dct_places = inp.import_data_table(s_table_name="param_places", s_filepath=f_places)
    df_places = dct_places["df"]
    df_places["Trait"] = df_places["Trait"].astype("float64")

    # import agents file
    dct_agents = inp.import_data_table(s_table_name="param_agents", s_filepath=f_agents)
    df_agents = dct_agents["df"]
    df_agents["Trait"] = df_agents["Trait"].astype("float64")

    # extra params
    n_agents = len(df_agents)
    n_places = len(df_places)
    n_traits = int(max([df_agents["Trait"].max(), df_places["Trait"].max()]))

    # ------------------------------
    #
    # run model
    dct_out = cue1d.play(
        df_agents=df_agents.copy(),
        df_places=df_places.copy(),
        n_steps=n_steps,
        b_tui=True,
        b_return=b_return,
        b_trace=b_trace,
    )

    # ------------------------------
    #
    # retrieve outputs
    df_agents_end = dct_out["Agents"]
    df_places_end = dct_out["Places"]

    # ------------------------------
    #
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

    # ------------------------------
    #
    # export results
    status("exporting start/end results datasets")
    df_agents.to_csv(
        "{}/param_agents_start.txt".format(s_dir_out), sep=";", index=False
    )
    df_agents_end.to_csv(
        "{}/param_agents_end.txt".format(s_dir_out), sep=";", index=False
    )
    df_places.to_csv(
        "{}/param_places_start.txt".format(s_dir_out), sep=";", index=False
    )
    df_places_end.to_csv(
        "{}/param_places_end.txt".format(s_dir_out), sep=";", index=False
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
    # ------------------------------
    #
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


def run_cue2d(s_fsim, b_wkplc=True, s_dir_out="C:/bin"):
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
    # get simulation parameters
    #
    # number of steps
    n_steps = int(
        df_param_sim.loc[df_param_sim["Metadata"] == "Steps", "Value"].values[0].strip()
    )

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

    #-------------------------------------------------------------------------------------------
    # extra params
    n_agents = len(df_agents)
    n_traits = int(max([df_agents["Trait"].max(), df_places["Trait"].max()]))

    #--------------------------------------------------------------------------------------------
    # run model
    dct_out = cue2d.play(
        df_agents=df_agents,
        df_places=df_places,
        grd_ids=grd_ids,
        n_steps=n_steps,
        b_tui=True,
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
        # deploy places dataframes
        df_traced_places_traits = pd.DataFrame({"Step": np.arange(0, n_steps)})

        # ----------------------------------------------------------------------------------------
        # loop to append fields to dataframe
        for i in range(n_places):
            s_lcl_place_trait = "{}_{}_Trait".format(
                df_places_end["Alias"].values[i],
                df_places_end["Id"].values[i]
            )
            df_traced_places_traits[s_lcl_place_trait] = grd_traced_places_traits_t[i]

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
                s_dir_out=s_dir_out
            )


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
    dct_places = inp.import_data_table(s_table_name="param_places", s_filepath=s_param_places)
    df_places = dct_places["df"]
    df_places["Trait"] = df_places["Trait"].astype("float64")
    # import agents file
    dct_agents = inp.import_data_table(s_table_name="param_agents", s_filepath=s_param_agents)
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
        s_dir_out='C:/'
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
    status("plotting frames", process=True)
    s_cmap = "viridis"  # 'tab20c'
    for t in range(n_steps):
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
            vct_traits=df_traced_places_traits.values[t][1:]
        )
        grd_traits[grd_traits == 0] = np.nan
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
    status("generating gif animation", process=True)
    export_gif(
        dir_output=s_dir_out,
        dir_images=s_dir_frames,
        nm_gif="animation",
        kind="png",
        suf="", #
    )






if __name__ == "__main__":
    run_cue2d(s_fsim="./samples/param_simulation_2d.txt")