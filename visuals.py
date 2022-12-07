"""

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

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def plot_sigle_frame(
    grd,
    s_cmap="Greys",
    s_dir_out="C:/bin",
    s_file_name="frame",
    s_suff="",
    s_ttl="",
    b_show=False,
    b_dark=True,
    n_dpi=100,
):
    """
    Plot single grid frame
    :param grd: 2d numpy array of current grid
    :param s_cmap: string cmap code
    :param s_dir_out: string output folder
    :param s_file_name: string file name
    :param s_suff: string suffix
    :param s_ttl: string title
    :param b_show: boolean to show
    :param b_dark: boolean to dark mode
    :param n_dpi: int dpi resolution
    :return: string file name
    """
    if b_dark:
        plt.style.use("dark_background")
    fig = plt.figure(figsize=(4, 4))  # Width, Height
    plt.suptitle(s_ttl)
    plt.imshow(grd, cmap=s_cmap)
    plt.axis("off")
    if b_show:
        plt.show()
        plt.close(fig)
    else:
        # export file
        if s_suff == "":
            filepath = s_dir_out + "/" + s_file_name + ".png"
        else:
            filepath = s_dir_out + "/" + s_file_name + "_" + s_suff + ".png"
        plt.savefig(filepath, dpi=n_dpi)
        plt.close(fig)
        del fig
        return filepath


def plot_traced_h(
    df_data,
    s_field='H',
    s_dir_out="C:/bin",
    s_file_name="frame",
    s_suff="",
    s_ttl="",
    b_show=False,
    b_dark=False,
    n_dpi=100,
):
    """
    plot time series of H
    :param df_data: pandas dataframe of time series (Step field required)
    :param s_field: string field of H
    :param s_dir_out: string output folder
    :param s_file_name: string file name
    :param s_suff: string suffix
    :param s_ttl: string title
    :param b_show: boolean to show fig
    :param b_dark: boolean to dark mode
    :param n_dpi: int dpi resolution
    :return: string filepath
    """
    if b_dark:
        plt.style.use("dark_background")
    fig = plt.figure(figsize=(8, 4))  # Width, Height
    plt.title(s_ttl)
    plt.plot(df_data["Step"], df_data[s_field], c='tab:grey')
    plt.ylabel("H")
    plt.xlabel("Steps")
    plt.xlim(0, df_data["Step"].max() + 1)
    if 1.1 * df_data[s_field].max() == 0:
        pass
    else:
        plt.ylim(0, 1.1 * df_data[s_field].max())
    if b_show:
        plt.show()
        plt.close(fig)
    else:
        # export file
        if s_suff == "":
            filepath = s_dir_out + "/" + s_file_name + ".png"
        else:
            filepath = s_dir_out + "/" + s_file_name + "_" + s_suff + ".png"
        plt.savefig(filepath, dpi=n_dpi)
        plt.close(fig)
        return filepath


def plot_traced_traits(
    df_data,
    df_params,
    n_traits,
    s_dir_out="C:/bin",
    s_file_name="frame",
    s_suff="",
    s_ttl="",
    b_show=False,
    b_dark=False,
    n_dpi=100,
):
    """
    plot time series of traits
    :param df_data: pandas dataframe of time series (Step field required)
    :param df_params: pandas dataframe of parameters (agents or places)
    :param n_traits: int max number of places
    :param s_dir_out: string output folder
    :param s_file_name: string file name
    :param s_suff: string suffix
    :param s_ttl: string title
    :param b_show: boolean to show fig
    :param b_dark: boolean to dark mode
    :param n_dpi: int dpi resolution
    :return: string filepath
    """
    if b_dark:
        plt.style.use("dark_background")
    fig = plt.figure(figsize=(8, 4))  # Width, Height
    plt.title(s_ttl)
    s_old_alias = ''
    for i in range(len(df_data.columns)):
        s_lcl_col = df_data.columns[i]
        if 'Trait' in s_lcl_col:
            # get alias
            s_lcl_alias = s_lcl_col.split("_")[0]
            if s_lcl_alias != s_old_alias:
                b_label = True
            else:
                b_label = False
            s_old_alias = s_lcl_alias
            # get id
            s_lcl_id = s_lcl_col.split("_")[1]
            # get color
            s_lcl_color = df_params.query("Id == {}".format(s_lcl_id))["Color"].values[0]
            if b_label:
                plt.plot(df_data["Step"], df_data[s_lcl_col], c=s_lcl_color, label=s_lcl_alias)
            else:
                plt.plot(df_data["Step"], df_data[s_lcl_col], c=s_lcl_color)
            plt.legend()
            plt.ylabel("Traits")
            plt.xlabel("Steps")
            plt.xlim(0, df_data["Step"].max() + 1)
            plt.ylim(0, n_traits + 1)
    if b_show:
        plt.show()
        plt.close(fig)
        del fig
    else:
        # export file
        if s_suff == "":
            filepath = s_dir_out + "/" + s_file_name + ".png"
        else:
            filepath = s_dir_out + "/" + s_file_name + "_" + s_suff + ".png"
        plt.savefig(filepath, dpi=n_dpi)
        plt.close(fig)
        del fig
        return filepath


def plot_traced_positions(
    df_data,
    df_params,
    n_positions,
    s_dir_out="C:/bin",
    s_file_name="frame",
    s_suff="",
    s_ttl="",
    s_position="x",
    b_show=False,
    b_dark=False,
    n_dpi=100,
):
    """
    plot time series of positions
    :param df_data: pandas dataframe of time series (Step field required)
    :param df_params: pandas dataframe of parameters (agents or places)
    :param n_positions: int max number of places
    :param s_dir_out: string output folder
    :param s_file_name: string file name
    :param s_suff: string suffix
    :param s_ttl: string title
    :param b_show: boolean to show fig
    :param b_dark: boolean to dark mode
    :param n_dpi: int dpi resolution
    :return:
    """
    if b_dark:
        plt.style.use("dark_background")
    fig = plt.figure(figsize=(8, 4))  # Width, Height
    plt.title(s_ttl)
    s_old_alias = ''
    for i in range(len(df_data.columns)):
        s_lcl_col = df_data.columns[i]
        if 'x' in s_lcl_col or 'y' in s_lcl_col:
            # get alias
            s_lcl_alias = s_lcl_col.split("_")[0]
            if s_lcl_alias != s_old_alias:
                b_label = True
            else:
                b_label = False
            s_old_alias = s_lcl_alias
            # get id
            s_lcl_id = s_lcl_col.split("_")[1]
            # get color
            s_lcl_color = df_params.query("Id == {}".format(s_lcl_id))["Color"].values[0]
            if b_label:
                plt.plot(df_data["Step"], df_data[s_lcl_col], c=s_lcl_color, label=s_lcl_alias)
            else:
                plt.plot(df_data["Step"], df_data[s_lcl_col], c=s_lcl_color)
            plt.legend()
            plt.ylabel(s_position)
            plt.xlabel("Steps")
            plt.xlim(0, df_data["Step"].max() + 1)
            plt.ylim(0, n_positions + 1)

    if b_show:
        plt.show()
        plt.close(fig)
    else:
        # export file
        if s_suff == "":
            filepath = s_dir_out + "/" + s_file_name + ".png"
        else:
            filepath = s_dir_out + "/" + s_file_name + "_" + s_suff + ".png"
        plt.savefig(filepath, dpi=n_dpi)
        plt.close(fig)
        return filepath


def plot_trait_histogram(
    df_data,
    n_traits,
    n_bins=10,
    s_dir_out="C:/bin",
    s_file_name="hist",
    s_suff="",
    s_ttl="",
    b_show=True,
    b_dark=False,
    n_dpi=100,
):
    """
    plot histogram
    :param df_data: pandas dataframe
    :param n_traits: int number of traits
    :param n_bins: int number of hist bins
    :param s_dir_out: string output directory
    :param s_file_name: string filename
    :param s_suff: string suffix
    :param s_ttl: string title
    :param b_show: boolean to show
    :param b_dark: boolean to dark mode
    :param n_dpi: int dpi resolution
    :return: string file path
    """
    if b_dark:
        plt.style.use("dark_background")
    fig = plt.figure(figsize=(8, 4))  # Width, Height
    plt.title(s_ttl)
    plt.hist(
        x=df_data["Trait"].values, bins=n_bins, range=(0, n_traits), color="tab:grey"
    )
    plt.ylim(0, len(df_data))
    plt.xlim(0, n_traits)
    plt.ylabel("count")
    plt.xlabel("traits")
    if b_show:
        plt.show()
        plt.close(fig)
    else:
        # export file
        if s_suff == "":
            filepath = s_dir_out + "/" + s_file_name + ".png"
        else:
            filepath = s_dir_out + "/" + s_file_name + "_" + s_suff + ".png"
        plt.savefig(filepath, dpi=n_dpi)
        plt.close(fig)
        return filepath


def plot_cue_1d_pannel(
    n_step,
    n_traits,
    n_places,
    n_agents,
    grd_places_traits_t,
    grd_agents_traits_t,
    grd_agents_x_t,
    s_cmap="viridis",
    s_dir_out="C:/bin",
    s_file_name="frame",
    s_suff="",
    s_ttl="",
    b_show=True,
    b_dark=False,
    n_dpi=100,
):
    """
    pannel of 1d CUE model
    :param n_step: int step
    :param n_traits: int traits
    :param n_places: int places
    :param n_agents: int agents
    :param grd_places_traits_t: 2d numpy array places traits transposed grid
    :param grd_agents_traits_t: 2d numpy array agents traits transposed grid
    :param grd_agents_x_t: 2d numpy array places position transposed grid
    :param s_cmap: string cmap code
    :param s_dir_out: string output folder
    :param s_file_name: string file name
    :param s_suff: string suffix
    :param s_ttl: string title
    :param b_show: boolean to show
    :param b_dark: boolean to dark mode
    :param n_dpi: int dpi resolution
    :return: string file name
    """
    if b_dark:
        plt.style.use("dark_background")

    if n_step < n_places:
        grd_lcl_spaces = grd_places_traits_t[:, : n_step + 1]
        vct_lcl_ticks = np.arange(0, n_step + 1, 5)
        vct_lcl_labels = vct_lcl_ticks
    else:
        grd_lcl_spaces = grd_places_traits_t[:, n_step - n_places : n_step + 1]
        vct_lcl_ticks = np.arange(0, n_places + 1, 5)
        vct_lcl_labels = vct_lcl_ticks + (n_step - n_places)

    fig = plt.figure(figsize=(6, 4))  # Width, Height
    gs = mpl.gridspec.GridSpec(
        2, 4, wspace=0.0, hspace=0.8, left=0.1, bottom=0.2, top=0.8, right=0.9
    )  # nrows, ncols
    plt.suptitle(s_ttl)
    #
    # space map
    ax = fig.add_subplot(gs[:, :2])
    im = plt.imshow(grd_lcl_spaces, cmap=s_cmap, vmin=0, vmax=n_traits)
    plt.colorbar(im, shrink=0.4)
    plt.title("places and agents")
    plt.xticks(ticks=vct_lcl_ticks, labels=vct_lcl_labels)
    plt.ylabel("position")
    plt.xlabel("time step")
    for a in range(len(grd_agents_x_t)):
        if n_step < n_places:
            vct_lcl_agents_i = grd_agents_x_t[a][: n_step + 1]
            vct_lcl_agents_types = grd_agents_traits_t[a][: n_step + 1]
        else:
            vct_lcl_agents_i = grd_agents_x_t[a][n_step - n_places : n_step + 1]
            vct_lcl_agents_types = grd_agents_traits_t[a][
                n_step - n_places : n_step + 1
            ]
        plt.plot(vct_lcl_agents_i, "white", zorder=1)
    for a in range(len(grd_agents_x_t)):
        if n_step < n_places:
            vct_lcl_agents_i = grd_agents_x_t[a][: n_step + 1]
            vct_lcl_agents_types = grd_agents_traits_t[a][: n_step + 1]
        else:
            vct_lcl_agents_i = grd_agents_x_t[a][n_step - n_places : n_step + 1]
            vct_lcl_agents_types = grd_agents_traits_t[a][
                n_step - n_places : n_step + 1
            ]
        plt.scatter(
            np.arange(len(vct_lcl_agents_i)),
            vct_lcl_agents_i,
            c=vct_lcl_agents_types,
            edgecolors="white",
            marker="o",
            cmap=s_cmap,
            vmin=0,
            vmax=n_traits,
            zorder=2,
        )

    #
    # space hist
    ax = fig.add_subplot(gs[0, 3])
    plt.title("Places histogram")
    plt.hist(
        x=grd_places_traits_t.transpose()[n_step],
        bins=n_traits,
        range=(0, n_traits),
        color="tab:grey",
    )
    plt.ylim(0, n_places)
    plt.xlim(0, n_traits)
    plt.ylabel("count")
    plt.xlabel("traits")
    #
    # agents hist
    ax = fig.add_subplot(gs[1, 3])
    plt.title("Agents histogram")
    plt.hist(
        x=grd_agents_traits_t.transpose()[n_step],
        bins=n_traits,
        range=(0, n_traits),
        color="tab:grey",
    )
    plt.ylim(0, n_agents)
    plt.xlim(0, n_traits)
    plt.ylabel("count")
    plt.xlabel("traits")
    if b_show:
        plt.show()
        plt.close(fig)
        del fig
    else:
        # export file
        if s_suff == "":
            filepath = s_dir_out + "/" + s_file_name + ".png"
        else:
            filepath = s_dir_out + "/" + s_file_name + "_" + s_suff + ".png"
        plt.savefig(filepath, dpi=n_dpi)
        plt.close(fig)
        del fig
        return filepath


def plot_cue_2d_pannel(
    grd_traits,
    n_step,
    n_traits,
    n_agents,
    n_places,
    vct_places_traits,
    vct_agents_traits,
    vct_agents_x,
    vct_agents_y,
    s_cmap="viridis",
    s_dir_out="C:/bin",
    s_file_name="frame",
    s_suff="",
    s_ttl="",
    b_show=True,
    b_dark=False,
    n_dpi=100,
):
    """
    pannel of 1d CUE model
    :param n_step: int step
    :param n_traits: int traits
    :param n_places: int places
    :param n_agents: int agents
    :param grd_places_traits_t: 2d numpy array places traits transposed grid
    :param grd_agents_traits_t: 2d numpy array agents traits transposed grid
    :param grd_agents_x_t: 2d numpy array places position transposed grid
    :param s_cmap: string cmap code
    :param s_dir_out: string output folder
    :param s_file_name: string file name
    :param s_suff: string suffix
    :param s_ttl: string title
    :param b_show: boolean to show
    :param b_dark: boolean to dark mode
    :param n_dpi: int dpi resolution
    :return: string file name
    """
    if b_dark:
        plt.style.use("dark_background")

    fig = plt.figure(figsize=(6, 4))  # Width, Height
    gs = mpl.gridspec.GridSpec(
        2, 4, wspace=0.0, hspace=0.8, left=0.1, bottom=0.2, top=0.8, right=0.9
    )  # nrows, ncols
    plt.suptitle(s_ttl)
    #
    # space map
    ax = fig.add_subplot(gs[:, :2])
    im = plt.imshow(grd_traits, cmap=s_cmap, vmin=0, vmax=n_traits, origin="lower")
    plt.colorbar(im, shrink=0.4)
    plt.title("places and agents")
    plt.ylabel("y")
    plt.xlabel("x")

    plt.scatter(
        vct_agents_x,
        vct_agents_y,
        c=vct_agents_traits,
        edgecolors="white",
        marker="o",
        cmap=s_cmap,
        vmin=0,
        vmax=n_traits,
        zorder=2,
    )

    #
    # space hist
    ax = fig.add_subplot(gs[0, 3])
    plt.title("Places histogram")
    plt.hist(
        x=vct_places_traits,
        bins=n_traits,
        range=(0, n_traits),
        color="tab:grey",
    )
    plt.ylim(0, n_places)
    plt.xlim(0, n_traits)
    plt.ylabel("count")
    plt.xlabel("traits")
    #
    # agents hist
    ax = fig.add_subplot(gs[1, 3])
    plt.title("Agents histogram")
    plt.hist(
        x=vct_agents_traits,
        bins=n_traits,
        range=(0, n_traits),
        color="tab:grey",
    )
    plt.ylim(0, n_agents)
    plt.xlim(0, n_traits)
    plt.ylabel("count")
    plt.xlabel("traits")
    if b_show:
        plt.show()
        plt.close(fig)
        del fig
    else:
        # export file
        if s_suff == "":
            filepath = s_dir_out + "/" + s_file_name + ".png"
        else:
            filepath = s_dir_out + "/" + s_file_name + "_" + s_suff + ".png"
        plt.savefig(filepath, dpi=n_dpi)
        plt.close(fig)
        del fig
        return filepath

