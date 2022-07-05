# Agent-based Modelling - Coorperation of Urban Environments (CUE) 

## CUE 1d model guide

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
* `C`: [positive real] place-to-agent degree of interaction influence (agents openness to change);
* `D`: [positive real] agent-to-place degree of interaction influence (places openness to change);
* `N_Steps`: [positive integer] number of time steps for simulation.

The `Min` and `Max` fields are reserved for future developments (such as sensitivity analysis 
and model calibration). Those fields are not used in the model standard simulation.

### The Alpha parameter

The `Alpha` parameter is a _factor_, i.e., it varies _from 0 to 1_. 
It is used to compute the agent-place type threshold given the number of orientation types:
```markdown
threshold = Alpha * N_Types
```
For instance, if `N_Types = 100` and `Alpha = 0.1` then `threshold = 10`. 
This means that agent-place interactions only will 
occur when the absolute discrepancy between types is less than 10.

* When `Alpha = 1`, agents will _always_ interact with places.
* When `Alpha = 0`, agents will _never_ interact with places.

### The Beta parameter 

The `Beta` parameter defines the distance threshold for the agent to move 
from place to place in the 1-D ring-like world. 
The window of sight of the agent comprises the agent's position `i` + - Beta` cell units.

For instance, if `Beta = 2` and the agent cell position is `i = 5` then the window of sight is cells [3, 4, 6, 7].

Note that the 1-D ring like is _infinite_ in the sense that agents can loop around, leaving one edge to show up in the other.

### The C and D parameters

The `C` and `D` parameters sets the respective strengths of agent-places influences on each other. 

The `C` is the openness of agents to change after interacting with a place:

```markdown
posterior_agent_type = (prior_agent_type + (C * place_type)) / (1 + C)
```
So:
* When `C = 0`, agents will never be influenced by places;
* When `C < 1`, agents posterior type will be weakly influenced by places.
* When `C = 1`, agents posterior type will be the average between agent and place prior types (50% influence);
* When `C > 1`, agents posterior type will be strongly influenced by places.

The same logic applies to the `D` parameter. 
The `D` is the openness of places to change after interacting with an agent:

```markdown
posterior_place_type = (prior_place_type + (D * agent_type)) / (1 + D)
```
So:
* When `D = 0`, places will never be influenced by agents;
* When `D < 1`, places posterior type will be weakly influenced by agents.
* When `D = 1`, places posterior type will be the average between agents and places prior types (50% influence);
* When `D > 1`, places posterior type will be strongly influenced by agents.

### The biased random walk

Agents walk randomly but biased towards places like them. 

For example, let `Alpha = 1` so agents can interact with any place. 
Now consider an agent with orientation type `Agent_type = 10` surrounded by places of the following
types: `[1, 20, 11, 8]`. Which place it will move in the next step?

The answer is: _we will never know_, because his movement is **random**.
However, the likelihood of moving towards the place of type `Place_type = 11` is much higher
than of moving towards the place of type `Place_type = 20`. 
In fact, in this example, the probabilities of moving to each place is `[0.09, 0.05, 0.45, 0.41]`.

Now, let `Alpha < 1` in a way that the interaction threshold excludes 
`Place_type = 1` and `Place_type = 20` from the possibility of interaction.
In such condition, the probabilities of moving to each place is `[0.0, 0.0, 0.53, 0.47]`.

Finally, in the situation when all places around are beyond the interaction threshold, there is no bias in
the random walk, and the probabilities of moving to each place is `[0.25, 0.25, 0.25, 0.25]` (just an uniform random walk).

### Benchmark runs

Some bench tests of the model in very restricted conditions were performed in order to get useful insights.

#### Benchmark 0: nothing happens

Here a single agent that never interacts walks in a constant world.

Parameters:
* `N_Agents`: 1
* `N_Places`: 40
* `N_Types`: 20
* `Alpha`: 0 (no interaction)
* `Beta`: 3
* `C`: 0 (agent never change)
* `D`: 1 (places change 50% at each interaction)
* `N_Steps`: 200

Initial conditions:
* `Agent_type = 18`
* `Agent_i = 20` (position)
* `Place_type = 2` (all)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/docs/figs/bench0.gif "bench0")

#### Benchmark 1: the closed agent alone in an open world

Here a single agent that never change (closed agent) walks in a constant (but open) world, changing it.

Parameters:
* `N_Agents`: 1
* `N_Places`: 40
* `N_Types`: 20
* `Alpha`: 1 (full interaction)
* `Beta`: 3
* `C`: 0 (agent never change)
* `D`: 1 (places change 50% at each interaction)
* `N_Steps`: 200

Initial conditions:
* `Agent_type = 18`
* `Agent_i = 20` (position)
* `Place_type = 2` (all)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/docs/figs/bench1.gif "bench1")

#### Benchmark 2: the open agent alone in a closed world

Here a single agent that is open to change walks in a world that never change (closed world).

Parameters:
* `N_Agents`: 1
* `N_Places`: 40
* `N_Types`: 20
* `Alpha`: 1 (full interaction)
* `Beta`: 3
* `C`: 0.01 (agent change 1% at each interaction)
* `D`: 0.0 (places never change)
* `N_Steps`: 200

Initial conditions:
* `Agent_type = 18`
* `Agent_i = 20` (position)
* `Place_type = 2` (all)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/docs/figs/bench2.gif "bench2")


#### Benchmark 3: the open agent alone in an open world

Here a single agent that is open to change walks in a world that is also open to change.

Parameters:
* `N_Agents`: 1
* `N_Places`: 40
* `N_Types`: 20
* `Alpha`: 1 (full interaction)
* `Beta`: 3
* `C`: 0.01 (agent change 1% at each interaction)
* `D`: 0.05 (places change 5% at each interaction)
* `N_Steps`: 200

Initial conditions:
* `Agent_type = 18`
* `Agent_i = 20` (position)
* `Place_type = 2` (all)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/docs/figs/bench3.gif "bench3")


#### Benchmark 4: agent with larger window of sigth

Here benchmark 3 is revisited with an agent with a larger window of sight (`Beta` parameter).

Parameters:
* `N_Agents`: 1
* `N_Places`: 40
* `N_Types`: 20
* `Alpha`: 1 (full interaction)
* `Beta`: 6 (larger)
* `C`: 0.01 (agent change 1% at each interaction)
* `D`: 0.05 (places change 5% at each interaction)
* `N_Steps`: 200

Initial conditions:
* `Agent_type = 18`
* `Agent_i = 20` (position)
* `Place_type = 2` (all)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/docs/figs/bench4.gif "bench4")

#### Benchmark 5: an agent (not that open) in a binary world

Here the agent interacts only with places within the `Alpha` threshold. 

Parameters:
* `N_Agents`: 1
* `N_Places`: 40
* `N_Types`: 20
* `Alpha`: 0.5 (threshold = 10)
* `Beta`: 3
* `C`: 0.01 (agent change 1% at each interaction)
* `D`: 0.05 (places change 5% at each interaction)
* `N_Steps`: 200

Initial conditions:
* `Agent_type = 13`
* `Agent_i = 20` (position)
* `Place_type = 18` (first half)
* `Place_type = 2` (second half)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/docs/figs/bench5.gif "bench5")

#### Benchmark 6: two agents (not that open) in a binary world

Benchmark 5 revisited with two different agents.

Parameters:
* `N_Agents`: 2
* `N_Places`: 40
* `N_Types`: 20
* `Alpha`: 0.5 (threshold = 10)
* `Beta`: 3
* `C`: 0.01 (agent change 1% at each interaction)
* `D`: 0.05 (places change 5% at each interaction)
* `N_Steps`: 200

Initial conditions:
* `Agent_type = 13` (first agent)
* `Agent_type = 8` (second agent)
* `Agent_i = 20` (both positions)
* `Place_type = 18` (first half)
* `Place_type = 2` (second half)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/docs/figs/bench6.gif "bench6")

