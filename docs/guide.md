# Agent-based Modelling - Coorperation of Urban Environments (CUE) 

 - [Model overview](https://github.com/ipo-exe/abm-cue/blob/main/docs/guide.md#model-overview)
 - [The 1-D and 2-D worlds](https://github.com/ipo-exe/abm-cue/blob/main/docs/guide.md#the-1-d-and-2-d-worlds)
 - [The random walk](https://github.com/ipo-exe/abm-cue/blob/main/docs/guide.md#the-random-walk)
 - [Attributes of Agents and Places](https://github.com/ipo-exe/abm-cue/blob/main/docs/guide.md#attributes-of-agents-and-places)
 - [Model parameters](https://github.com/ipo-exe/abm-cue/blob/main/docs/guide.md#model-parameters)
 - [CUE 1D guide](https://github.com/ipo-exe/abm-cue/blob/main/docs/guide.md#cue-1d-model-guide)
 - [CUE 2D guide](https://github.com/ipo-exe/abm-cue/blob/main/docs/guide.md#cue-2d-model-guide)

> **Note**: see the theoretical notation PDF:
> [`iodocs.md`](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md);

## Model overview

The model is characterized by the following general rules:

1) Agents walk randomly around a 1-D or 2-D gridded world of Places;
2) Agents and Places have mutable traits;
3) Agents may have a bias to go to Places like themselves;
4) Agents have a limited window of sight to the nearest Places to go;
5) Agents interact with Places only if they are related enough;
6) Agents evaluate their own trait with a limited memory of previous states;
7) Agents may contaminate the Place trait to a certain extent, and vice-versa.

The expected output from simulations is a evolving environment of the traits of Agents and Places. A low-entropy system may or not emerge depending on the initial conditions.

> **Note**: see the Input/Output and Glossary documentation:
> [`iodocs.md`](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md);

## The 1-D and 2-D worlds

The simulated world has a gridded structure. That is, it is a rectagular grid of cells. Both versions of 1-D and 2-D worlds are infinite in the sense that Agents can loop around, leaving one edge to show up in the other. Locality is determined by the rows and columns coordinates.

> **Note**: In the 1-D world `x` denotes the row coordinate.

> **Note**: In the 2-D world and `y` denotes the row coordinate and `x` denotes the column coordinate.

> **Note**: In the 2-D world Places must be categorized in `Indoor` and `Outdoor`. 

![figure](https://github.com/ipo-exe/abm-cue/blob/main/figs/worlds.PNG "Worlds")

## The random walk

At each time step, Agents walk randomly towards the avaiable Places for interaction. The functions for weighting the decision likelihood are:

* `Uniform` - equal likelihood for the available places;
* `Linear` - trait-based proportional likelihood (Agents are biased to Places like them). 

When all Places around are beyond the interaction threshold, the `Uniform` function is used.

## Attributes of Agents and Places 

> **Note**: see the theoretical notation PDF:
> [`iodocs.md`](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md);

### Id number

Each Agent and Place has an unique integer number, the `Id` label.

### Trait

Trait is a variable attribute of both Agents and Places. They share the same units of traits.

### Position

Agents and Places have locality defined by integer coordinates in the gridded world. Agents positions (`x` and `y`) are mutable. Places positions (`x` and `y`) are immutable.

### Name, Alias and Color

All Agents and Places must have a `Name`, `Alias` (a short nickname for chart plotting) and `Color`. `Color` must be the HEX code or available in the `matplotlib` package [color list](https://matplotlib.org/stable/gallery/color/named_colors.html). These attributes may not be unique for each Agent and Place (clones are allowed). 


## Model Parameters

> **Note**: see the theoretical notation PDF:
> [`iodocs.md`](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md);

### The D parameter

`D` is a parameter of Agents. It is the critical Hamming distance of trait orientation for Agent-Place interaction. It is used to decide if Agent-Place interactions occur or not. It has the same units of traits. For instance, if `D = 10` this means that Agent-Place interactions only will occur when the absolute discrepancy between traits is less than 10. If `D` is higher than the maximum value of traits in the model, interactions will always happen.

* When `D > max(Traits)`, Agents will _always_ interact with Places.
* When `D = 0`, Agents will _never_ interact with Places.

### The R parameter 

`R` is a parameter of Agents. It defines the critical radius for the Agent's limited window of sight to the nearest Places to go. It has integer units of cells. The window of sight of the Agent comprises the Agent's position `i + - R` cell units in x and y spatial dimensions. For instance, if `R = 2` and the Agent cell position is `i = 5` then the window of sight is cells [3, 4, 6, 7] in one dimension. 

![figure](https://github.com/ipo-exe/abm-cue/blob/main/figs/windows.png "Windows")

### The C parameter

`C` is a parameter of both Agents and Places. It quantifies the openness to contamination, or place-to-agent degree of interaction influence. In the case of Agents, the `C` is the openness of any given Agent to change after interacting with a Place:

```markdown
posterior_trait = (prior_trait + (Agent_C * Place_trait)) / (1 + Agent_C)
```
So:
* When `C = 0`, Agents will never be influenced by Places;
* When `C < 1`, Agents posterior trait will be weakly influenced by Places.
* When `C = 1`, Agents posterior trait will be the average between Agent and Place prior traits (50% influence);
* When `C > 1`, Agents posterior trait will be strongly influenced by Places.

The same logic applies to Places: 

```markdown
posterior_trait = (prior_trait + (Place_C * Agent_trait)) / (1 + Place_C)
```
So:
* When `C = 0`, Places will never be influenced by Agents;
* When `C < 1`, Places posterior trait will be weakly influenced by Agents.
* When `C = 1`, Places posterior trait will be the average between Agents and Places prior traits (50% influence);
* When `C > 1`, Places posterior trait will be strongly influenced by Agents.

### The M parameter

The `M` parameter is a parameter of Agents. It defines the memory size for each Agent. It has units of time steps. This memory allocates the `M` previous traits so the Agent's `prior_trait` during interaction is the average of the states stored in memory. 

## CUE 1d model guide

### Files to run the model

There are 3 files needed to run the model:
1) the simulation parameters file (`param_simulation_1d.txt`);
2) the Agents parameters file (`param_agents_1d.txt`);
3) the Places parameters file (`param_places_1d.txt`).

All files to run the model are plain `.txt` files.

> **Note**: the model is not sensitive to file names, as long as the formatting is correct. 

> **Note**: see the Input/Output documentation for proper formatting:
> [`iodocs.md`](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md);

### Running the model in python script

A simple python script to run the model looks like this:

```python
# import the function
from tools import run_cue1d

# define the path to the simulation file
file_simulation = "C:/You/Documents/abm-cue/param_simulation_1d.txt"

# call the function
run_cue1d(s_fsim=file_simulation)

```

### Running the model by using the GUI app

A simple Graphic User Interface is available to run the model. Data Management Tools are also available to setup the Agents and Places parameters files.



## CUE 2D Model Guide

### Files to run the model

There are 3 files needed to run the model:
1) the simulation parameters file (`param_simulation_1d.txt`);
2) the Agents parameters file (`param_agents_1d.txt`);
3) the Places parameters file (`param_places_1d.txt`).

All files to run the model are plain `.txt` files.

> **Note**: the model is not sensitive to file names, as long as the formatting is correct. 

> **Note**: see the Input/Output documentation for proper formatting:
> [`iodocs.md`](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md);

### Running the model in python script

A simple python script to run the model looks like this:

```python
# import the function
from tools import run_cue1d

# define the path to the simulation file
file_simulation = "C:/You/Documents/abm-cue/param_simulation_1d.txt"

# call the function
run_cue1d(s_fsim=file_simulation)

```

### Running the model by using the GUI app

A simple Graphic User Interface is available to run the model. Data Management tools are also available for 