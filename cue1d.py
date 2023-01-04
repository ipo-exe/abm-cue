"""

CUE 1d routines source code

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
import backend


def linear_prob(x, x_max):
    """
    linear probability function
    :param x: value
    :type x: float or numpy array
    :param x_max: x max value
    :type x_max: float
    :return: probability
    :rtype:
    """
    return ((-2 / np.square(x_max)) * x) + (2/x_max)


def play(df_agents, df_places, n_steps, s_weight='uniform', b_tui=False, b_return=False, b_trace=True):
    """
    Run the CUE 1d simulation
    :param df_agents: pandas dataframe of agents
    :param df_places: pandas dataframe of places
    :param n_steps: int number of time steps
    :param s_weight: sampling method type. Options: 'uniform', 'linear'
    :type s_weight: str
    :param b_tui: boolean to terminal display
    :param b_return: boolean to return agent back to initial position every time step
    :param b_trace: boolean to trace back simulation
    :return: output dictionary
    """
    # ------------------------------------------------------------------------------------------
    # start up
    s_dtype = "float32"
    n_agents = len(df_agents)
    n_places = len(df_places)

    # ------------------------------------------------------------------------------------------
    # scanning window parameters set up

    # get unique beta (radius size) values
    lst_unique_rc = list(df_agents["R"].unique())
    dct_window = dict()
    for n_rc in lst_unique_rc:

        # --------------------------------------------------------------------------------------
        # get scanning window parameters
        vct_window_rows, vct_window_cols = backend.get_window_ids(
            n_rows=n_places,
            n_cols=n_places,
            n_rsize=n_rc,
            b_flat=False
        )

        # --------------------------------------------------------------------------------------
        # use columns only (1D simulation)
        if b_return:
            lst_aux = list(vct_window_cols[0])
        else:
            # remove the origin from window
            lst_aux = list()
            for e in vct_window_cols[0]:
                if e == 0:
                    pass
                else:
                    lst_aux.append(e)

        # --------------------------------------------------------------------------------------
        # get window base ids
        vct_rows_base_ids = np.array(lst_aux, dtype="uint16")

        # --------------------------------------------------------------------------------------
        # deploy recyclable window dataframe
        n_window_size = len(vct_rows_base_ids)
        df_window = pd.DataFrame(
            {
                "x": np.zeros(n_window_size, dtype="uint16"),
                "Trait": np.zeros(n_window_size, dtype=s_dtype),
                "C": np.zeros(n_window_size, dtype=s_dtype),
                "Discr": np.zeros(n_window_size, dtype=s_dtype),
                "Prob": np.zeros(n_window_size, dtype=s_dtype),
            }
        )

        # --------------------------------------------------------------------------------------
        # append to dict
        dct_window[str(n_rc)] = {
            "ids": vct_rows_base_ids,
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
        grd_traced_agents_traits = np.zeros(shape=(n_steps, n_agents), dtype=s_dtype)
        grd_traced_places_traits = np.zeros(shape=(n_steps, n_places), dtype=s_dtype)
        grd_traced_places_traits[0] = df_places["Trait"].values
        grd_traced_agents_traits[0] = df_agents["Trait"].values
        grd_traced_agents_x[0] = df_agents["x"].values

    # ------------------------------------------------------------------------------------------
    # return variables
    if b_return:
        df_agents_copy = df_agents.copy()
        vct_agents_origin_x = df_agents_copy["x"].values

    # ------------------------------------------------------------------------------------------
    # allocate memory variables
    dct_memory = dict()
    for a in range(n_agents):
        n_memory = df_agents["M"].values[a]
        n_trait = df_agents["Trait"].values[a]
        dct_memory[str(df_agents["Id"].values[a])] = n_trait * np.ones(n_memory)

    # ------------------------------------------------------------------------------------------
    # main simulation loop
    for t in range(1, n_steps):
        if b_tui:
            backend.status(
                "CUE1d :: simulation step {} [{:.2f}%]".format(t, 100 * t / n_steps)
            )
        # --------------------------------------------------------------------------------------
        # agents movements
        for a in range(n_agents):
            # ----------------------------------------------------------------------------------
            # get agent variables
            a_id = df_agents["Id"].values[a]
            vct_a_memory = dct_memory[str(a_id)]  # get memory
            a_trait = np.mean(vct_a_memory) # mean over memory
            a_x = df_agents["x"].values[a]

            # ----------------------------------------------------------------------------------
            # get agent parameters
            a_deltac = df_agents["D"].values[a]
            a_rc = df_agents["R"].values[a]
            a_ca = df_agents["C"].values[a]

            # ----------------------------------------------------------------------------------
            # get current window objects
            vct_rows_base_ids = dct_window[str(a_rc)]["ids"]
            df_window = dct_window[str(a_rc)]["df"]

            # ----------------------------------------------------------------------------------
            # update window dataframe
            df_window["x"] = (a_x + vct_rows_base_ids) % n_places # here the magic happens
            df_window["Trait"] = df_places["Trait"].values[df_window["x"].values]
            df_window["C"] = df_places["C"].values[df_window["x"].values]
            df_window["Discr"] = np.abs(a_trait - df_window["Trait"].values)

            # ----------------------------------------------------------------------------------
            # get sampling probability
            if s_weight.lower() == 'uniform':
                # uniform interaction prob
                df_window["Prob"] = 1 / a_deltac
            elif s_weight.lower() == 'linear':
                # linear interaction score
                df_window["Prob"] = linear_prob(
                    x=df_window['Discr'].values,
                    x_max=a_deltac
                )
            else:
                # uniform interaction prob
                df_window["Prob"] = 1 / a_deltac

            # ----------------------------------------------------------------------------------
            # apply cutoff criterion
            df_window["Prob"] = df_window["Prob"].values * (df_window['Discr'].values <= a_deltac)
            if df_window["Prob"].sum() == 0:
                # go uniform
                df_window["Prob"] = 1 / len(df_window)
            # normalize
            df_window["Prob"] = df_window["Prob"].values / df_window["Prob"].sum()

            # ----------------------------------------------------------------------------------
            # move agent
            np.random.seed(grd_seeds[t, a])  # restart random state
            # weighted random sampling
            n_next_index = np.random.choice(
                a=df_window.index,
                size=1,
                p=df_window["Prob"].values
            )[0] # get the first

            # ----------------------------------------------------------------------------------
            # update agent position
            df_agents["x"].values[a] = df_window["x"].values[n_next_index]

            # ----------------------------------------------------------------------------------
            # apply interaction criteria
            if df_window["Prob"].values[n_next_index] > 0:
                # ------------------------------------------------------------------------------
                # get space parameters from window dataframe
                n_crt_place_trait = df_window["Trait"].values[n_next_index]
                n_crt_place_x = df_window["x"].values[n_next_index]
                n_crt_place_d = df_window["C"].values[n_next_index]

                # ------------------------------------------------------------------------------
                # compute means
                r_mean_agent = (a_trait + (a_ca * n_crt_place_trait)) / (1 + a_ca)
                r_mean_place = (n_crt_place_trait + (n_crt_place_d * a_trait)) / (1 + n_crt_place_d)

                # ------------------------------------------------------------------------------
                # replace in simulation dataframes
                df_agents["Trait"].values[a] = r_mean_agent
                df_places["Trait"].values[n_crt_place_x] = r_mean_place

                # ------------------------------------------------------------------------------
                # update memory vector
                for i in range(len(vct_a_memory) - 1, 0, -1):
                    vct_a_memory[i] = vct_a_memory[i - 1]
                vct_a_memory[0] = r_mean_agent
                dct_memory[str(a_id)] = vct_a_memory

        # ----------------------------------------------------------------------------------
        # trace
        if b_trace:
            grd_traced_places_traits[t] = df_places["Trait"].values
            grd_traced_agents_traits[t] = df_agents["Trait"].values
            grd_traced_agents_x[t] = df_agents["x"].values

        # ----------------------------------------------------------------------------------
        # reset x values
        if b_return:
            # reset x
            df_agents["x"] = vct_agents_origin_x

    # ------------------------------------------------------------------------------------------
    # prepare output dict
    dct_output = {"Agents": df_agents, "Places": df_places}

    # ------------------------------------------------------------------------------------------
    # append extra content
    if b_trace:
        dct_output["Simulation"] = {
            "Places_traits": grd_traced_places_traits,
            "Agents_traits": grd_traced_agents_traits,
            "Agents_x": grd_traced_agents_x,
        }
    return dct_output
