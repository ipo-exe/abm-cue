# Agent-based Modelling - Coorperation of Urban Environments (CUE) 

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

![figure](https://github.com/ipo-exe/abm-cue/blob/main/figs/worlds.png "Worlds")


### The Delta_c parameter

The `Delta_c` parameter is the critical Hamming distance of trait orientation for Agent-Place interaction. It is used to decide if Agent-Place interactions occur or not. It has the same units of traits. For instance, if `Delta_c = 10` this means that Agent-Place interactions only will occur when the absolute discrepancy between traits is less than 10. If `Delta_c` is higher than the maximum value of traits in the model, interactions will always happen.

* When `Delta_c > max(Traits)`, Agents will _always_ interact with Places.
* When `Delta_c = 0`, Agents will _never_ interact with Places.

### The R_c parameter 

The `R_c` parameter defines the critical radius for the Agent's limited window of sight to the nearest Places to go. It has integer units of cells. The window of sight of the Agent comprises the Agent's position `i + - R_c` cell units in x and y spatial dimensions. For instance, if `R_c = 2` and the Agent cell position is `i = 5` then the window of sight is cells [3, 4, 6, 7] in one dimension. 

### The C_a and C_p parameters

The `C_a` is the Agent openness to contamination, or place-to-agent degree of interaction influence.  

The `C` is the openness of Agents to change after interacting with a Place:

```markdown
posterior_Agent_trait = (prior_Agent_trait + (C * Place_trait)) / (1 + C)
```
So:
* When `C = 0`, Agents will never be influenced by Places;
* When `C < 1`, Agents posterior trait will be weakly influenced by Places.
* When `C = 1`, Agents posterior trait will be the average between Agent and Place prior traits (50% influence);
* When `C > 1`, Agents posterior trait will be strongly influenced by Places.

The same logic applies to the `D` parameter. 
The `D` is the openness of Places to change after interacting with an Agent:

```markdown
posterior_Place_trait = (prior_Place_trait + (D * Agent_trait)) / (1 + D)
```
So:
* When `D = 0`, Places will never be influenced by Agents;
* When `D < 1`, Places posterior trait will be weakly influenced by Agents.
* When `D = 1`, Places posterior trait will be the average between Agents and Places prior traits (50% influence);
* When `D > 1`, Places posterior trait will be strongly influenced by Agents.

### The biased random walk

Agents walk randomly but biased towards Places like them. 

For example, let `Alpha = 100` (very large) so Agents can interact with any Place. 
Now consider an Agent with orientation trait `Agent_trait = 10` surrounded by Places of the following
traits: `[1, 20, 11, 8]`. Which Place it will move in the next step?

The answer is: _we will never know_, because his movement is **random**.
However, the likelihood of moving towards the Place of trait `Place_trait = 11` is much higher
than of moving towards the Place of trait `Place_trait = 20`. 
In fact, in this example, the probabilities of moving to each Place is `[0.09, 0.05, 0.45, 0.41]`.

Now, let `Alpha < 10` in a way that the interaction threshold excludes 
`Place_trait = 1` and `Place_trait = 20` from the possibility of interaction.
In such condition, the probabilities of moving to each Place is `[0.0, 0.0, 0.53, 0.47]`.

Finally, in the situation when all Places around are beyond the interaction threshold, there is no bias in
the random walk, and the probabilities of moving to each Place is `[0.25, 0.25, 0.25, 0.25]` (just an uniform random walk).



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




### Basic Benchmark runs

Some bench tests of the model in very restricted conditions were performed in order to get useful insights.

#### Benchmark 0: nothing happens

Here a single Agent that never interacts walks in a constant world.

Parameters:
* `N_Agents`: 1
* `N_Places`: 40
* `Alpha`: 0 (no interaction)
* `Beta`: 3
* `C`: 0 (Agent never change)
* `D`: 1 (Places change 50% at each interaction)
* `N_Steps`: 200

Initial conditions:
* `Agent_trait = 18`
* `Agent_i = 20` (position)
* `Place_trait = 2` (all)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench0.gif "bench0")

#### Benchmark 1: the closed Agent alone in an open world

Here a single Agent that never change (closed Agent) walks in a constant (but open) world, changing it.

Parameters:
* `N_Agents`: 1
* `N_Places`: 40
* `Alpha`: 20 (full interaction)
* `Beta`: 3
* `C`: 0 (Agent never change)
* `D`: 1 (Places change 50% at each interaction)
* `N_Steps`: 200

Initial conditions:
* `Agent_trait = 18`
* `Agent_i = 20` (position)
* `Place_trait = 2` (all)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench1.gif "bench1")

#### Benchmark 2: the open Agent alone in a closed world

Here a single Agent that is open to change walks in a world that never change (closed world).

Parameters:
* `N_Agents`: 1
* `N_Places`: 40
* `Alpha`: 20 (full interaction)
* `Beta`: 3
* `C`: 0.01 (Agent change 1% at each interaction)
* `D`: 0.0 (Places never change)
* `N_Steps`: 200

Initial conditions:
* `Agent_trait = 18`
* `Agent_i = 20` (position)
* `Place_trait = 2` (all)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench2.gif "bench2")


#### Benchmark 3: the open Agent alone in an open world

Here a single Agent that is open to change walks in a world that is also open to change.

Parameters:
* `N_Agents`: 1
* `N_Places`: 40
* `Alpha`: 20 (full interaction)
* `Beta`: 3
* `C`: 0.01 (Agent change 1% at each interaction)
* `D`: 0.05 (Places change 5% at each interaction)
* `N_Steps`: 200

Initial conditions:
* `Agent_trait = 18`
* `Agent_i = 20` (position)
* `Place_trait = 2` (all)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench3.gif "bench3")


#### Benchmark 4: Agent with larger window of sigth

Here benchmark 3 is revisited with an Agent with a larger window of sight (`Beta` parameter).

Parameters:
* `N_Agents`: 1
* `N_Places`: 40
* `Alpha`: 20 (full interaction)
* `Beta`: 6 (larger)
* `C`: 0.01 (Agent change 1% at each interaction)
* `D`: 0.05 (Places change 5% at each interaction)
* `N_Steps`: 200

Initial conditions:
* `Agent_trait = 18`
* `Agent_i = 20` (position)
* `Place_trait = 2` (all)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench4.gif "bench4")

#### Benchmark 5: an Agent (not that open) in a binary world

Here the Agent interacts only with Places within the `Alpha` threshold. 

Parameters:
* `N_Agents`: 1
* `N_Places`: 40
* `Alpha`: 10
* `Beta`: 3
* `C`: 0.01 (Agent change 1% at each interaction)
* `D`: 0.05 (Places change 5% at each interaction)
* `N_Steps`: 200

Initial conditions:
* `Agent_trait = 13`
* `Agent_i = 20` (position)
* `Place_trait = 18` (first half)
* `Place_trait = 2` (second half)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench5.gif "bench5")

#### Benchmark 6: two Agents (not that open) in a binary world

Benchmark 5 revisited with two different Agents.

Parameters:
* `N_Agents`: 2
* `N_Places`: 40
* `N_Types`: 20
* `Alpha`: 10
* `Beta`: 3
* `C`: 0.01 (Agent change 1% at each interaction)
* `D`: 0.05 (Places change 5% at each interaction)
* `N_Steps`: 200

Initial conditions:
* `Agent_trait = 13` (first Agent)
* `Agent_trait = 8` (second Agent)
* `Agent_i = 20` (both positions)
* `Place_trait = 18` (first half)
* `Place_trait = 2` (second half)

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench6.gif "bench6")

### Multi-parameter simulations

The 1D world can be populated with Places with different combinations of parameters. For instance, Agents can have
different interaction thresholds (`Alpha` parameter). Or different distance thresholds (`Beta` parameter), and so on.

#### Benchmark 7: multi-alpha simulation of closed Agents in an open world

Here we have 3 closed Agents with same `Beta = 2` but different `Alpha` so only two of them interact with Places.
The environment in which they walk is a constant world of `Trait = 1`. 
Agents are set to return to they initial Place each time step.

Agents Parameters:
```
Id;  x; Trait; Alpha; Beta;   C;    Name; Alias; Color
 1;  5;    12;    20;    2; 0.0; Agent 1;    a1;   red
 2; 15;     8;     5;    2; 0.0; Agent 2;    a2;  blue
 3; 24;     4;     5;    2; 0.0; Agent 3;    a3; green
```

Despite having a high-value trait, Agent 1 has also a large interaction threshold 
(`Alpha = 20`) so it expected to interact with Places.

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench7.gif "bench7")


#### Benchmark 8: "attractor" effect with multi-alpha and multi-beta combinations

As already stated, Agents walk randomly but biased towards Places like them. This allows to scenarios where
the effect of one Agent in the environment attracts others by changing the environment to a sufficient trait level.

Agents Parameters:
```
Id;  x; Trait; Alpha; Beta;   C;    Name; Alias; Color
 1;  5;    10;     7;    2; 0.0; Agent 1;    a1;   red
 2; 15;     5;     6;    2; 0.0; Agent 2;    a2;  blue
 3; 25;    12;     9;    2; 0.0; Agent 3;    a3; green
```

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench8.gif "bench8")


Plot for Agents's positions. Note that Agent 2 is the cause of the attractor effect.

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench8a.png "bench8a")


#### Benchmark 9: "preference" effect with multi-alpha and multi-beta combinations

If Agents are set to return to their respective initial Place every time step, the attractor effect only happens
if there are superpositions on the distance thresholds. In this sense, it might be described more like a 
"preference effect" -- a more interesting neighborhood for some Agents.

Agents Parameters:
```
Id;  x; Trait; Alpha; Beta;   C;    Name; Alias; Color
 1;  5;    10;     7;    6; 0.0; Agent 1;    a1;   red
 2; 15;     5;     6;    8; 0.0; Agent 2;    a2;  blue
 3; 25;    12;     9;    6; 0.0; Agent 3;    a3; green
```

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench9.gif "bench9")


Plot for Agents's positions. Note that Agent 2 is the cause of the attractor effect.

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench9a.png "bench9a")


#### Benchmark 10: "attract-release" or "contamination" effect with open Agents

So far Agents were completely closed for change (`C = 0`). However, if some Agents are even slightly open for 
change (`C > 0`) then the attracting effect ends up with a rebound, releasing the Agents to interact with
Places that earlier were uninteresting. They end up being "contaminated" after enough interactions.

Agents Parameters:
```
Id;  x; Trait; Alpha; Beta;   C;    Name; Alias; Color
 1;  8;    10;     7;    6; 0.01; Agent 1;    a1;   red
 2; 15;     5;     6;    4;  0.0; Agent 2;    a2;  blue
 3; 22;    12;     9;    6; 0.01; Agent 3;    a3; green
```

Output:

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench10.gif "bench10")


Plot for Agents' positions. Note that Agent 2 is the cause of the attractor effect. 
Initially, Agents 1 and 3 walk randomly without interactions until they got attracted by
the region of influence of Agent 2. Then, after changing enough, Agents 1 and 3 start
to interact with their respective region of influence. 

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench10a.png "bench10a")

Plot for Agents' traits. Note that Agent 2 is closed and is (`C = 0`) the cause of the attractor effect. 
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


Plot for Agents' positions. Note that Agent 2 is the cause of the attractor effect. 
Clearly, the higher density of Agents accelerated the attraction since the environment
changed much faster.

![anim](https://github.com/ipo-exe/abm-cue/blob/main/figs/bench11a.png "bench11a")

