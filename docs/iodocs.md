# I/O documentation
 - [Imported files](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#imported-files)
 - [Output files](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#output-files)
 - [Glossary](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#glossary)

# Imported files
These files must be prepared and sourced by the user. Samples are provided for proper formatting.

|File | Source | Format | Sample|
|:--- | :--- | :--- | :---|
|[param_agents_1d.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_agents_1dtxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_agents_1d.txt)|
|[param_agents_2d.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_agents_2dtxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_agents_2d.txt)|
|[param_places_1d.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_places_1dtxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_places_1d.txt)|
|[param_places_2d.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_places_2dtxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_places_2d.txt)|
|[map_places_2d.asc](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#map_places_2dasc) | imported by user | Raster Map | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/map_places_2d.asc)|
|[param_simulation_1d.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_simulation_1dtxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_simulation_1d.txt)|
|[param_simulation_2d.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_simulation_2dtxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_simulation_2d.txt)|
|[param_simulation_network_2d.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_simulation_network_2dtxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_simulation_network_2d.txt)|
|[param_batch_simulation.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_batch_simulationtxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_batch_simulation.txt)|

## `param_agents_1d.txt`
 - **Description**: Table of agents parameters and initial conditions;
 - **Source**: imported by user;
 - **File sample**: [param_agents_1d.txt](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_agents_1d.txt);
 - **Format**: Data Table;
 - **Formating example**:
```
Id;  x; Trait;  D; R;  M;    C;    Name; Alias;  Color
 1;  5;    20; 20; 5;  4;  0.0; Agent A;   AgA;    red
 2; 10;    20; 20; 5; 10;  0.0; Agent B;   AgB;   blue
 3; 15;     1; 20; 5;  1; 0.01; Agent C;   AgC; orange
 4; 20;     1; 20; 3;  1; 0.01; Agent C;   AgC; orange
 5; 25;     1; 20; 3;  1; 0.01; Agent C;   AgC; orange
 6; 30;     1; 20; 3;  1; 0.01; Agent C;   AgC; orange
 7; 35;     1; 20; 3;  1; 0.01; Agent C;   AgC; orange
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Id ` | unique integer number | Category numerical identifyier | -|
|` x ` | positive integer number | Position coordinate in the x axis | cell units|
|` Trait ` | positive real number | Trait orientation value | trait units|
|` D ` | positive real number | Critical Hamming Distance of trait orientation for agent-place interaction | -|
|` R ` | positive integer number | Critical radius distance for agent movement. | cell units|
|` M ` | positive integer number | Agent memory lag time. | step units|
|` C ` | positive real number | Agent or Place openness to contamination, degree of interaction influence | -|
|` Name ` | text | Category name | -|
|` Alias ` | text | Category alias (one-word only) | -|
|` Color` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | -|

## `param_agents_2d.txt`
 - **Description**: Table of agents parameters and initial conditions;
 - **Source**: imported by user;
 - **File sample**: [param_agents_2d.txt](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_agents_2d.txt);
 - **Format**: Data Table;
 - **Formating example**:
```
Id; x; y; Trait;  D; R; M;   C;    Name; Alias;  Color
 1; 2; 2;  10.0; 10; 4; 5; 0.0; Agent A;   AgA;    red
 2; 2; 6;   1.0; 10; 1; 1; 0.1; Agent B;   AgB;   blue
 3; 6; 2;     1; 10; 1; 3; 0.5; Agent C;   AgC; orange
 4; 6; 6;     1; 10; 1; 1; 0.0; Agent D;   AgD;  green
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Id ` | unique integer number | Category numerical identifyier | -|
|` x ` | positive integer number | Position coordinate in the x axis | cell units|
|` y ` | positive integer number | Position coordinate in the y axis | cell units|
|` Trait ` | positive real number | Trait orientation value | trait units|
|` D ` | positive real number | Critical Hamming Distance of trait orientation for agent-place interaction | -|
|` R ` | positive integer number | Critical radius distance for agent movement. | cell units|
|` M ` | positive integer number | Agent memory lag time. | step units|
|` C ` | positive real number | Agent or Place openness to contamination, degree of interaction influence | -|
|` Name ` | text | Category name | -|
|` Alias ` | text | Category alias (one-word only) | -|
|` Color` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | -|

## `param_places_1d.txt`
 - **Description**: Table of places parameters and initial conditions;
 - **Source**: imported by user;
 - **File sample**: [param_places_1d.txt](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_places_1d.txt);
 - **Format**: Data Table;
 - **Formating example**:
```
Id;  x; Trait;   C;    Name; Alias; Color
 1;  0;     5; 0.1; Place A;    PA;  blue
 2;  1;     5; 0.1; Place A;    PA;  blue
 3;  2;     5; 0.1; Place A;    PA;  blue
 4;  3;     5; 0.1; Place A;    PA;  blue
 5;  4;     5; 0.1; Place A;    PA;  blue
 6;  5;     5; 0.1; Place A;    PA;  blue
 7;  6;     5; 0.1; Place A;    PA;  blue
 8;  7;     5; 0.1; Place A;    PA;  blue
 9;  8;     5; 0.1; Place A;    PA;  blue
10;  9;     5; 0.1; Place A;    PA;  blue
11; 10;     5; 0.1; Place A;    PA;  blue
12; 11;     5; 0.1; Place A;    PA;  blue
13; 12;     5; 0.1; Place A;    PA;  blue
14; 13;     5; 0.1; Place A;    PA;  blue
15; 14;     5; 0.1; Place A;    PA;  blue
16; 15;     5; 0.1; Place A;    PA;  blue
17; 16;     5; 0.1; Place A;    PA;  blue
18; 17;     5; 0.1; Place A;    PA;  blue
19; 18;     5; 0.1; Place A;    PA;  blue
20; 19;     5; 0.1; Place A;    PA;   red
21; 20;     5; 0.1; Place B;    PB;   red
22; 21;     5; 0.1; Place B;    PB;   red
23; 22;     5; 0.1; Place B;    PB;   red
24; 23;     5; 0.1; Place B;    PB;   red
25; 24;     5; 0.1; Place B;    PB;   red
26; 25;     5; 0.1; Place B;    PB;   red
27; 26;     5; 0.1; Place B;    PB;   red
28; 27;     5; 0.1; Place B;    PB;   red
29; 28;     5; 0.1; Place B;    PB;   red
30; 29;     5; 0.1; Place B;    PB;   red
31; 30;     5; 0.1; Place B;    PB;   red
32; 31;     5; 0.1; Place B;    PB;   red
33; 32;     5; 0.1; Place B;    PB;   red
34; 33;     5; 0.1; Place B;    PB;   red
35; 34;     5; 0.1; Place B;    PB;   red
36; 35;     5; 0.1; Place B;    PB;   red
37; 36;     5; 0.1; Place B;    PB;   red
38; 37;     5; 0.1; Place B;    PB;   red
39; 38;     5; 0.1; Place B;    PB;   red
40; 39;     5; 0.1; Place B;    PB;   red
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Id ` | unique integer number | Category numerical identifyier | -|
|` x ` | positive integer number | Position coordinate in the x axis | cell units|
|` Trait ` | positive real number | Trait orientation value | trait units|
|` C ` | positive real number | Agent or Place openness to contamination, degree of interaction influence | -|
|` Name ` | text | Category name | -|
|` Alias ` | text | Category alias (one-word only) | -|
|` Color` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | -|

## `param_places_2d.txt`
 - **Description**: Table of places parameters and initial conditions;
 - **Source**: imported by user;
 - **File sample**: [param_places_2d.txt](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_places_2d.txt);
 - **Format**: Data Table;
 - **Formating example**:
```
Id; Trait;   C;     Name; Alias; Color
 0;     0; 0.0; Outdoors;    P0; white
 1;    10; 0.1;  Place 1;    P1;  blue
 2;     1; 0.1;  Place 2;    P2;  blue
 3;     1; 0.1;  Place 3;    P3;  blue
 4;     9; 0.1;  Place 4;    P4;  blue
 5;     6; 0.1;  Place 5;    P5;  blue
 6;     7; 0.1;  Place 6;    P6;  blue
 7;     7; 0.1;  Place 7;    P7;  blue
 8;     4; 0.1;  Place 8;    P8;  blue
 9;     9; 0.1;  Place 9;    P9;  blue
10;     3; 0.2; Place 10;   P10;  blue
11;     4; 0.2; Place 11;   P11;  blue
12;     3; 0.2; Place 12;   P12;  blue
13;     9; 0.2; Place 13;   P13;  blue
14;     3; 0.2; Place 14;   P14;  blue
15;     5; 0.2; Place 15;   P15;  blue
16;     2; 0.2; Place 16;   P16;  blue
17;     9; 0.2; Place 17;   P17;  blue
18;     4; 0.2; Place 18;   P18;  blue
19;     4; 0.2; Place 19;   P19;  blue
20;     7; 0.2; Place 20;   P20;  blue
21;    10; 0.2; Place 21;   P21;  blue
22;     1; 0.2; Place 22;   P22;  blue
23;     7; 0.2; Place 23;   P23;  blue
24;     3; 0.2; Place 24;   P24;  blue
25;     7; 0.2; Place 25;   P25;  blue
26;     2; 0.2; Place 26;   P26;  blue
27;     5; 0.2; Place 27;   P27;  blue
28;     5; 0.2; Place 28;   P28;  blue
29;     7; 0.2; Place 29;   P29;  blue
30;     9; 0.2; Place 30;   P30;  blue
31;     2; 0.2; Place 31;   P31;  blue
32;     6; 0.2; Place 32;   P32;  blue
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Id ` | unique integer number | Category numerical identifyier | -|
|` Trait ` | positive real number | Trait orientation value | trait units|
|` C ` | positive real number | Agent or Place openness to contamination, degree of interaction influence | -|
|` Name ` | text | Category name | -|
|` Alias ` | text | Category alias (one-word only) | -|
|` Color` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | -|

## `map_places_2d.asc`
 - **Description**: Map of places IDs;
 - **Source**: imported by user;
 - **File sample**: [map_places_2d.asc](https://github.com/ipo-exe/abm-cue/blob/main/samples/map_places_2d.asc);
 - **Format**: Raster Map;
 - **Formating example**:
```
ncols        95
nrows        77 
xllcorner    639958.57
yllcorner    6699796.10
cellsize     30.0
NODATA_value -1
5 5 5 5 5 5 5 5 5 5 5 3 3 3 ... 3 3 3 3 3 3 3 3 3 3 3 3 3 4
5 5 5 5 5 5 5 5 5 5 5 3 3 3 ... 3 3 3 3 3 3 3 3 3 3 3 4 4 4
                            ...  
5 5 5 5 5 5 5 5 5 5 5 3 3 3 ... 3 3 3 3 3 3 3 3 3 3 3 4 4 3
5 5 5 5 5 5 5 5 5 5 5 3 3 3 ... 3 3 3 3 3 3 3 3 3 3 3 3 3 3

```
> See the Raster preparation tutorial
 - **Requirements**:
	 - Rows and columns must match the same size of other related raster maps;
	 - CRS must be projected (coordinates in meters);
	 - Grid cells must be squared;
	 - All grid cells must be filled with values;
	 - Default No-Data cell value: `-1`;

## `param_simulation_1d.txt`
 - **Description**: Table of simulation parameters;
 - **Source**: imported by user;
 - **File sample**: [param_simulation_1d.txt](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_simulation_1d.txt);
 - **Format**: Data Table;
 - **Formating example**:
```
     Metadata;                                                      Value
    Timestamp;                                     2022/12/21 19:34:46.27
 Input Folder;                     C:/000_myFiles/myCodes/abm-cue/samples
   Run Folder;                                                     C:/bin
  Places File; C:/000_myFiles/myCodes/abm-cue/samples/param_places_1d.txt
  Agents File; C:/000_myFiles/myCodes/abm-cue/samples/param_agents_1d.txt
        Steps;                                                        100
    Weighting;                                                     Linear
Return Agents;                                                       True
   Trace Back;                                                       True
   Plot Steps;                                                       True
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Metadata ` | text | Name of metadata | -|
|` Value` | miscellaneus | Value of data | -|

## `param_simulation_2d.txt`
 - **Description**: Table of simulation parameters;
 - **Source**: imported by user;
 - **File sample**: [param_simulation_2d.txt](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_simulation_2d.txt);
 - **Format**: Data Table;
 - **Formating example**:
```
     Metadata;                                                      Value
    Timestamp;                                     2022/08/25 16:48:07.86
 Input Folder;                     C:/000_myFiles/myCodes/abm-cue/samples
   Run Folder;                                                     C:/bin
   Places Map;   C:/000_myFiles/myCodes/abm-cue/samples/map_places_2d.asc
  Places File; C:/000_myFiles/myCodes/abm-cue/samples/param_places_2d.txt
  Agents File; C:/000_myFiles/myCodes/abm-cue/samples/param_agents_2d.txt
        Steps;                                                        100
    Weighting;                                                     Linear
Return Agents;                                                      False
   Trace Back;                                                       True
   Plot Steps;                                                       True
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Metadata ` | text | Name of metadata | -|
|` Value` | miscellaneus | Value of data | -|

## `param_simulation_network_2d.txt`
 - **Description**: Table of simulation parameters;
 - **Source**: imported by user;
 - **File sample**: [param_simulation_network_2d.txt](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_simulation_network_2d.txt);
 - **Format**: Data Table;
 - **Formating example**:
```
     Metadata;                                    Value
    Timestamp;                   2022/08/25 16:48:07.86
 Input Folder;                        ./demo/benchmark1
   Run Folder;                                   C:/bin
   Places Map;         ./demo/benchmark1/benchmark1.asc
  Places File;  ./demo/benchmark1/benchmark1_places.txt
  Agents File;  ./demo/benchmark1/benchmark1_agents.txt
   Nodes File;   ./demo/benchmark1/benchmark1_nodes.txt
 Network File; ./demo/benchmark1/benchmark1_network.txt
        Steps;                                      100
    Weighting;                                   Linear
Return Agents;                                    False
   Trace Back;                                     True
   Plot Steps;                                     True
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Metadata ` | text | Name of metadata | -|
|` Value` | miscellaneus | Value of data | -|

## `param_batch_simulation.txt`
 - **Description**: Table for batch simulation parameters by changing Agents parameters. Parameters keywords: D, R, M and C. The first two rows of the table is taken;
 - **Source**: imported by user;
 - **File sample**: [param_batch_simulation.txt](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_batch_simulation.txt);
 - **Format**: Data Table;
 - **Formating example**:
```
Parameter; Min; Max; Grid
        D;  20;  40;   10
        R;   5;  50;   10
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Parameter ` | text | Name of variable set as a parameter in the sensitivity analysis | -|
|` Min ` | positive real number | Keyword for `Minimum` | -|
|` Max ` | positive real number | Keyword for `Maximum` | -|
|` Grid` | positive integer number | Number of segments for sampling the parameter space | -|

# Output files
These files are generated by the program. Note that the user may source it as input to other processes.

|File | Source | Format|
|:--- | :--- | :---|
|[nodes_2d.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#nodes_2dtxt) | process output | Data Table|
|[network_2d.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#network_2dtxt) | process output | Data Table|
|[param_agents_1d_start.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_agents_1d_starttxt) | process output | Data Table|
|[param_agents_1d_end.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_agents_1d_endtxt) | process output | Data Table|
|[param_places_1d_start.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_places_1d_starttxt) | process output | Data Table|
|[param_places_1d_end.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_places_1d_endtxt) | process output | Data Table|
|[param_agents_2d_start.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_agents_2d_starttxt) | process output | Data Table|
|[param_agents_2d_end.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_agents_2d_endtxt) | process output | Data Table|
|[param_places_2d_start.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_places_2d_starttxt) | process output | Data Table|
|[param_places_2d_end.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_places_2d_endtxt) | process output | Data Table|
|[hist_agents_start.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#hist_agents_starttxt) | process output | Data Table|
|[hist_agents_end.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#hist_agents_endtxt) | process output | Data Table|
|[hist_places_start.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#hist_places_starttxt) | process output | Data Table|
|[hist_places_end.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#hist_places_endtxt) | process output | Data Table|
|[traced_agents_traits.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#traced_agents_traitstxt) | process output | Time Series|
|[traced_agents_x.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#traced_agents_xtxt) | process output | Time Series|
|[traced_agents_xy.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#traced_agents_xytxt) | process output | Time Series|
|[traced_places_traits.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#traced_places_traitstxt) | process output | Time Series|
|[analyst_start_end.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#analyst_start_endtxt) | process output | Data Table|

## `nodes_2d.txt`
 - **Description**: Table of nodes in the Map of Places;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Id_node ` | unique integer number | Category numerical identifyier of Nodes | -|
|` y ` | positive integer number | Position coordinate in the y axis | cell units|
|` x ` | positive integer number | Position coordinate in the x axis | cell units|
|` Id_place ` | unique integer number | Category numerical identifyier of Place in Network | -|
|` Geom` | text | Feature geometry encoded in Well Known Text | -|

## `network_2d.txt`
 - **Description**: Table of topological network of nodes in the Map of Places;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|` Id_node_src ` | unique integer number | Category numerical identifyier of Source Node in Network | -|
|` Id_node_dst ` | unique integer number | Category numerical identifyier of Destiny Node in Network | -|
|` Euclidean ` | positive real number | Euclidean distance | map units|
|` AStar ` | positive real number | Non-euclidean distance computed by the A-Star algorithm | map units|
|` Id_place_src ` | unique integer number | Category numerical identifyier of Source Place in Network | -|
|` Id_place_dst ` | unique integer number | Category numerical identifyier of Destiny Place in Network | -|
|` Geom` | text | Feature geometry encoded in Well Known Text | -|

## `param_agents_1d_start.txt`
 - **Description**: Table of agents parameters and initial conditions;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
```
Id;  x; Trait;  D; R; M;    C;    Name; Alias;  Color
 1;  5;  20.0; 20; 5; 1;  0.0; Agent A;   AgA;    red
 2; 10;  20.0; 20; 5; 1;  0.0; Agent B;   AgB;   blue
 3; 15;   1.0; 20; 5; 1; 0.01; Agent C;   AgC; orange
 4; 20;   1.0; 20; 3; 1; 0.01; Agent C;   AgC; orange
 5; 25;   1.0; 20; 3; 1; 0.01; Agent C;   AgC; orange
 6; 30;   1.0; 20; 3; 1; 0.01; Agent C;   AgC; orange
 7; 35;   1.0; 20; 3; 1; 0.01; Agent C;   AgC; orange
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Id ` | unique integer number | Category numerical identifyier | -|
|` x ` | positive integer number | Position coordinate in the x axis | cell units|
|` Trait ` | positive real number | Trait orientation value | trait units|
|` D ` | positive real number | Critical Hamming Distance of trait orientation for agent-place interaction | -|
|` R ` | positive integer number | Critical radius distance for agent movement. | cell units|
|` M ` | positive integer number | Agent memory lag time. | step units|
|` C` | positive real number | Agent or Place openness to contamination, degree of interaction influence | -|

## `param_agents_1d_end.txt`
 - **Description**: Table of agents parameters and final conditions;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
```
Id;  x;              Trait;  D; R; M;    C;    Name; Alias;  Color
 1;  8;               20.0; 20; 5; 1;  0.0; Agent A;   AgA;    red
 2;  2;               20.0; 20; 5; 1;  0.0; Agent B;   AgB;   blue
 3; 24; 2.0169052053126433; 20; 5; 1; 0.01; Agent C;   AgC; orange
 4; 37;  2.796720743555842; 20; 3; 1; 0.01; Agent C;   AgC; orange
 5; 35;  2.398801065834344; 20; 3; 1; 0.01; Agent C;   AgC; orange
 6; 11; 2.3202020984591623; 20; 3; 1; 0.01; Agent C;   AgC; orange
 7; 24;  2.223469829024803; 20; 3; 1; 0.01; Agent C;   AgC; orange
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Id ` | unique integer number | Category numerical identifyier | -|
|` x ` | positive integer number | Position coordinate in the x axis | cell units|
|` Trait ` | positive real number | Trait orientation value | trait units|
|` D ` | positive real number | Critical Hamming Distance of trait orientation for agent-place interaction | -|
|` R ` | positive integer number | Critical radius distance for agent movement. | cell units|
|` M ` | positive integer number | Agent memory lag time. | step units|
|` C` | positive real number | Agent or Place openness to contamination, degree of interaction influence | -|

## `param_places_1d_start.txt`
 - **Description**: Table of places parameters and initial conditions;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
```
Id;  x; Trait;   C;    Name; Alias; Color
 1;  0;   5.0; 0.1; Place A;    PA;  blue
 2;  1;   5.0; 0.1; Place A;    PA;  blue
 3;  2;   5.0; 0.1; Place A;    PA;  blue
 4;  3;   5.0; 0.1; Place A;    PA;  blue
 5;  4;   5.0; 0.1; Place A;    PA;  blue
 6;  5;   5.0; 0.1; Place A;    PA;  blue
 7;  6;   5.0; 0.1; Place A;    PA;  blue
 8;  7;   5.0; 0.1; Place A;    PA;  blue
 9;  8;   5.0; 0.1; Place A;    PA;  blue
10;  9;   5.0; 0.1; Place A;    PA;  blue
11; 10;   5.0; 0.1; Place A;    PA;  blue
12; 11;   5.0; 0.1; Place A;    PA;  blue
13; 12;   5.0; 0.1; Place A;    PA;  blue
14; 13;   5.0; 0.1; Place A;    PA;  blue
15; 14;   5.0; 0.1; Place A;    PA;  blue
16; 15;   5.0; 0.1; Place A;    PA;  blue
17; 16;   5.0; 0.1; Place A;    PA;  blue
18; 17;   5.0; 0.1; Place A;    PA;  blue
19; 18;   5.0; 0.1; Place A;    PA;  blue
20; 19;   5.0; 0.1; Place A;    PA;   red
21; 20;   5.0; 0.1; Place B;    PB;   red
22; 21;   5.0; 0.1; Place B;    PB;   red
23; 22;   5.0; 0.1; Place B;    PB;   red
24; 23;   5.0; 0.1; Place B;    PB;   red
25; 24;   5.0; 0.1; Place B;    PB;   red
26; 25;   5.0; 0.1; Place B;    PB;   red
27; 26;   5.0; 0.1; Place B;    PB;   red
28; 27;   5.0; 0.1; Place B;    PB;   red
29; 28;   5.0; 0.1; Place B;    PB;   red
30; 29;   5.0; 0.1; Place B;    PB;   red
31; 30;   5.0; 0.1; Place B;    PB;   red
32; 31;   5.0; 0.1; Place B;    PB;   red
33; 32;   5.0; 0.1; Place B;    PB;   red
34; 33;   5.0; 0.1; Place B;    PB;   red
35; 34;   5.0; 0.1; Place B;    PB;   red
36; 35;   5.0; 0.1; Place B;    PB;   red
37; 36;   5.0; 0.1; Place B;    PB;   red
38; 37;   5.0; 0.1; Place B;    PB;   red
39; 38;   5.0; 0.1; Place B;    PB;   red
40; 39;   5.0; 0.1; Place B;    PB;   red
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Id ` | unique integer number | Category numerical identifyier | -|
|` x ` | positive integer number | Position coordinate in the x axis | cell units|
|` Trait ` | positive real number | Trait orientation value | trait units|
|` C` | positive real number | Agent or Place openness to contamination, degree of interaction influence | -|

## `param_places_1d_end.txt`
 - **Description**: Table of places parameters and final conditions;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
```
Id;  x;              Trait;   C;    Name; Alias; Color
 1;  0; 10.263800082090642; 0.1; Place A;    PA;  blue
 2;  1;  5.615619196714282; 0.1; Place A;    PA;  blue
 3;  2; 10.880599978926014; 0.1; Place A;    PA;  blue
 4;  3; 14.166679910097368; 0.1; Place A;    PA;  blue
 5;  4;   3.76852651781194; 0.1; Place A;    PA;  blue
 6;  5;   4.76813068656856; 0.1; Place A;    PA;  blue
 7;  6; 15.220537734344639; 0.1; Place A;    PA;  blue
 8;  7;  5.689908229995313; 0.1; Place A;    PA;  blue
 9;  8; 12.046071819367574; 0.1; Place A;    PA;  blue
10;  9; 11.532891049193335; 0.1; Place A;    PA;  blue
11; 10; 14.007980010051345; 0.1; Place A;    PA;  blue
12; 11;  5.967074257880513; 0.1; Place A;    PA;  blue
13; 12; 4.7017195720738965; 0.1; Place A;    PA;  blue
14; 13; 13.119901912531992; 0.1; Place A;    PA;  blue
15; 14; 3.2029617157139763; 0.1; Place A;    PA;  blue
16; 15;   2.48266136439564; 0.1; Place A;    PA;  blue
17; 16; 2.9595956975553954; 0.1; Place A;    PA;  blue
18; 17;  2.434647374836465; 0.1; Place A;    PA;  blue
19; 18; 2.6396673172610168; 0.1; Place A;    PA;  blue
20; 19;  3.516466708974913; 0.1; Place A;    PA;   red
21; 20;  2.373013801520825; 0.1; Place B;    PB;   red
22; 21;  3.506984592714363; 0.1; Place B;    PB;   red
23; 22;  3.479338239310509; 0.1; Place B;    PB;   red
24; 23;  3.276042483035429; 0.1; Place B;    PB;   red
25; 24; 2.6639556252378638; 0.1; Place B;    PB;   red
26; 25;  2.927880206017587; 0.1; Place B;    PB;   red
27; 26;  3.182037172794281; 0.1; Place B;    PB;   red
28; 27;  2.706355356475567; 0.1; Place B;    PB;   red
29; 28; 3.7751118317145003; 0.1; Place B;    PB;   red
30; 29;  4.209700132645874; 0.1; Place B;    PB;   red
31; 30;  4.428281075976054; 0.1; Place B;    PB;   red
32; 31;  4.258210411309325; 0.1; Place B;    PB;   red
33; 32;  4.722995685621642; 0.1; Place B;    PB;   red
34; 33;  4.422457922058943; 0.1; Place B;    PB;   red
35; 34;  5.617980113414946; 0.1; Place B;    PB;   red
36; 35;   5.05020974967109; 0.1; Place B;    PB;   red
37; 36;  7.014833644714424; 0.1; Place B;    PB;   red
38; 37;  3.215454677777739; 0.1; Place B;    PB;   red
39; 38;  5.463058117621738; 0.1; Place B;    PB;   red
40; 39;  11.18441397395982; 0.1; Place B;    PB;   red
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Id ` | unique integer number | Category numerical identifyier | -|
|` x ` | positive integer number | Position coordinate in the x axis | cell units|
|` Trait ` | positive real number | Trait orientation value | trait units|
|` C` | positive real number | Agent or Place openness to contamination, degree of interaction influence | -|

## `param_agents_2d_start.txt`
 - **Description**: Table of agents parameters and initial conditions;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Id ` | unique integer number | Category numerical identifyier | -|
|` x ` | positive integer number | Position coordinate in the x axis | cell units|
|` y ` | positive integer number | Position coordinate in the y axis | cell units|
|` Trait ` | positive real number | Trait orientation value | trait units|
|` D ` | positive real number | Critical Hamming Distance of trait orientation for agent-place interaction | -|
|` R ` | positive integer number | Critical radius distance for agent movement. | cell units|
|` M ` | positive integer number | Agent memory lag time. | step units|
|` C` | positive real number | Agent or Place openness to contamination, degree of interaction influence | -|

## `param_agents_2d_end.txt`
 - **Description**: Table of agents parameters and final conditions;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Id ` | unique integer number | Category numerical identifyier | -|
|` x ` | positive integer number | Position coordinate in the x axis | cell units|
|` y ` | positive integer number | Position coordinate in the y axis | cell units|
|` Trait ` | positive real number | Trait orientation value | trait units|
|` D ` | positive real number | Critical Hamming Distance of trait orientation for agent-place interaction | -|
|` R ` | positive integer number | Critical radius distance for agent movement. | cell units|
|` M ` | positive integer number | Agent memory lag time. | step units|
|` C` | positive real number | Agent or Place openness to contamination, degree of interaction influence | -|

## `param_places_2d_start.txt`
 - **Description**: Table of places parameters and initial conditions;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Id ` | unique integer number | Category numerical identifyier | -|
|` Trait ` | positive real number | Trait orientation value | trait units|
|` C` | positive real number | Agent or Place openness to contamination, degree of interaction influence | -|

## `param_places_2d_end.txt`
 - **Description**: Table of places parameters and final conditions;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Id ` | unique integer number | Category numerical identifyier | -|
|` Trait ` | positive real number | Trait orientation value | trait units|
|` C` | positive real number | Agent or Place openness to contamination, degree of interaction influence | -|

## `hist_agents_start.txt`
 - **Description**: Histogram table of agents on initial conditions;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
```
Trait; Count
  1.0;     0
  2.0;     2
  3.0;     0
  4.0;     0
  5.0;     0
  6.0;     0
  7.0;     0
  8.0;     0
  9.0;     0
 10.0;     0
 11.0;     0
 12.0;     0
 13.0;     0
 14.0;     0
 15.0;     0
 16.0;     0
 17.0;     0
 18.0;     0
 19.0;     0
 20.0;     2
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Trait ` | positive real number | Trait orientation value | trait units|
|` Count` | positive integer number | Keyword for `Counting` | -|
 - **Data view**:

![hist_agents_start](https://github.com/ipo-exe/abm-cue/blob/main/samples/view_hist_agents_start.png "hist_agents_start")

## `hist_agents_end.txt`
 - **Description**: Histogram table of agents on final conditions;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
```
Trait; Count
  1.0;     0
  2.0;     0
  3.0;     0
  4.0;     0
  5.0;     2
  6.0;     0
  7.0;     0
  8.0;     0
  9.0;     0
 10.0;     0
 11.0;     0
 12.0;     0
 13.0;     0
 14.0;     0
 15.0;     0
 16.0;     0
 17.0;     0
 18.0;     0
 19.0;     0
 20.0;     2
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Trait ` | positive real number | Trait orientation value | trait units|
|` Count` | positive integer number | Keyword for `Counting` | -|
 - **Data view**:

![hist_agents_end](https://github.com/ipo-exe/abm-cue/blob/main/samples/view_hist_agents_end.png "hist_agents_end")

## `hist_places_start.txt`
 - **Description**: Histogram table places of placess on initial conditions;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
```
Trait; Count
  1.0;     0
  2.0;     0
  3.0;     0
  4.0;     0
  5.0;     0
  6.0;    40
  7.0;     0
  8.0;     0
  9.0;     0
 10.0;     0
 11.0;     0
 12.0;     0
 13.0;     0
 14.0;     0
 15.0;     0
 16.0;     0
 17.0;     0
 18.0;     0
 19.0;     0
 20.0;     0
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Trait ` | positive real number | Trait orientation value | trait units|
|` Count` | positive integer number | Keyword for `Counting` | -|
 - **Data view**:

![hist_places_start](https://github.com/ipo-exe/abm-cue/blob/main/samples/view_hist_places_start.png "hist_places_start")

## `hist_places_end.txt`
 - **Description**: Histogram table places of places on final conditions;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
```
Trait; Count
  1.0;     0
  2.0;     0
  3.0;     0
  4.0;     2
  5.0;     7
  6.0;     4
  7.0;     3
  8.0;     4
  9.0;     4
 10.0;     6
 11.0;     2
 12.0;     0
 13.0;     2
 14.0;     1
 15.0;     2
 16.0;     1
 17.0;     1
 18.0;     0
 19.0;     1
 20.0;     0
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Trait ` | positive real number | Trait orientation value | trait units|
|` Count` | positive integer number | Keyword for `Counting` | -|
 - **Data view**:

![hist_places_end](https://github.com/ipo-exe/abm-cue/blob/main/samples/view_hist_places_end.png "hist_places_end")

## `traced_agents_traits.txt`
 - **Description**: Time series table of agents traits;
 - **Source**: process output;
 - **Format**: Time Series;
 - **Formating example**:
```
Step; A_1_Trait; A_2_Trait; A_3_Trait; A_4_Trait; A_5_Trait; A_6_Trait; A_7_Trait;          H
   0;      20.0;      20.0;       1.0;       1.0;       1.0;       1.0;       1.0; 0.86312056
   1;      20.0;      20.0;  1.039604; 1.0360036;  1.039604; 1.0360036;  1.039604; 0.86312056
   2;      20.0;      20.0; 1.0788158; 1.0752511; 1.0788158; 1.0752511; 1.0788158; 0.86312056
   3;      20.0;      20.0; 1.1176394;   1.11411; 1.1176394;  1.110542; 1.1176394; 0.86312056
   4;      20.0;      20.0; 1.1525106; 1.1490515; 1.1525139; 1.1454868;  1.149337; 0.86312056
   5;      20.0;      20.0; 1.1906046; 1.1804706; 1.1838727;  1.180121; 1.1778394; 0.86312056
   6;      20.0;      20.0; 1.2652549; 1.2087224; 1.2120702; 1.2057272; 1.2011404; 0.86312056
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
	 - Time resolution: daily timesteps;
	 - Date format: `YYYY-MM-DD` (example: `2022-01-29`);
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Step ` | positive integer number | Time step number | -|
|` A_Id_Trait ` | positive real number | Trait orientation of Agent A_Id (ex: A_12_Trait) | trait units|
|` H` | real number | Shannon Entropy | Bits|
 - **Data view**:

![traced_agents_traits](https://github.com/ipo-exe/abm-cue/blob/main/samples/view_traced_agents_traits.png "traced_agents_traits")

## `traced_agents_x.txt`
 - **Description**: Time series table of agents positions;
 - **Source**: process output;
 - **Format**: Time Series;
 - **Formating example**:
```
Step; A_1_x; A_2_x; A_3_x; A_4_x; A_5_x; A_6_x; A_7_x
   0;   5.0;  10.0;  15.0;  20.0;  25.0;  30.0;  35.0
   1;   8.0;  10.0;  19.0;  19.0;  27.0;  27.0;  37.0
   2;  10.0;  11.0;  12.0;  17.0;  26.0;  29.0;  32.0
   3;   4.0;  12.0;  20.0;  22.0;  24.0;  29.0;  33.0
   4;   3.0;   8.0;  17.0;  22.0;  26.0;  32.0;  32.0
   5;   6.0;  10.0;  16.0;  22.0;  26.0;  33.0;  32.0
   6;   6.0;  11.0;  10.0;  22.0;  26.0;  32.0;  32.0
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
	 - Time resolution: daily timesteps;
	 - Date format: `YYYY-MM-DD` (example: `2022-01-29`);
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Step ` | positive integer number | Time step number | -|
|` A_Id_x` | positive integer number | Position coordinate in the x axis of Agent A_Id (ex: A_12_x) | cell units|
 - **Data view**:

![traced_agents_x](https://github.com/ipo-exe/abm-cue/blob/main/samples/view_traced_agents_x.png "traced_agents_x")

## `traced_agents_xy.txt`
 - **Description**: Time series table of agents positions;
 - **Source**: process output;
 - **Format**: Time Series;
 - **Formating example**:
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
	 - Time resolution: daily timesteps;
	 - Date format: `YYYY-MM-DD` (example: `2022-01-29`);
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Step ` | positive integer number | Time step number | -|
|` A_Id_x ` | positive integer number | Position coordinate in the x axis of Agent A_Id (ex: A_12_x) | cell units|
|` A_Id_y` | positive integer number | Position coordinate in the y axis of Agent A_Id (ex: A_12_y) | cell units|

## `traced_places_traits.txt`
 - **Description**: Time series table of places traits;
 - **Source**: process output;
 - **Format**: Time Series;
 - **Formating example**:
```
Step; P_1_Trait; P_2_Trait; P_3_Trait; P_4_Trait; P_5_Trait; P_6_Trait; P_7_Trait; P_8_Trait; P_9_Trait; P_10_Trait; P_11_Trait; P_12_Trait; P_13_Trait; P_14_Trait; P_15_Trait; P_16_Trait; P_17_Trait; P_18_Trait; P_19_Trait; P_20_Trait; P_21_Trait; P_22_Trait; P_23_Trait; P_24_Trait; P_25_Trait; P_26_Trait; P_27_Trait; P_28_Trait; P_29_Trait; P_30_Trait; P_31_Trait; P_32_Trait; P_33_Trait; P_34_Trait; P_35_Trait; P_36_Trait; P_37_Trait; P_38_Trait; P_39_Trait; P_40_Trait;          H
   0;       5.0;       5.0;       5.0;       5.0;       5.0;       5.0;       5.0;       5.0;       5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;       -0.0
   1;       5.0;       5.0;       5.0;       5.0;       5.0;       5.0;       5.0;       5.0; 6.3636365;        5.0;  6.3636365;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;   4.305785;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;   4.305785;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;  4.6363635;        5.0;        5.0; 0.66493326
   2;       5.0;       5.0;       5.0;       5.0;       5.0;       5.0;       5.0;       5.0; 6.3636365;        5.0;   7.603306;  6.3636365;   4.639964;        5.0;        5.0;        5.0;        5.0;  4.6396365;        5.0;   4.305785;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;   4.639964;   4.305785;        5.0;  4.6396365;        5.0;        5.0;   4.639964;        5.0;        5.0;        5.0;        5.0;  4.6363635;        5.0;        5.0;  1.1498919
   3;       5.0;       5.0;       5.0;       5.0; 6.3636365;       5.0;       5.0;       5.0; 6.3636365;        5.0;   7.603306;  6.3636365;  6.0363307;        5.0;        5.0;        5.0;        5.0;  4.6396365;        5.0;   4.305785;   4.643529;        5.0;  4.6432047;        5.0;   4.643529;        5.0;   4.639964;   4.305785;        5.0;   4.315602;        5.0;        5.0;   4.639964;   4.643529;        5.0;        5.0;        5.0;  4.6363635;        5.0;        5.0;  1.4196069
   4;       5.0;       5.0;       5.0; 6.3636365; 6.3636365;       5.0;       5.0;       5.0;  7.603306;        5.0;   7.603306;  6.3636365;  6.0363307;        5.0;        5.0;        5.0;        5.0;   4.319455;        5.0;   4.305785;   4.643529;        5.0;  4.3223777;        5.0;   4.643529;        5.0;  4.3197527;   4.305785;        5.0;   4.315602;        5.0;        5.0;  4.0280647;   4.643529;        5.0;        5.0;        5.0;  4.6363635;        5.0;        5.0;  1.5195363
   5;       5.0;       5.0;       5.0; 6.3636365; 6.3636365;       5.0; 6.3636365;       5.0;  7.603306;        5.0;   8.730278;  6.3636365;  6.0363307;        5.0;        5.0;        5.0;   4.650228;   4.319455;        5.0;   4.305785;   4.643529;        5.0;  4.0338936;        5.0;   4.643529;        5.0;  4.0318217;   4.305785;        5.0;   4.315602;        5.0;        5.0;  3.7663624;   4.325525;        5.0;        5.0;        5.0;  4.6363635;        5.0;        5.0;  1.7743767
   6;       5.0;       5.0;       5.0; 6.3636365; 6.3636365;       5.0;  7.603306;       5.0;  7.603306;        5.0;   8.044853;   7.603306;  6.0363307;        5.0;        5.0;        5.0;   4.650228;   4.319455;        5.0;   4.305785;   4.643529;        5.0;  3.7744915;        5.0;   4.643529;        5.0;  3.7729175;   4.305785;        5.0;   4.315602;        5.0;        5.0;  3.3173032;   4.325525;        5.0;        5.0;        5.0;  4.6363635;        5.0;        5.0;  1.9461118
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
	 - Time resolution: daily timesteps;
	 - Date format: `YYYY-MM-DD` (example: `2022-01-29`);
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Step ` | positive integer number | Time step number | -|
|` P_Id_Trait ` | positive integer number | Trait orientation of Place P_Id (ex: P_10_Trait) | trait units|
|` H` | real number | Shannon Entropy | Bits|
 - **Data view**:

![traced_places_traits](https://github.com/ipo-exe/abm-cue/blob/main/samples/view_traced_places_traits.png "traced_places_traits")

## `analyst_start_end.txt`
 - **Description**: Table of Start-End analysis of Shannon Entropy;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
```
 Step;           H_agents;           H_places
Start;  0.863120568566631;               -0.0
  End; 1.3787834934861753; 3.0199309752155794
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Step ` | positive integer number | Time step number | -|
|` H_agents ` | real number | Shannon Entropy of Agents | Bits|
|` H_places` | real number | Shannon Entropy of Places | Bits|

## Glossary

### By A-Z order
|Keyword | Data Type | Description | Units | Category|
|:--- | :--- | :--- | :--- | :---|
|`AStar` | positive real number | Non-euclidean distance computed by the A-Star algorithm | map units | field|
|`A_Id_Trait` | positive real number | Trait orientation of Agent A_Id (ex: A_12_Trait) | trait units | variable|
|`A_Id_x` | positive integer number | Position coordinate in the x axis of Agent A_Id (ex: A_12_x) | cell units | variable|
|`A_Id_y` | positive integer number | Position coordinate in the y axis of Agent A_Id (ex: A_12_y) | cell units | variable|
|`Agents File` | text | File path to the agents parameter file (ex: C:/data/param_agents.txt) | - | keyword|
|`Alias` | text | Category alias (one-word only) | - | field|
|`C` | positive real number | Agent or Place openness to contamination, degree of interaction influence | - | parameter|
|`Color` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | - | field|
|`Count` | positive integer number | Counting units | - | field|
|`Count` | positive integer number | Keyword for `Counting` | - | keyword|
|`D` | positive real number | Critical Hamming Distance of trait orientation for agent-place interaction | - | parameter|
|`Date` | date | Date of record | - | field|
|`Euclidean` | positive real number | Euclidean distance | map units | field|
|`Geom` | text | Feature geometry encoded in Well Known Text | - | field|
|`Grid` | positive integer number | Number of segments for sampling the parameter space | - | field|
|`H` | real number | Shannon Entropy | Bits | field|
|`H_agents` | real number | Shannon Entropy of Agents | Bits | field|
|`H_places` | real number | Shannon Entropy of Places | Bits | field|
|`Id` | unique integer number | Category numerical identifyier | - | field|
|`Id_node` | unique integer number | Category numerical identifyier of Nodes | - | field|
|`Id_node_dst` | unique integer number | Category numerical identifyier of Destiny Node in Network | - | field|
|`Id_node_src` | unique integer number | Category numerical identifyier of Source Node in Network | - | field|
|`Id_place` | unique integer number | Category numerical identifyier of Place in Network | - | field|
|`Id_place_dst` | unique integer number | Category numerical identifyier of Destiny Place in Network | - | field|
|`Id_place_src` | unique integer number | Category numerical identifyier of Source Place in Network | - | field|
|`Input Folder` | text | Folder path to the input data folder (ex: C:/data) | - | keyword|
|`M` | positive integer number | Agent memory lag time. | step units | parameter|
|`Max` | positive real number | Keyword for `Maximum` | - | keyword|
|`Mean` | positive real number | Keyword for `Mean` | - | keyword|
|`Med` | positive real number | Keyword for `Median` | - | keyword|
|`Metadata` | text | Name of metadata | - | field|
|`Min` | positive real number | Keyword for `Minimum` | - | keyword|
|`Name` | text | Category name | - | field|
|`P_Id_Trait` | positive integer number | Trait orientation of Place P_Id (ex: P_10_Trait) | trait units | variable|
|`P_Id_x` | positive integer number | Position coordinate in the x axis of Place P_Id (ex: P_10_x) | cell units | variable|
|`Parameter` | text | Name of variable set as a parameter in the sensitivity analysis | - | field|
|`Places File` | text | File path to the places parameter file (ex: C:/data/param_places.txt) | - | keyword|
|`R` | positive integer number | Critical radius distance for agent movement. | cell units | parameter|
|`Run Folder` | text | Folder path to the folder to store simulation outputs (ex: C:/output) | - | keyword|
|`SD` | positive real number | Keyword for `Standard Deviation` | - | keyword|
|`Stat` | text | Keyword for `statistic` | - | keyword|
|`Step` | positive integer number | Time step number | - | field|
|`Steps` | positive integer number | Number of time steps in the simulation | - | parameter|
|`Sum` | positive real number | Keyword for `sum` | - | keyword|
|`Trait` | positive real number | Trait orientation value | trait units | variable|
|`Value` | miscellaneus | Value of data | - | field|
|`p05` | positive real number | Keyword for `5% percentile` | - | keyword|
|`p95` | positive real number | Keyword for `95% percentile` | - | keyword|
|`x` | positive integer number | Position coordinate in the x axis | cell units | variable|
|`y` | positive integer number | Position coordinate in the y axis | cell units | variable|

### By category

#### Field
|Keyword | Data Type | Description | Units | Category|
|:--- | :--- | :--- | :--- | :---|
|`AStar` | positive real number | Non-euclidean distance computed by the A-Star algorithm | map units | field|
|`Alias` | text | Category alias (one-word only) | - | field|
|`Color` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | - | field|
|`Count` | positive integer number | Counting units | - | field|
|`Date` | date | Date of record | - | field|
|`Euclidean` | positive real number | Euclidean distance | map units | field|
|`Geom` | text | Feature geometry encoded in Well Known Text | - | field|
|`Grid` | positive integer number | Number of segments for sampling the parameter space | - | field|
|`H` | real number | Shannon Entropy | Bits | field|
|`H_agents` | real number | Shannon Entropy of Agents | Bits | field|
|`H_places` | real number | Shannon Entropy of Places | Bits | field|
|`Id` | unique integer number | Category numerical identifyier | - | field|
|`Id_node` | unique integer number | Category numerical identifyier of Nodes | - | field|
|`Id_node_dst` | unique integer number | Category numerical identifyier of Destiny Node in Network | - | field|
|`Id_node_src` | unique integer number | Category numerical identifyier of Source Node in Network | - | field|
|`Id_place` | unique integer number | Category numerical identifyier of Place in Network | - | field|
|`Id_place_dst` | unique integer number | Category numerical identifyier of Destiny Place in Network | - | field|
|`Id_place_src` | unique integer number | Category numerical identifyier of Source Place in Network | - | field|
|`Metadata` | text | Name of metadata | - | field|
|`Name` | text | Category name | - | field|
|`Parameter` | text | Name of variable set as a parameter in the sensitivity analysis | - | field|
|`Step` | positive integer number | Time step number | - | field|
|`Value` | miscellaneus | Value of data | - | field|

#### Variable
|Keyword | Data Type | Description | Units | Category|
|:--- | :--- | :--- | :--- | :---|
|`A_Id_Trait` | positive real number | Trait orientation of Agent A_Id (ex: A_12_Trait) | trait units | variable|
|`A_Id_x` | positive integer number | Position coordinate in the x axis of Agent A_Id (ex: A_12_x) | cell units | variable|
|`A_Id_y` | positive integer number | Position coordinate in the y axis of Agent A_Id (ex: A_12_y) | cell units | variable|
|`P_Id_Trait` | positive integer number | Trait orientation of Place P_Id (ex: P_10_Trait) | trait units | variable|
|`P_Id_x` | positive integer number | Position coordinate in the x axis of Place P_Id (ex: P_10_x) | cell units | variable|
|`Trait` | positive real number | Trait orientation value | trait units | variable|
|`x` | positive integer number | Position coordinate in the x axis | cell units | variable|
|`y` | positive integer number | Position coordinate in the y axis | cell units | variable|

#### Keyword
|Keyword | Data Type | Description | Units | Category|
|:--- | :--- | :--- | :--- | :---|
|`Agents File` | text | File path to the agents parameter file (ex: C:/data/param_agents.txt) | - | keyword|
|`Count` | positive integer number | Keyword for `Counting` | - | keyword|
|`Input Folder` | text | Folder path to the input data folder (ex: C:/data) | - | keyword|
|`Max` | positive real number | Keyword for `Maximum` | - | keyword|
|`Mean` | positive real number | Keyword for `Mean` | - | keyword|
|`Med` | positive real number | Keyword for `Median` | - | keyword|
|`Min` | positive real number | Keyword for `Minimum` | - | keyword|
|`Places File` | text | File path to the places parameter file (ex: C:/data/param_places.txt) | - | keyword|
|`Run Folder` | text | Folder path to the folder to store simulation outputs (ex: C:/output) | - | keyword|
|`SD` | positive real number | Keyword for `Standard Deviation` | - | keyword|
|`Stat` | text | Keyword for `statistic` | - | keyword|
|`Sum` | positive real number | Keyword for `sum` | - | keyword|
|`p05` | positive real number | Keyword for `5% percentile` | - | keyword|
|`p95` | positive real number | Keyword for `95% percentile` | - | keyword|

#### Parameter
|Keyword | Data Type | Description | Units | Category|
|:--- | :--- | :--- | :--- | :---|
|`C` | positive real number | Agent or Place openness to contamination, degree of interaction influence | - | parameter|
|`D` | positive real number | Critical Hamming Distance of trait orientation for agent-place interaction | - | parameter|
|`M` | positive integer number | Agent memory lag time. | step units | parameter|
|`R` | positive integer number | Critical radius distance for agent movement. | cell units | parameter|
|`Steps` | positive integer number | Number of time steps in the simulation | - | parameter|
