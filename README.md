# Agent-based Modelling - Coorperation of Urban Environments (CUE) 

## CUE 1d model

### The simulation overview

1) Agents walk randomly around a ring-like 1-D world of places;
2) Agents and places have orientation types;
3) Agents have a _bias_ to go to places like themselves;
4) Agents have a limited window of sight to the nearest places to go;
5) Agents interact with places only if they are related enough;
7) During interaction, agents influence the place orientation type to a certain extent, and vice-versa.

### Parameters of the model
Simulation parameters must be provided in tha plain `.txt` file like this:

```text
Parameter;  Set;  Min;  Max
 N_Agents;    2;    1;  100
 N_Places;   40;    4;  100
  N_Types;   20;    3;   50
    Alpha;  1.0;  0.1;  1.0
     Beta;    6;    1;   10
        C; 0.01; 0.01;  1.5
        D; 0.90; 0.01;  1.5
  N_Steps;   30;   10; 1000
```

Where the `Set` field is used in the simulation:
* `N_Agents`: [positive integer] number of agents;
* `N_Places`: [positive integer] number of places;
* `N_Types`: [positive integer] number of action types (orientation of agents and places);
* `Alpha`: [positive real from 0 to 1] orientation threshold for agent-place interaction;
* `Beta`: [positive integer > 0] distance threshold for agent movement;
* `C`: [positive real] place-to-agent degree of interaction influence;
* `D`: [positive real] agent-to-place degree of interaction influence;
* `N_Steps`: [positive integer] number of time steps for simulation.



### The Alpha parameter

The `Alpha` parameter is a _factor_, i.e., it varies _from 0 to 1_. 
It is used to compute the agent-place type threshold given the number of orientation types:
```markdown
threshold = Alpha * N_Types
```
For instance, if `N_Types = 100` and `Alpha = 0.1` then `threshold = 10`. 
This means that agent-place interactions only will 
occur when the absolute discrepancy between types is less then 10.

* When `Alpha = 1`, agents will _always_ interact with places.
* When `Alpha = 0`, agents will _never_ interact with places.

### The Beta parameter 

The `Beta` parameter defines the distance threshold for the agent to move 
from place to place in the 1-D ring-like world. 
The window of sight of the agent comprises the agent's position `i` + - Beta` cell units.

For instance, if `Beta = 2` and the agent cell position is `i = 5` then the window of sight is cells [3, 4, 6, 7].

Note that the 1-D ring like is _infinite_ in the sense that agents can loop around, leaving one edge to show up in the other.

### The C and D parameters

The `C` and `D` parameters sets the respective strengths of agent-places influences. 

