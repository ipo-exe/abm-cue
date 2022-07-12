# Agent-based Modelling - Coorperation of Urban Environments (CUE) 

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
2) Agents and places have orientation types;
3) Agents have a _bias_ to go to places like themselves;
4) Agents have a limited window of sight to the nearest places to go;
5) Agents interact with places only if they are related enough;
7) During interaction, agents influence the place orientation type to a certain extent, and vice-versa.

The result is an evolving urban environment:

![intro](https://github.com/ipo-exe/abm-cue/blob/main/figs/intro.gif "intro")

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
6) Execute the `app_cue1d.py` file for the CUE 1-d model.


