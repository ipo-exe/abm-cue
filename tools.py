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
import numpy as np


def run_cue1d(fsim):

    # import param_simulation.txt
    dct_fsim = inp.import_data_table(s_table_name='param_simulation', s_filepath=fsim)
    df_param_sim = dct_fsim['df']
    # update timestamp value
    df_param_sim.loc[df_param_sim['Metadata'] == 'Timestamp', 'Value'] = backend.timestamp_log()

    # get run folder
    s_workplace = df_param_sim.loc[df_param_sim['Metadata'] == 'Run Folder', 'Value'].values[0].strip()
    s_dir_out = backend.create_rundir(label='CUE1d', wkplc=s_workplace)

    # get places file
    f_places = df_param_sim.loc[df_param_sim['Metadata'] == 'Places File', 'Value'].values[0].strip()
    # get agents file
    f_agents = df_param_sim.loc[df_param_sim['Metadata'] == 'Agents File', 'Value'].values[0].strip()

    # get simulation parameters
    n_steps = int(df_param_sim.loc[df_param_sim['Metadata'] == 'Steps', 'Value'].values[0].strip())
    s_return = df_param_sim.loc[df_param_sim['Metadata'] == 'Return Agents', 'Value'].values[0].strip()
    s_trace = df_param_sim.loc[df_param_sim['Metadata'] == 'Trace Back', 'Value'].values[0].strip()
    s_plot = df_param_sim.loc[df_param_sim['Metadata'] == 'Plot Results', 'Value'].values[0].strip()
    b_return = False
    b_trace = False
    b_plot = False
    if s_trace == 'True':
        b_trace = True
    if s_return == 'True':
        b_return = True
    if s_plot == 'True':
        b_plot = True

    # import places file
    dct_places = inp.import_data_table(s_table_name='param_places', s_filepath=f_places)
    df_places = dct_places['df']

    df_places['Trait'] = df_places['Trait'].astype('float64')

    # import agents file
    dct_agents = inp.import_data_table(s_table_name='param_agents', s_filepath=f_agents)
    df_agents = dct_agents['df']

    df_agents['Trait'] = df_agents['Trait'].astype('float64')


    # extra params
    n_agents = len(df_agents)
    n_places = len(df_places)
    n_traits = int(max([df_agents['Trait'].max(), df_places['Trait'].max()]))

    # run model
    dct_out = cue1d.play(df_agents=df_agents.copy(),
                         df_places=df_places.copy(),
                         n_steps=n_steps,
                         b_return=b_return,
                         b_trace=b_trace)

    # retrieve outputs
    df_agents_end = dct_out['Agents']
    df_places_end = dct_out['Places']

    # export results
    status('exporting start/end results datasets')
    df_agents.to_csv('{}/param_agents_start.txt'.format(s_dir_out), sep=';', index=False)
    df_agents_end.to_csv('{}/param_agents_end.txt'.format(s_dir_out), sep=';', index=False)
    df_places.to_csv('{}/param_places_start.txt'.format(s_dir_out), sep=';', index=False)
    df_places_end.to_csv('{}/param_places_end.txt'.format(s_dir_out), sep=';', index=False)
    # aux lists
    lst_df = [df_agents, df_agents_end, df_places, df_places_end]
    lst_nms = ['hist_agents_start',
               'hist_agents_end',
               'hist_places_start',
               'hist_places_end']
    lst_ttl = ['Agents Histogram | Start',
               'Agents Histogram | End',
               'Places Histogram | Start',
               'Places Histogram | End',]
    # export histograms
    if b_plot:
        from visuals import plot_trait_histogram
    for i in range(len(lst_df)):
        df_lcl = lst_df[i]
        vct_hist, vct_bins = np.histogram(a=df_lcl['Trait'].values, bins=n_traits, range=(0, n_traits))
        df_hist = pd.DataFrame({'Trait': vct_bins[1:], 'Count': vct_hist})
        df_hist.to_csv('{}/{}.txt'.format(s_dir_out, lst_nms[i]), sep=';', index=False)
        if b_plot:
            plot_trait_histogram(df_data=df_lcl,
                                 n_traits=n_traits,
                                 n_bins=n_traits,
                                 ttl=lst_ttl[i],
                                 folder=s_dir_out,
                                 fname=lst_nms[i],
                                 dpi=100,
                                 show=False)

    if b_trace:
        import os
        from visuals import plot_cue_1d_pannel
        from out import export_gif

        status('exporting traced results datasets')
        grd_traced_places_traits_t = dct_out['Simulation']['Places_traits'].transpose()
        grd_traced_agents_x_t = dct_out['Simulation']['Agents_x'].transpose()
        grd_traced_agents_traits_t = dct_out['Simulation']['Agents_traits'].transpose()

        n_fill = int(np.log10(n_steps)) + 1

        df_traced_agents_x = pd.DataFrame({'Step': np.arange(0, n_steps)})
        df_traced_agents_traits = pd.DataFrame({'Step': np.arange(0, n_steps)})
        for i in range(n_agents):
            s_lcl_agent_x = 'A_{}_x'.format(df_agents['Id'].values[i])
            s_lcl_agent_trait = 'A_{}_trait'.format(df_agents['Id'].values[i])
            df_traced_agents_x[s_lcl_agent_x] = grd_traced_agents_x_t[i]
            df_traced_agents_traits[s_lcl_agent_trait] = grd_traced_agents_traits_t[i]
        df_traced_places_traits = pd.DataFrame({'Step': np.arange(0, n_steps)})
        for i in range(n_places):
            s_lcl_place_trait = 'P_{}_trait'.format(df_places['Id'].values[i])
            df_traced_places_traits[s_lcl_place_trait] = grd_traced_places_traits_t[i]
        df_traced_agents_x.to_csv('{}/traced_agents_x.txt'.format(s_dir_out), sep=';', index=False)
        df_traced_agents_traits.to_csv('{}/traced_agents_traits.txt'.format(s_dir_out), sep=';', index=False)
        df_traced_places_traits.to_csv('{}/traced_places_traits.txt'.format(s_dir_out), sep=';', index=False)

        # plot frames
        if b_plot:
            dir_frames = '{}/frames'.format(s_dir_out)
            os.mkdir(path=dir_frames)
            status('plotting frames', process=True)

            s_cmap = 'viridis'  # 'tab20c'


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
                                   fname='frame_{}'.format(str(t).zfill(n_fill)),
                                   show=False,
                                   dark=False)
            status('generating animation', process=True)
            export_gif(dir_output=s_dir_out, dir_images=dir_frames, nm_gif='animation', kind='png', suf='')
