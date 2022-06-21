'''

Visuals routines source code

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
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def plot_sigle_frame(grd,
                     cmap='Greys',
                     folder='C:/bin',
                     fname='frame',
                     suff='',
                     ttl='',
                     show=False,
                     dark=True,
                     dpi=100):
    if dark:
        plt.style.use('dark_background')
    fig = plt.figure(figsize=(4, 4))  # Width, Height
    plt.suptitle(ttl)
    plt.imshow(grd, cmap=cmap)
    plt.axis('off')
    if show:
        plt.show()
        plt.close(fig)
    else:
        # export file
        if suff == '':
            filepath = folder + '/' + fname + '.png'
        else:
            filepath = folder + '/' + fname + '_' + suff + '.png'
        plt.savefig(filepath, dpi=dpi)
        plt.close(fig)
        return filepath


def plot_cue_1d_pannel(step, n_types, n_places, n_agents, places_types_t, agents_types_t, agents_i_t,
                       cmap='viridis', folder='C:/bin', fname='frame',
                       suff='',
                       ttl='',
                       show=True,
                       dark=True,
                       dpi=100):
    if dark:
        plt.style.use('dark_background')

    if step < n_places:
        grd_lcl_spaces = places_types_t[:, : step + 1]
        vct_lcl_ticks = np.arange(0, step + 1, 5)
        vct_lcl_labels = vct_lcl_ticks
    else:
        grd_lcl_spaces = places_types_t[:, step - n_places: step + 1]
        vct_lcl_ticks = np.arange(0, n_places + 1, 5)
        vct_lcl_labels = vct_lcl_ticks + (step - n_places)

    fig = plt.figure(figsize=(10, 5))  # Width, Height
    gs = mpl.gridspec.GridSpec(2, 4, wspace=0.0, hspace=0.5, left=0.05, bottom=0.1, top=0.9, right=0.95)  # nrows, ncols
    plt.suptitle(ttl)
    #
    # space map
    ax = fig.add_subplot(gs[:, :2])
    im = plt.imshow(grd_lcl_spaces, cmap=cmap, vmin=0, vmax=n_types)
    plt.colorbar(im, shrink=0.4)
    plt.title('places and agents')
    plt.xticks(ticks=vct_lcl_ticks, labels=vct_lcl_labels)
    plt.ylabel('position')
    plt.xlabel('time step')

    for a in range(len(agents_i_t)):
        if step < n_places:
            vct_lcl_agents_i = agents_i_t[a][: step + 1]
            vct_lcl_agents_types = agents_types_t[a][:step + 1]
        else:
            vct_lcl_agents_i = agents_i_t[a][step - n_places:step + 1]
            vct_lcl_agents_types = agents_types_t[a][step - n_places:step + 1]
        plt.plot(vct_lcl_agents_i, 'white', zorder=1)

    for a in range(len(agents_i_t)):
        if step < n_places:
            vct_lcl_agents_i = agents_i_t[a][: step + 1]
            vct_lcl_agents_types = agents_types_t[a][:step + 1]
        else:
            vct_lcl_agents_i = agents_i_t[a][step - n_places:step + 1]
            vct_lcl_agents_types = agents_types_t[a][step - n_places:step + 1]
        plt.scatter(np.arange(len(vct_lcl_agents_i)),
                    vct_lcl_agents_i,
                    c=vct_lcl_agents_types,
                    edgecolors='white',
                    marker='o',
                    cmap=cmap,
                    vmin=0,
                    vmax=n_types,
                    zorder=2)

    #
    # space hist
    ax = fig.add_subplot(gs[0, 3])
    plt.title('Places histogram')
    plt.hist(x=places_types_t.transpose()[step], bins=10, range=(0, n_types), color='tab:grey')
    plt.ylim(0, n_places)
    plt.xlim(0, n_types)
    plt.ylabel('count')
    plt.xlabel('types')
    #
    # agents hist
    ax = fig.add_subplot(gs[1, 3])
    plt.title('Agents histogram')
    plt.hist(x=agents_types_t.transpose()[step], bins=10, range=(0, n_types), color='tab:grey')
    plt.ylim(0, n_agents)
    plt.xlim(0, n_types)
    plt.ylabel('count')
    plt.xlabel('types')
    if show:
        plt.show()
        plt.close(fig)
    else:
        # export file
        if suff == '':
            filepath = folder + '/' + fname + '.png'
        else:
            filepath = folder + '/' + fname + '_' + suff + '.png'
        plt.savefig(filepath, dpi=dpi)
        plt.close(fig)
        return filepath
