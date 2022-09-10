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

For example, let `Alpha = 100` (very large) so agents can interact with any place. 
Now consider an agent with orientation trait `Agent_trait = 10` surrounded by places of the following
traits: `[1, 20, 11, 8]`. Which place it will move in the next step?

The answer is: _we will never know_, because his movement is **random**.
However, the likelihood of moving towards the place of trait `Place_trait = 11` is much higher
than of moving towards the place of trait `Place_trait = 20`. 
In fact, in this example, the probabilities of moving to each place is `[0.09, 0.05, 0.45, 0.41]`.

Now, let `Alpha < 10` in a way that the interaction threshold excludes 
`Place_trait = 1` and `Place_trait = 20` from the possibility of interaction.
In such condition, the probabilities of moving to each place is `[0.0, 0.0, 0.53, 0.47]`.

Finally, in the situation when all places around are beyond the interaction threshold, there is no bias in
the random walk, and the probabilities of moving to each place is `[0.25, 0.25, 0.25, 0.25]` (just an uniform random walk).

### Basic Benchmark runs

Some bench tests of the model in very restricted conditions were performed in order to get useful insights.

#### Benchmark 0: nothing happens

Here a single agent that never interacts walks in a constant world.

Parameters:
* `N_Agents`: 1
* `N_Places`: 40
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

### Multi-parameter simulations

The 1D world can be populated with places with different combinations of parameters. For instance, agents can have
different interaction thresholds (`Alpha` parameter). Or different distance thresholds (`Beta` parameter), and so on.

#### Benchmark 7: multi-alpha simulation of closed agents in an open world

Here we have 3 closed agents with same `Beta = 2` but different `Alpha` so only two of them interact with places.
The environment in which they walk is a constant world of `Trait = 1`. 
Agents are set to return to they initial place each time step.

Agents Parameters:
```
Id;  x; Trait; Alpha; Beta;   C;    Name; Alias; Color
 1;  5;    12;    20;    2; 0.0; Agent 1;    a1;   red
 2; 15;     8;     5;    2; 0.0; Agent 2;    a2;  blue
 3; 24;     4;     5;    2; 0.0; Agent 3;    a3; green
```

Despite having a high-value trait, Agent 1 has also a large interaction threshold 
(`Alpha = 20`) so it expected to interact with places.

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench7.gif "bench7")


#### Benchmark 8: "attractor" effect with multi-alpha and multi-beta combinations

As already stated, agents walk randomly but biased towards places like them. This allows to scenarios where
the effect of one agent in the environment attracts others by changing the environment to a sufficient trait level.

Agents Parameters:
```
Id;  x; Trait; Alpha; Beta;   C;    Name; Alias; Color
 1;  5;    10;     7;    2; 0.0; Agent 1;    a1;   red
 2; 15;     5;     6;    2; 0.0; Agent 2;    a2;  blue
 3; 25;    12;     9;    2; 0.0; Agent 3;    a3; green
```

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench8.gif "bench8")


Plot for agents's positions. Note that Agent 2 is the cause of the attractor effect.

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench8a.png "bench8a")


#### Benchmark 9: "preference" effect with multi-alpha and multi-beta combinations

If agents are set to return to their respective initial place every time step, the attractor effect only happens
if there are superpositions on the distance thresholds. In this sense, it might be described more like a 
"preference effect" -- a more interesting neighborhood for some agents.

Agents Parameters:
```
Id;  x; Trait; Alpha; Beta;   C;    Name; Alias; Color
 1;  5;    10;     7;    6; 0.0; Agent 1;    a1;   red
 2; 15;     5;     6;    8; 0.0; Agent 2;    a2;  blue
 3; 25;    12;     9;    6; 0.0; Agent 3;    a3; green
```

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench9.gif "bench9")


Plot for agents's positions. Note that Agent 2 is the cause of the attractor effect.

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench9a.png "bench9a")


#### Benchmark 10: "attract-release" or "contamination" effect with open agents

So far agents were completely closed for change (`C = 0`). However, if some agents are even slightly open for 
change (`C > 0`) then the attracting effect ends up with a rebound, releasing the agents to interact with
places that earlier were uninteresting. They end up being "contaminated" after enough interactions.

Agents Parameters:
```
Id;  x; Trait; Alpha; Beta;   C;    Name; Alias; Color
 1;  8;    10;     7;    6; 0.01; Agent 1;    a1;   red
 2; 15;     5;     6;    4;  0.0; Agent 2;    a2;  blue
 3; 22;    12;     9;    6; 0.01; Agent 3;    a3; green
```

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench10.gif "bench10")


Plot for agents' positions. Note that Agent 2 is the cause of the attractor effect. 
Initially, Agents 1 and 3 walk randomly without interactions until they got attracted by
the region of influence of Agent 2. Then, after changing enough, Agents 1 and 3 start
to interact with their respective region of influence. 

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench10a.png "bench10a")

Plot for agents' traits. Note that Agent 2 is closed and is (`C = 0`) the cause of the attractor effect. 
Agents 1 and 3 are open (`C > 0`) and start interacting in the attractor region of influence after some random walk.
Then they change so much that they are released from the attractor region. 

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench10b.png "bench10b")


#### Benchmark 11: exploring density effects

Agents can be grouped into blocks of categories so density effects can be simulated. 
This is done simply by adding identical Agents (same Name, Alias and Color) like this:

Agents Parameters:
```
Id;  x; Trait; Alpha; Beta;   C;    Name; Alias; Color
 1;  8;    10;     7;    6; 0.01; Agent 1;    a1;   red
 2;  7;    10;     7;    6; 0.01; Agent 1;    a1;   red
 3;  6;    10;     7;    6; 0.01; Agent 1;    a1;   red
 4;  8;    10;     7;    6; 0.01; Agent 1;    a1;   red
 5; 15;     5;     6;    4;  0.0; Agent 2;    a2;  blue
 6; 14;     5;     6;    4;  0.0; Agent 2;    a2;  blue
 7; 15;     5;     6;    4;  0.0; Agent 2;    a2;  blue
 8; 16;     5;     6;    4;  0.0; Agent 2;    a2;  blue
 9; 15;     5;     6;    4;  0.0; Agent 2;    a2;  blue
10; 15;     5;     6;    4;  0.0; Agent 2;    a2;  blue
11; 15;     5;     6;    4;  0.0; Agent 2;    a2;  blue
12; 15;     5;     6;    4;  0.0; Agent 2;    a2;  blue
13; 22;    12;     9;    6; 0.01; Agent 3;    a3; green
14; 23;    12;     9;    6; 0.01; Agent 3;    a3; green
15; 22;    12;     9;    6; 0.01; Agent 3;    a3; green
```

This is the same settings for the attractor-release scenario. 
However, note that there are several clones of Agent 1, 2 and 3. 
They can start in any position `x`. 


Plot for agents' positions. Note that Agent 2 is the cause of the attractor effect. 
Clearly, the higher density of Agents accelerated the attraction since the environment
changed much faster.

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench11a.png "bench11a")

