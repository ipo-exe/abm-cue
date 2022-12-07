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


def map_traits(grd_ids, vct_traits, vct_ids):
    grd_traits = np.zeros(shape=np.shape(grd_ids), dtype="float32")
    for i in range(len(vct_traits)):
        grd_traits = grd_traits + (vct_traits[i] * (grd_ids == vct_ids[i]))
    return grd_traits


def play(df_agents, df_places, grd_ids, n_steps, b_tui=False, b_trace=True, b_return=False):
    """
    Simulation of CUE 2D

    :param df_agents: agents dataframe
    :type df_agents: pandas.DataFrame
    :param df_places: places dataframe
    :type df_places: pandas.DataFrame
    :param grd_ids: places ids map
    :type grd_ids: numpy.ndarray
    :param n_steps: number of simulation steps
    :type n_steps: int
    :param b_tui: boolean to terminal display
    :type b_tui: bool
    :param b_trace: boolean to traceback simulation
    :type b_trace: bool
    :return: simulation object
    :rtype: dict
    """
    # ------------------------------------------------------------------------------------------
    # df_places setup
    # first get unique places found in the ids map
    df_places_grd = pd.DataFrame(
        {
            "Id": np.unique(grd_ids)
        }
    )
    # remove Id = 0
    df_places_grd = df_places_grd.query("Id != 0")
    # then merge places dataframes
    df_places = pd.merge(
        how='left',
        left=df_places_grd,
        right=df_places[["Id", "Trait", "D", "Name", "Alias", "Color"]],
        left_on="Id",
        right_on="Id"
    )

    # ------------------------------------------------------------------------------------------
    # start up
    s_dtype = "float32"
    n_agents = len(df_agents)
    n_places = len(df_places)
    n_rows = np.shape(grd_ids)[0]
    n_cols = np.shape(grd_ids)[1]

    # ------------------------------------------------------------------------------------------
    # scanning window parameters set up
    lst_unique_beta = list(df_agents["Beta"].unique())  # get unique beta (radius size) values
    dct_window = dict()
    # construction loop
    for n_beta in lst_unique_beta:

        # --------------------------------------------------------------------------------------
        # get scanning window parameters
        vct_window_rows, vct_window_cols = backend.get_window_ids(
            n_rows=n_rows,
            n_cols=n_cols,
            n_rsize=n_beta,
            b_flat=True
        )

        # --------------------------------------------------------------------------------------
        # remove the origin from window
        lst_aux_rows = list()
        lst_aux_cols = list()
        for i in range(len(vct_window_rows)):
            if vct_window_rows[i] == 0 and vct_window_cols[i] == 0:
                pass
            else:
                lst_aux_rows.append(vct_window_rows[i])
                lst_aux_cols.append(vct_window_cols[i])

        # --------------------------------------------------------------------------------------
        # get window base ids
        vct_rows_base_ids = np.array(lst_aux_rows, dtype="uint16")
        vct_cols_base_ids = np.array(lst_aux_cols, dtype="uint16")

        # --------------------------------------------------------------------------------------
        # deploy recyclable window dataframe
        n_window_size = len(vct_rows_base_ids)
        df_window = pd.DataFrame(
            {
                "rows": vct_rows_base_ids,
                "cols": vct_cols_base_ids,
                "x": np.zeros(n_window_size, dtype="uint16"),
                "y": np.zeros(n_window_size, dtype="uint16"),
                "Id": np.zeros(n_window_size, dtype="int16"),
            }
        )
        # --------------------------------------------------------------------------------------
        # append to dict
        dct_window[str(n_beta)] = {
            "df": df_window
        }

    # ------------------------------------------------------------------------------------------
    # define random seeds prior to simulation loop
    np.random.seed(backend.get_seed())
    grd_seeds = np.random.randint(
        low=100,
        high=999,
        size=(n_steps, n_agents),
        dtype="uint16"
    )

    # ------------------------------------------------------------------------------------------
    # tracing variables
    if b_trace:
        grd_traced_agents_x = np.zeros(shape=(n_steps, n_agents), dtype=s_dtype)
        grd_traced_agents_y = np.zeros(shape=(n_steps, n_agents), dtype=s_dtype)
        grd_traced_agents_traits = np.zeros(shape=(n_steps, n_agents), dtype=s_dtype)
        grd_traced_places_traits = np.zeros(shape=(n_steps, n_places), dtype=s_dtype)
        grd_traced_places_traits[0] = df_places["Trait"].values
        grd_traced_agents_traits[0] = df_agents["Trait"].values
        grd_traced_agents_x[0] = df_agents["x"].values
        grd_traced_agents_y[0] = df_agents["y"].values

    # ------------------------------------------------------------------------------------------
    # return variables
    if b_return:
        vct_agents_origin_x = df_agents.copy()["x"].values
        vct_agents_origin_y = df_agents.copy()["y"].values

    # ------------------------------------------------------------------------------------------
    # prepare output dict
    dct_output = {"Agents_Start": df_agents.copy(), "Places_Start": df_places.copy()}

    # ------------------------------------------------------------------------------------------
    # main simulation loop:
    for t in range(n_steps):
        if b_tui:
            backend.status(
                "CUE2d :: simulation step {} [{:.2f}%]".format(t + 1, 100 * (t + 1) / n_steps)
            )

        # --------------------------------------------------------------------------------------
        # agents loop
        for a in range(len(df_agents)):

            # ----------------------------------------------------------------------------------
            # get agents attributes
            a_id = df_agents["Id"].values[a]
            a_x = df_agents["x"].values[a]
            a_y = df_agents["y"].values[a]
            a_trait = df_agents["Trait"].values[a]
            a_alpha = df_agents["Alpha"].values[a]
            a_beta = df_agents["Beta"].values[a]
            a_c = df_agents["C"].values[a]

            # ----------------------------------------------------------------------------------
            # access window dataframe using
            df_window = dct_window[str(a_beta)]["df"]
            # update window x and y
            df_window["x"] = (a_x + df_window["cols"].values) % n_cols
            df_window["y"] = (a_y + df_window["rows"].values) % n_rows
            # find cells ids
            for i in range(len(df_window)):
                lcl_x = df_window["x"].values[i]
                lcl_y = df_window["y"].values[i]
                df_window["Id"].values[i] = grd_ids[lcl_y][lcl_x]

            # ----------------------------------------------------------------------------------
            # get agent's place id based on its location
            p_id = grd_ids[a_y][a_x]

            # ----------------------------------------------------------------------------------
            # action conditional

            # todo problems with return feature

            np.random.seed(grd_seeds[t, a])  # restart random state
            if p_id == 0:  # just move to indoors weighted

                # ------------------------------------------------------------------------------
                # filter window
                df_wnd_move = df_window.query("Id != 0")

                # ------------------------------------------------------------------------------
                # movement conditional
                if len(df_wnd_move) == 0:  # there is no indoor place to go
                    df_wnd_move = df_window.copy()
                    # then move randomly
                    n_next_index = np.random.choice(
                        a=np.arange(len(df_wnd_move)),
                        size=1
                    )[0]  # get the first
                else:

                    # --------------------------------------------------------------------------
                    # append fields
                    df_wnd_move = pd.merge(
                        how='left',
                        left=df_wnd_move,
                        right=df_places,
                        left_on="Id",
                        right_on="Id"
                    )

                    # --------------------------------------------------------------------------
                    # compute discrepancy
                    df_wnd_move["Discrepancy"] = np.abs(
                        a_trait - df_wnd_move["Trait"].values
                    )

                    # --------------------------------------------------------------------------
                    # compute selection Interac_score
                    df_wnd_move["Interac_score"] = (
                            df_wnd_move["Discrepancy"].max() - df_wnd_move["Discrepancy"] + 1
                    )

                    # --------------------------------------------------------------------------
                    # normalize
                    # set score = zero where place is beyond alpha threshold
                    df_wnd_move["Interac_score"] = df_wnd_move["Interac_score"].values * (
                            df_wnd_move["Discrepancy"].values <= a_alpha
                    )

                    # --------------------------------------------------------------------------
                    # compute probabilistic weights
                    if df_wnd_move["Interac_score"].sum() == 0:
                        # uniform distribution when all scores == 0:
                        df_wnd_move["Interac_prob"] = 1 / len(df_wnd_move)
                    else:
                        df_wnd_move["Interac_prob"] = (
                                df_wnd_move["Interac_score"] / df_wnd_move["Interac_score"].sum()
                        )

                    # --------------------------------------------------------------------------
                    # weighted random sampling
                    n_next_index = np.random.choice(
                        a=np.arange(len(df_wnd_move)),
                        size=1,
                        p=df_wnd_move["Interac_prob"].values
                    )[0]  # get the first
            else:  # interact and move to outdoors randomly

                # ------------------------------------------------------------------------------
                # interact

                # get place dataframe index
                p_index = df_places.query("Id == {}".format(p_id)).index[0]
                # get place trait
                p_trait = df_places["Trait"].values[p_index]
                # get place d
                p_d = df_places["D"].values[p_index]

                # ------------------------------------------------------------------------------
                # apply interaction criteria
                n_discrepancy = np.abs(a_trait - p_trait)
                if n_discrepancy <= a_alpha:
                    # compute means
                    a_mean = (a_trait + (a_c * p_trait)) / (1 + a_c)
                    p_mean = (p_trait + (p_d * a_trait)) / (1 + p_d)

                    # replace in simulation dataframes
                    df_agents["Trait"].values[a] = a_mean
                    df_places["Trait"].values[p_index] = p_mean

                # ------------------------------------------------------------------------------
                # move to outdoors
                # filter window
                df_wnd_move = df_window.query("Id == 0")
                #
                if len(df_wnd_move) == 0:  # there is no outdoor place to go
                    df_wnd_move = df_window.copy()
                # then move randomly indoors
                n_next_index = np.random.choice(
                    a=np.arange(len(df_wnd_move)),
                    size=1
                )[0]  # get the first

            # ----------------------------------------------------------------------------------
            # update agent position
            df_agents["x"].values[a] = df_wnd_move["x"].values[n_next_index]
            df_agents["y"].values[a] = df_wnd_move["y"].values[n_next_index]

        # --------------------------------------------------------------------------------------
        # trace variables
        if b_trace:
            grd_traced_places_traits[t] = df_places["Trait"].values
            grd_traced_agents_traits[t] = df_agents["Trait"].values
            grd_traced_agents_x[t] = df_agents["x"].values
            grd_traced_agents_y[t] = df_agents["y"].values

        # --------------------------------------------------------------------------------------
        # reset position values
        if b_return:
            # reset x
            df_agents["x"] = vct_agents_origin_x
            # reset y
            df_agents["y"] = vct_agents_origin_y

    # ------------------------------------------------------------------------------------------
    # prepare output dict
    dct_output["Agents_End"] = df_agents.copy()
    dct_output["Places_End"] = df_places.copy()

    # ------------------------------------------------------------------------------------------
    # append extra content
    if b_trace:
        dct_output["Simulation"] = {
            "Places_traits": grd_traced_places_traits,
            "Agents_traits": grd_traced_agents_traits,
            "Agents_x": grd_traced_agents_x,
            "Agents_y": grd_traced_agents_y,
        }
    return dct_output



if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import random


    n_steps = 50
    n_agents = 3

    # create agents dataframe (read from table)
    df_agents = pd.DataFrame(
        {
            "Id": np.arange(1, n_agents + 1),
            "x": [12, 12, 12],
            "y": [5, 10, 15],
            "Trait": [5.0, 5.0, 5.0],
            "Alpha": [3, 3, 3],
            "Beta": [1, 5, 3],
            "C": [0.1, 0.2, 0.0]
        }
    )

    # read places parameters table
    df_places_input = pd.read_csv("C:/gis/bin/places_params.csv", sep=";")
    df_places_input = df_places_input[["Id", "Trait"]]
    df_places_input["D"] = 0.1
    df_places_input["Name"] = "P"
    for i in range(len(df_places_input)):
        df_places_input["Name"].values[i] = "P" + str(df_places_input["Id"].values[i])
    df_places_input["Alias"] = df_places_input["Name"]

    number_of_colors = len(df_places_input)

    color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]

    df_places_input["color"] = color

    df_places_input.to_csv("C:/gis/bin/places_param_2d.txt", sep=";", index=False)

    # read ID map
    meta, grd_ids = inp.asc_raster(file="C:/gis/bin/places_demo_5m.asc")


    #grd_traits = map_places_traits(grd_ids=grd_ids, df_places=df_places)

    play(
        df_agents=df_agents,
        df_places=df_places_input,
        grd_ids=grd_ids,
        n_steps=n_steps,
        b_trace=True,
        b_tui=False
    )