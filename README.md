# Agent-based Modelling - Cooperation in Urban Environments (CUE) 

This repository includes:
- [x] All files required to run `abm-cue` models;
- [x] A directory called `./samples` with examples of input files and datasets;
- [x] A directory called `./docs` with some documentation files;
- [x] A directory called `./gui` with some graphical user interface files;
- [x] The User Guide file: [`guide.md`](https://github.com/ipo-exe/abm-cue/blob/main/docs/guide.md)
- [x] The installation tutorial for Windows file: [`install_windows.md`](https://github.com/ipo-exe/abm-cue/blob/main/docs/install_windows.md)
- [x] The Input/Output documentation file: [`iodocs.md`](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md);

## Quick intro to the model
> **Note**: see the [User Guide](https://github.com/ipo-exe/abm-cue/blob/main/docs/guide.md)

1) Agents walk randomly around a ring-like 1-D world of places;
2) Agents and places have orientation traits;
3) Agents have a _bias_ to go to places like themselves;
4) Agents have a limited window of sight to the nearest places to go;
5) Agents interact with places only if they are related enough;
7) During interaction, agents influence the place orientation trait to a certain extent, and vice-versa.

The result is an evolving urban environment in 1-D world:

![intro](https://github.com/ipo-exe/abm-cue/blob/main/figs/intro1d.gif "intro")

Or in 2-D world:

![intro](https://github.com/ipo-exe/abm-cue/blob/main/figs/intro2d.gif "intro2")

Topology features of simulations may be assessed via integration with GIS applications:

![intro](https://github.com/ipo-exe/abm-cue/blob/main/figs/fig_output_network.PNG "intro3")

Large batch processing may be used for in-depth insights with sensitivity analysis:

![intro](https://github.com/ipo-exe/abm-cue/blob/main/figs/fig_output_batch.PNG "intro4")


## Installing and Running CUE on a local machine

> **Note**: see the [installation tutorial for Windows](https://github.com/ipo-exe/abm-cue/blob/main/docs/install_windows.md)

For Windows, Mac and Linux, follow these generic steps:

1) Install `python 3`;
2) Install the following Python dependencies:
   * `numpy`;
   * `scipy`;
   * `pandas`;
   * `matplotlib`;
   * `imageio`.
3) Clone the [latest release of this repository](https://github.com/ipo-exe/abm-cue/releases) (download the asset zip folder);
4) Extract the files to a folder of preference (ex: `C:\Users\Home\Documents\abm-cue-main`);
> **Warning**: do not change internal folder and file names.
6) Execute the `app_cue1d.py` file for the CUE 1-D model or the `app_cue2d.py` file for the CUE 2-D model.


