# Agent-based Modelling - Coorperation of Urban Environments (CUE) 
 - [Model overview](https://github.com/ipo-exe/abm-cue/blob/main/docs/guide.md#model-overview)
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
7) Agents interaction, Agents may contaminate the Place trait to a certain extent, and vice-versa.

The expected output from simulations is a evolving environment of the traits of Agents and Places. A low-entropy system may or not emerge depending on the initial conditions.

### The 1-D and 2-D worlds

The simulated world has a gridded structure. That is, it is a rectagular grid of cells. Both versions of 1-D and 2-D worlds are _infinite_ in the sense that Agents can loop around, leaving one edge to show up in the other. Locality is determined by the rows and columns indexes `x` and `y`. 

![figure](https://github.com/ipo-exe/abm-cue/blob/main/figs/worlds.PNG "Worlds")


### The D parameter

`D` is a parameter of Agents. It is the critical Hamming distance of trait orientation for Agent-Place interaction. It is used to decide if Agent-Place interactions occur or not. It has the same units of traits. For instance, if `D = 10` this means that Agent-Place interactions only will occur when the absolute discrepancy between traits is less than 10. If `D` is higher than the maximum value of traits in the model, interactions will always happen.

* When `D > max(Traits)`, Agents will _always_ interact with Places.
* When `D = 0`, Agents will _never_ interact with Places.

### The R parameter 

`R` is a parameter of Agents. It defines the critical radius for the Agent's limited window of sight to the nearest Places to go. It has integer units of cells. The window of sight of the Agent comprises the Agent's position `i + - R` cell units in x and y spatial dimensions. For instance, if `R = 2` and the Agent cell position is `i = 5` then the window of sight is cells [3, 4, 6, 7] in one dimension. 

![figure](https://github.com/ipo-exe/abm-cue/blob/main/figs/windows.png "Windows")

### The C parameter

> **Note**: see the theoretical notation PDF:
> [`iodocs.md`](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md);

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

### The random walk

At each time step, Agents walk randomly towards the avaiable Places for interaction. The functions for weighting the decision likelihood are:

* `Uniform` - equal likelihood for the available places;
* `Linear` - trait-based proportional likelihood (Agents are biased to Places like them). 

When all Places around are beyond the interaction threshold, the `Uniform` function is used.

## CUE 1d model guide

### Files to run the model

There are 3 files needed to run the model:
1) the simulation parameters file (`param_simulation.txt`);
2) the Agents parameters file (`param_Agents.txt`);
3) the Places parameters file (`param_Places.txt`).

All files to run the model are plain `.txt` files.

> **Note**: see the Input/Output documentation:
> [`iodocs.md`](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md);

The simulation parameter file looks like this:
```text
     Metadata; Value
    Timestamp; 2022/07/05 07:59:57.65
 Input Folder; C:/Users/You/Documents/abm-cue/samples
   Run Folder; C:/Users/You/Documents/outputs
  Agents File; C:/Users/You/Documents/abm-cue/samples/param_Agents.txt
  Places File; C:/Users/You/Documents/abm-cue/samples/param_Places.txt
        Steps; 100
Return Agents; False
   Trace Back; False
 Plot Results; True
```
Where the `Value` column can be edited either manually or via the Graphical User Interface.

* `Input Folder` [text]: system path to a folder where the input file are stored;
* `Run Folder` [text]: system path to a folder used for simulation outputs;
* `Agents File` [text]: system path to the param_Agents.txt file;
* `Places File `[text]: system path to the param_Places.txt file;
* `Steps` [positive integer number]: number of time steps in the simulation;
* `Return Agents` [boolean: False or True]: option to return Agents to the initial
Place every time step;
* `Trace Back` [boolean: False or True]: option to keep track of all steps in the simulation;
> Note that if `Trace Back = True`, the simulation may turn out to be computationally heavy. 
* `Plot Results` [boolean: False or True]: option to create graphics after simulation.

The Agents parameters must be provided in tha plain `.txt` file like this:

```text
Id;  x; Trait; Alpha; Beta;    C;    Name; Alias; Color
 1;  5;    20;    20;    5;  0.0; Agent A;   AgA; red
 2; 10;    20;    20;    5;  0.0; Agent B;   AgB; blue
 3; 15;     1;    20;    5; 0.01; Agent C;   AgC; orange
 4; 35;     1;    20;    3; 0.01; Agent C;   AgC; orange
```

Where:
* `Id`: [positive unique integer]: is the Agent unique identifier;
* `x`: [positive integer]: is the Agent position in space;
* `Trait`: [positive real] is the Agent trait;
* `Alpha`: [positive real] orientation threshold for Agent-Place interaction;
* `Beta`: [positive integer > 0] distance threshold for Agent movement;
* `C`: [positive real] Place-to-Agent degree of interaction influence (Agents openness to change);
* `Name`: [text] Agent full name;
* `Alias`: [text] Agent alias (nickname);
* `Color`: [text] Agent color.

The Places parameters must be provided in tha plain `.txt` file like this:

```text
Id;  x; Trait;   D;    Name; Alias
 1;  0;     5; 0.1; Place A;    PA
 2;  1;     5; 0.1; Place A;    PA
 3;  2;     5; 0.1; Place A;    PA
 4;  3;     5; 0.1; Place A;    PA
 ...
36; 35;     5; 0.1; Place B;    PB
37; 36;     5; 0.1; Place B;    PB
38; 37;     5; 0.1; Place B;    PB
39; 38;     5; 0.1; Place B;    PB
40; 39;     5; 0.1; Place B;    PB
```

Where:
* `Id`: [positive unique integer] is the Place unique identifier;
* `x`: [positive integer] is the Place position in space;
* `Trait`: [positive real] is the Place trait;
* `D`: [positive real] Agent-to-Place degree of interaction influence (Places openness to change);
* `Name`: [text] Place full name;
* `Alias`: [text] Place alias (nickname);
* `Color`: [text] Place color.



## CUE 2D Model Guide