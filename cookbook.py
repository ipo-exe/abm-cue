'''

Cookbook scripts source code

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

'''
import os
import numpy as np
import pandas as pd
from backend import create_rundir, status
from out import export_gif


def cue_1d_recipe():
    import cue1d
    from visuals import plot_cue_1d_pannel

    # workplace
    wkpl = '/home/ipora/Documents/bin'
    dir_out = create_rundir(label='CUE1D', wkplc=wkpl)
    dir_frames = '{}/frames'.format(dir_out)
    os.mkdir(dir_frames)

    # >>> simulation parameters dataframe (import from csv file)
    df_sim_params = pd.read_csv('./datasets/sim_params.txt', sep=';')
    df_sim_params.columns = df_sim_params.columns.str.strip()
    df_sim_params['Parameter'] = df_sim_params['Parameter'].str.strip()
    print(df_sim_params.to_string())
    # >>> retrieve model parameters from dataframe to local variables:
    status('retrieving simulation parameters')
    # number of agents:
    n_agents = int(df_sim_params[df_sim_params['Parameter'] == 'N_Agents']['Set'].values[0])

    # number of public places:
    n_places = int(df_sim_params[df_sim_params['Parameter'] == 'N_Places']['Set'].values[0])

    # number of types of actions:
    n_types = int(df_sim_params[df_sim_params['Parameter'] == 'N_Types']['Set'].values[0])

    # orientation threshold for interaction:
    n_alpha = int(n_types * df_sim_params[df_sim_params['Parameter'] == 'Alpha']['Set'].values[0])
    print(n_alpha)

    # distance threshold for interaction:
    n_beta = int(df_sim_params[df_sim_params['Parameter'] == 'Beta']['Set'].values[0])

    # number of time steps:
    n_steps = int(df_sim_params[df_sim_params['Parameter'] == 'N_Steps']['Set'].values[0])

    # degree of influence of spaces to agentes
    r_c_places = df_sim_params[df_sim_params['Parameter'] == 'C']['Set'].values[0]

    # degree of influence of spaces to agentes
    r_d_agents = df_sim_params[df_sim_params['Parameter'] == 'D']['Set'].values[0]


    s_dtype = 'float32'
    # >>> set simulation initial conditions:
    status('getting simulation initial conditions')
    b_random = False
    if b_random:
        from backend import get_seed
        # set random state:
        np.random.seed(get_seed())
        # set uniform random distribution
        vct_agents_types = np.round(n_types * np.random.random(size=n_agents), 0)
        vct_agents_i = np.random.randint(low=0, high=n_places, size=n_agents, dtype='uint16')
        vct_places_types = np.round(n_types * np.random.random(size=n_places), 0)
        vct_places_types[: 10] = 5
        vct_places_types[10: 20] = 15
        vct_places_types[20: 30] = 10
        vct_places_types[30:] = 19
    else:
        print('import from file')  # todo import from file
        vct_agents_types = np.ones(shape=n_agents, dtype=s_dtype)
        vct_agents_types[0] = 18
        #vct_agents_types[1] = 1
        vct_agents_i = np.ones(shape=n_agents, dtype='uint16')  # np.random.randint(low=0, high=n_spaces, size=n_agents, dtype='uint16')
        vct_agents_i[0] = 20
        #vct_agents_i[1] = 19
        vct_places_types = 2 * np.ones(shape=n_places, dtype=s_dtype)


    # deploy simulation dataframes
    df_agents = pd.DataFrame({'Agent_type': vct_agents_types, 'Agent_i': vct_agents_i})
    print(df_agents.to_string())
    df_places = pd.DataFrame({'Place_type': vct_places_types, 'Place_i': np.arange(0, n_places)})
    print(df_places.to_string())

    status('running cue 1d model')
    b_trace = True
    dct_out = cue1d.play(df_agents=df_agents,
                         df_places=df_places,
                         n_steps=n_steps,
                         r_d_agents=r_d_agents,
                         r_c_places=r_c_places,
                         n_beta=n_beta,
                         n_alpha=n_alpha,
                         b_trace=b_trace)

    if b_trace:
        # todo export simulation data

        # plot stuff
        status('plotting outputs', process=True)

        s_cmap = 'viridis'  # 'tab20c'
        grd_traced_places_types_t = dct_out['Simulation']['Places_types'].transpose()
        grd_traced_agents_i_t = dct_out['Simulation']['Agents_i'].transpose()
        grd_traced_agents_types_t = dct_out['Simulation']['Agents_types'].transpose()

        for t in range(n_steps - 1):
            #print('plot {}'.format(t))
            plot_cue_1d_pannel(step=t,
                               n_types=n_types,
                               n_places=n_places,
                               n_agents=n_agents,
                               places_types_t=grd_traced_places_types_t,
                               agents_types_t=grd_traced_agents_types_t,
                               agents_i_t=grd_traced_agents_i_t,
                               ttl='Step = {}'.format(t),
                               folder=dir_frames,
                               fname='frame_{}'.format(str(t).zfill(4)),
                               show=False,
                               dark=False)

        export_gif(dir_output=dir_out, dir_images=dir_frames, nm_gif='animation', kind='png', suf='')

cue_1d_recipe()