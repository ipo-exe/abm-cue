'''

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

'''
import cue1d
import inp, backend
from backend import status
import pandas as pd


def run_cue1d(fsim):
    # import param_simulation.txt
    dct_fsim = inp.import_data_table(s_table_name='param_simulation', s_filepath=fsim)
    df_param_sim = dct_fsim['df']
    # update timestamp value
    df_param_sim.loc[df_param_sim['Metadata'] == 'Timestamp', 'Value'] = backend.timestamp_log()
    print(df_param_sim.to_string())
    # get run folder
    s_workplace = df_param_sim.loc[df_param_sim['Metadata'] == 'Run Folder', 'Value'].values[0].strip()
    s_dir_out = backend.create_rundir(label='CUE1d', wkplc=s_workplace)

    # get places file
    f_places = df_param_sim.loc[df_param_sim['Metadata'] == 'Places File', 'Value'].values[0].strip()
    # get agents file
    f_agents = df_param_sim.loc[df_param_sim['Metadata'] == 'Agents File', 'Value'].values[0].strip()

    # get n steps
    n_steps = int(df_param_sim.loc[df_param_sim['Metadata'] == 'Steps', 'Value'].values[0].strip())

    # import places file
    dct_places = inp.import_data_table(s_table_name='param_places', s_filepath=f_places)
    df_places = dct_places['df']
    print(df_places.to_string())
    # import agents file
    dct_agents = inp.import_data_table(s_table_name='param_agents', s_filepath=f_agents)
    df_agents = dct_agents['df']
    print(df_agents.to_string())

    b_trace = True

    dct_out = cue1d.play(df_agents=df_agents.copy(),
                         df_places=df_places.copy(),
                         n_steps=n_steps,
                         b_return=True,
                         b_trace=b_trace)

    if b_trace:
        import os
        from visuals import plot_cue_1d_pannel
        from out import export_gif

        n_agents = len(df_agents)
        n_places = len(df_places)
        n_traits = max([df_agents['Trait'].max(), df_places['Trait'].max()])
        dir_frames = '{}/frames'.format(s_dir_out)
        os.mkdir(path=dir_frames)
        # todo export simulation data

        # plot stuff
        status('plotting outputs', process=True)

        s_cmap = 'viridis'  # 'tab20c'
        grd_traced_places_traits_t = dct_out['Simulation']['Places_traits'].transpose()
        grd_traced_agents_x_t = dct_out['Simulation']['Agents_x'].transpose()
        grd_traced_agents_traits_t = dct_out['Simulation']['Agents_traits'].transpose()

        for t in range(n_steps - 1):
            status('plot {}'.format(t))
            plot_cue_1d_pannel(step=t,
                               n_traits=n_traits,
                               n_places=n_places,
                               n_agents=n_agents,
                               places_traits_t=grd_traced_places_traits_t,
                               agents_traits_t=grd_traced_agents_traits_t,
                               agents_x_t=grd_traced_agents_x_t,
                               ttl='Step = {}'.format(t),
                               folder=dir_frames,
                               fname='frame_{}'.format(str(t).zfill(4)),
                               show=False,
                               dark=False)

        export_gif(dir_output=s_dir_out, dir_images=dir_frames, nm_gif='animation', kind='png', suf='')


fsim = './samples/param_simulation.txt'
run_cue1d(fsim=fsim)