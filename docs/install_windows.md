# Installation guide for Windows users

Here is a nice installation tutorial for Windows users. 
> **Note**: read _all_ the steps _before_ executing them! You may anticipate some issues.

## 1) **Download Python**
Go to https://www.python.org/ and download the latest version of `Python 3`;
> **Note**: unless you have good reasons to keep it, we encourage you to first 
> _uninstall_ older Python versions to prevent problems.  

## 2) **Install Python**
Double-click the installation file to launch the **installation wizard**. Then enable the option:

> [x] Add `Python 3.x` to PATH (where `x` is the number of version)
> 
> Example:
> 
> ![addpath](https://github.com/ipo-exe/abm-cue/blob/main/figs/install_windows_add_to_path.png "add")

Click `Install Now` and follow through the installation steps in the wizard:

> ![install](https://github.com/ipo-exe/abm-cue/blob/main/figs/install_windows_install.png "install")

## 3) Install the required dependencies
Here the safest way is to open the Windows `Command Prompt` program and 
type some installation commands in sequence. 

If you are already using Python, you may want to upgrade `pip` (the package manager) 
to the latest version by typing:
```commandline
python -m pip install --upgrade pip
```

The installation command is the same except the name of the dependency. So the `numpy` installation command will look like this: 
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

It would look like this:

![pip install](https://github.com/ipo-exe/abm-cue/blob/main/figs/install_windows_pip_install.png "pip")

## 4) Download (clone) the latest release source code

First, open the source code releases repository in your web browser: 
https://github.com/ipo-exe/abm-cue/releases.
Then in the tab `Assets` of the latest release, download the `ZIP` folder of the source code.

After completed download, extract the folder to a location of your preference in your disk. 
Example: `C:/Users/You/Documents/abm-cue-main`

> **Warning**: do not change any files and subfolders from the repository. 

## 5) Execute the application file

The application file for the 1-d CUE model is the `app_cue1d.py` file.  

### 5.1) Executing by double-clicking
The _easiest_ way to execute the app is **double-click the app file**. 
If everything is OK, Windows should launch the Graphical User Interface of the application.

However, things can be _not_ OK for several reasons and after double-clicking the app will launch and crash due to some system error.
This will be the case if you have some other software previously installed with an older
version of Python set as the default `PATH` for Windows. 

### 5.2) Executing via Command Prompt
The _safest_ way to execute the app is via Command Prompt. 
First, make sure you know the _system path to the app file_.
For instance, let the path be `C:/Users/You/Documents/abm-cue-main/app_cue1d.py`.
Then open the Command Prompt and type:
```commandline
python C:/Users/You/Documents/abm-cue-main/app_cue1d.py
```

It would look like this:

![app](https://github.com/ipo-exe/abm-cue/blob/main/figs/install_windows_app_cmd.png "app")

### 5.3) Executing via IDLE or third-party IDEs

Alternatively, you may open and execute the app file from the script editor 
`IDLE` that was installed with Python or third-party IDEs 
such as PyCharm, Sublime, etc.

This is the _unsafest_ way
to execute the app file since **you might commit unwanted 
detrimental changes to the source code**. One advantage, tough, is
that if you are dealing with execution issues you may inform yourself about the 
error types returned from the system.

