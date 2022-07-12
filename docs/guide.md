# Agent-based Modelling - Coorperation of Urban Environments (CUE) 

## CUE 1d model guide

### The simulation overview

1) Agents walk randomly around a ring-like 1-D world of places;
2) Agents and places have orientation types;
3) Agents have a _bias_ to go to places like themselves;
4) Agents have a limited window of sight to the nearest places to go;
5) Agents interact with places only if they are related enough;
7) During interaction, agents influence the place orientation type to a certain extent, and vice-versa.

### Files to run the model

There are 3 files needed to run the model:
1) the simulation parameters file (`param_simulation.txt`);
2) the agents parameters file (`param_agents.txt`);
3) the places parameters file (`param_places.txt`).

All files to run the model are plain `.txt` files.

> **Note**: see the Input/Output documentation:
> [`iodocs.md`](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md);

The simulation parameter file looks like this:
```text
     Metadata; Value
    Timestamp; 2022/07/05 07:59:57.65
 Input Folder; C:/Users/You/Documents/abm-cue/samples
   Run Folder; C:/Users/You/Documents/outputs
  Agents File; C:/Users/You/Documents/abm-cue/samples/param_agents.txt
  Places File; C:/Users/You/Documents/abm-cue/samples/param_places.txt
        Steps; 100
Return Agents; False
   Trace Back; False
 Plot Results; True
```
Where the `Value` column can be edited either manually or via the Graphical User Interface.

* `Input Folder` [text]: system path to a folder where the input file are stored;
* `Run Folder` [text]: system path to a folder used for simulation outputs;
* `Agents File` [text]: system path to the param_agents.txt file;
* `Places File `[text]: system path to the param_places.txt file;
* `Steps` [positive integer number]: number of time steps in the simulation;
* `Return Agents` [boolean: False or True]: option to return agents to the initial
place every time step;
* `Trace Back` [boolean: False or True]: option to keep track of all steps in the simulation;
> Note that if `Trace Back = True`, the simulation may turn out to be computationally heavy. 
* `Plot Results` [boolean: False or True]: option to create graphics after simulation.

The agents parameters must be provided in tha plain `.txt` file like this:

```text
Id;  x; Trait; Alpha; Beta;    C;    Name; Alias; Color
 1;  5;    20;    20;    5;  0.0; Agent A;   AgA; red
 2; 10;    20;    20;    5;  0.0; Agent B;   AgB; blue
 3; 15;     1;    20;    5; 0.01; Agent C;   AgC; orange
 4; 35;     1;    20;    3; 0.01; Agent C;   AgC; orange
```

Where:
* `Id`: [positive unique integer]: is the agent unique identifier;
* `x`: [positive integer]: is the agent position in space;
* `Trait`: [positive real] is the agent trait;
* `Alpha`: [positive real] orientation threshold for agent-place interaction;
* `Beta`: [positive integer > 0] distance threshold for agent movement;
* `C`: [positive real] place-to-agent degree of interaction influence (agents openness to change);
* `Name`: [text] Agent full name;
* `Alias`: [text] Agent alias (nickname);
* `Color`: [text] Agent color.

The places parameters must be provided in tha plain `.txt` file like this:

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
* `Id`: [positive unique integer] is the place unique identifier;
* `x`: [positive integer] is the place position in space;
* `Trait`: [positive real] is the place trait;
* `D`: [positive real] agent-to-place degree of interaction influence (places openness to change);
* `Name`: [text] Place full name;
* `Alias`: [text] Place alias (nickname);
* `Color`: [text] Place color.


### The Alpha parameter

The `Alpha` parameter is an absolute trait threshold. 
It is used to decide if agent-place interactions occur or not.
For instance, if `Alpha = 10` this means that agent-place interactions only will 
occur when the absolute discrepancy between traits is less than 10. 
If `Alpha` is higher than the maximum value of traits in the model,
interactions will always happen.

* When `Alpha > max(Traits)`, agents will _always_ interact with places.
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
posterior_agent_trait = (prior_agent_trait + (C * place_trait)) / (1 + C)
```
So:
* When `C = 0`, agents will never be influenced by places;
* When `C < 1`, agents posterior trait will be weakly influenced by places.
* When `C = 1`, agents posterior trait will be the average between agent and place prior traits (50% influence);
* When `C > 1`, agents posterior trait will be strongly influenced by places.

The same logic applies to the `D` parameter. 
The `D` is the openness of places to change after interacting with an agent:

```markdown
posterior_place_trait = (prior_place_trait + (D * agent_trait)) / (1 + D)
```
So:
* When `D = 0`, places will never be influenced by agents;
* When `D < 1`, places posterior trait will be weakly influenced by agents.
* When `D = 1`, places posterior trait will be the average between agents and places prior traits (50% influence);
* When `D > 1`, places posterior trait will be strongly influenced by agents.

### The biased random walk

Agents walk randomly but biased towards places like them. 

For example, let `Alpha = 1` so agents can interact with any place. 
Now consider an agent with orientation trait `Agent_trait = 10` surrounded by places of the following
traits: `[1, 20, 11, 8]`. Which place it will move in the next step?

The answer is: _we will never know_, because his movement is **random**.
However, the likelihood of moving towards the place of trait `Place_trait = 11` is much higher
than of moving towards the place of trait `Place_trait = 20`. 
In fact, in this example, the probabilities of moving to each place is `[0.09, 0.05, 0.45, 0.41]`.

Now, let `Alpha < 1` in a way that the interaction threshold excludes 
`Place_trait = 1` and `Place_trait = 20` from the possibility of interaction.
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
* `Agent_trait = 18`
* `Agent_i = 20` (position)
* `Place_trait = 2` (all)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench0.gif "bench0")

#### Benchmark 1: the closed agent alone in an open world

Here a single agent that never change (closed agent) walks in a constant (but open) world, changing it.

Parameters:
* `N_Agents`: 1
* `N_Places`: 40
* `N_Types`: 20
* `Alpha`: 20 (full interaction)
* `Beta`: 3
* `C`: 0 (agent never change)
* `D`: 1 (places change 50% at each interaction)
* `N_Steps`: 200

Initial conditions:
* `Agent_trait = 18`
* `Agent_i = 20` (position)
* `Place_trait = 2` (all)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench1.gif "bench1")

#### Benchmark 2: the open agent alone in a closed world

Here a single agent that is open to change walks in a world that never change (closed world).

Parameters:
* `N_Agents`: 1
* `N_Places`: 40
* `N_Types`: 20
* `Alpha`: 20 (full interaction)
* `Beta`: 3
* `C`: 0.01 (agent change 1% at each interaction)
* `D`: 0.0 (places never change)
* `N_Steps`: 200

Initial conditions:
* `Agent_trait = 18`
* `Agent_i = 20` (position)
* `Place_trait = 2` (all)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench2.gif "bench2")


#### Benchmark 3: the open agent alone in an open world

Here a single agent that is open to change walks in a world that is also open to change.

Parameters:
* `N_Agents`: 1
* `N_Places`: 40
* `N_Types`: 20
* `Alpha`: 20 (full interaction)
* `Beta`: 3
* `C`: 0.01 (agent change 1% at each interaction)
* `D`: 0.05 (places change 5% at each interaction)
* `N_Steps`: 200

Initial conditions:
* `Agent_trait = 18`
* `Agent_i = 20` (position)
* `Place_trait = 2` (all)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench3.gif "bench3")


#### Benchmark 4: agent with larger window of sigth

Here benchmark 3 is revisited with an agent with a larger window of sight (`Beta` parameter).

Parameters:
* `N_Agents`: 1
* `N_Places`: 40
* `N_Types`: 20
* `Alpha`: 20 (full interaction)
* `Beta`: 6 (larger)
* `C`: 0.01 (agent change 1% at each interaction)
* `D`: 0.05 (places change 5% at each interaction)
* `N_Steps`: 200

Initial conditions:
* `Agent_trait = 18`
* `Agent_i = 20` (position)
* `Place_trait = 2` (all)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench4.gif "bench4")

#### Benchmark 5: an agent (not that open) in a binary world

Here the agent interacts only with places within the `Alpha` threshold. 

Parameters:
* `N_Agents`: 1
* `N_Places`: 40
* `N_Types`: 20
* `Alpha`: 10
* `Beta`: 3
* `C`: 0.01 (agent change 1% at each interaction)
* `D`: 0.05 (places change 5% at each interaction)
* `N_Steps`: 200

Initial conditions:
* `Agent_trait = 13`
* `Agent_i = 20` (position)
* `Place_trait = 18` (first half)
* `Place_trait = 2` (second half)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench5.gif "bench5")

#### Benchmark 6: two agents (not that open) in a binary world

Benchmark 5 revisited with two different agents.

Parameters:
* `N_Agents`: 2
* `N_Places`: 40
* `N_Types`: 20
* `Alpha`: 10
* `Beta`: 3
* `C`: 0.01 (agent change 1% at each interaction)
* `D`: 0.05 (places change 5% at each interaction)
* `N_Steps`: 200

Initial conditions:
* `Agent_trait = 13` (first agent)
* `Agent_trait = 8` (second agent)
* `Agent_i = 20` (both positions)
* `Place_trait = 18` (first half)
* `Place_trait = 2` (second half)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench6.gif "bench6")

