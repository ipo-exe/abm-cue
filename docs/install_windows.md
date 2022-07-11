# Installation guide for Windows users

Here is a nice installation tutorial for Windows users. 
> **Tip**: read _all_ the steps _before_ executing them! You may anticipate some issues.

## 1) **Download Python**
Go to https://www.python.org/ and download the latest version of `python 3`;
> Note: unless you have good reasons to keep it, we encourage you to first 
> _uninstall_ older Python versions to prevent problems.  

## 2) **Install Python**
Double-click the installation file to launch the **installation wizard**. Then enable the option:

> [x] Add `Python 3.x` to PATH (where `x` is the number of version)
> 
> Example:
> 
> ![addpath](https://github.com/ipo-exe/abm-cue/blob/main/docs/figs/install_windows_add_to_path.png "add")

Click `Install Now` and follow through the installation steps in the wizard:

> ![install](https://github.com/ipo-exe/abm-cue/blob/main/docs/figs/install_windows_install.png "install")

## 3) Install the required dependencies
Here the easiest way is to open the Windows `Command Prompt` program and 
type some installation commands in sequence. 

If you are already using Python, you may want to upgrade `pip` (the package manager) 
to the latest version by typing:
```commandline
python3.x -m pip install --upgrade pip
```
> Warning: you must replace the `x` in `python3.x` by the version number you just installed.
> Hence, for Python 3.10: 
> ```commandline
> python3.10 -m pip install --upgrade pip
> ```
> The same applies to all commands below.

The installation command is the same except the name of the dependency. So the `numpy` installation command will look like this: 
```commandline
python3.x -m pip install numpy
```
Then `scipy` installation:
```commandline
python3.x -m pip install scipy
```
Then `pandas` installation:
```commandline
python3.x -m pip install pandas
```
Then `matplotlib` installation:
```commandline
python3.x -m pip install matplotlib
```
Then `imageio` installation:
```commandline
python3.x -m pip install imageio
```

## 4) Execute the application file

The application file for the 1-d CUE model is the `app_cue1d.py` file.  

### 4.1) Executing by double-clicking
The _easiest_ way to execute the app is **double-click the app file**. 
If everything is OK, Windows should launch the Graphical User Interface of the application.

However, things can be _not_ OK for several reasons and after double-clicking the app will launch and crash due to some system error.
This will be the case if you have some other software previously installed with an older
version of Python set as the default `PATH` for Windows. 

### 4.2) Executing via Command Prompt
The _safest_ way to execute the app is via Command Prompt. 
First, make sure you know the _system path to the app file_.
For instance, let the path be `C:/Users/You/Documents/abm-cue-main/app_cue1d.py`.
Then open the Command Prompt and type:
```commandline
python3.x C:/Users/You/Documents/abm-cue-main/app_cue1d.py
```
> Warning: again, you must replace the `x` in `python3.x` by the version number you just installed.
> Hence, for Python 3.10: 
> ```commandline
> python3.10 C:/Users/You/Documents/abm-cue-main/app_cue1d.py
> ```

### 4.3) Executing via IDLE or third-party IDEs

Alternatively, you may open and execute the app file from the script editor 
`IDLE` that was installed with Python or third-party IDEs 
such as PyCharm, Sublime, etc.

This is the _unsafest_ way
to execute the app file since **you might commit unwanted 
detrimental changes to the source code**. One advantage, tough, is
that if you are dealing with executing issues you may inform yourself about the 
error types returned from the system.

