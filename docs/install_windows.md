# Installation guide for Windows users

Here is a nice installation tutorial for Windows users. 
> **Tip**: read _all_ the steps _before_ executing them! You may anticipate some issues.

## 1) **Download Python**
Go to https://www.python.org/ and download the latest version of `python 3`;
> Unless you have good reasons to keep it, we encourage you to first 
> _uninstall_ older Python versions to prevent problems.  

## 2) **Install Python**
Double-click the installation file to launch the **installation wizard**. Then enable the option:

> [x] Add Python 3.# to PATH
> 
> Example:
> 
> ![addpath](https://github.com/ipo-exe/abm-cue/blob/main/docs/figs/add_to_path.png "add")

Click `Install Now` and follow through the installation steps in the wizard:

> ![install](https://github.com/ipo-exe/abm-cue/blob/main/docs/figs/install.png "install")

## 3) Install the required dependencies
Here the easiest way is to open the Windows `Command Prompt` program and 
type some installation commands in sequence. 
> If you are already using Python, you may want to upgrade `pip` (the package manager) 
> to the latest version by typing:
```commandline
python -m pip install --upgrade pip
```

The installation command is the same but changes in the name of the dependency. So the `numpy` installation command will look like this: 
```commandline
python -m pip install numpy
```
Then `scipy` installation:
```commandline
python -m pip install scipy
```
Then `pandas` installation:
```commandline
python -m pip install pandas
```
Then `matplotlib` installation:
```commandline
python -m pip install matplotlib
```
Then `imageio` installation:
```commandline
python -m pip install imageio
```
> The sequence would look like this:
> 
> ![pip1](https://github.com/ipo-exe/abm-cue/blob/main/docs/figs/pip_install_1.PNG "pip1")
> 
> And this:
> ![pip2](https://github.com/ipo-exe/abm-cue/blob/main/docs/figs/pip_install_2.PNG "pip2")

