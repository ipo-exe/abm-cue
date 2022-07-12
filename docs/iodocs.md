# I/O documentation
 - [Imported files](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#imported-files)
 - [Output files](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#output-files)
 - [Glossary](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#glossary)

# Imported files
These files must be prepared and sourced by the user. Samples are provided for proper formatting.

|File | Source | Format | Sample|
|:--- | :--- | :--- | :---|
|[param_agents.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_agentstxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_agents.txt)|
|[param_places.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_placestxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_places.txt)|
|[param_simulation.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_simulationtxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_simulation.txt)|

## `param_agents.txt`
 - **Description**: Table of agents parameters and initial conditions;
 - **Source**: imported by user;
 - **File sample**: [param_agents.txt](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_agents.txt);
 - **Format**: Data Table;
 - **Formating example**:
```
Id;  x; Trait; Alpha; Beta;    C;    Name; Alias ;  Color
 1;  5;    20;    20;    5;  0.0; Agent A;    AgA;    red
 2; 10;    20;    20;    5;  0.0; Agent B;    AgB;   blue
 3; 15;     1;    20;    5; 0.01; Agent C;    AgC; orange
 4; 35;     1;    20;    3; 0.01; Agent C;    AgC; orange
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
|` Alpha ` | positive real number | Trait orientation threshold for agent-place interaction | -|
|` Beta ` | positive integer number | Distance threshold for agent movement. | cell units|
|` C` | positive real number | Place-to-agent degree of interaction influence (agents openness to change) | -|
 - **Optional Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Name ` | text | Category name | -|
|` Alias ` | text | Category alias (one-word only) | -|
|` Color` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | -|
 - **Data view**:

missing file

## `param_places.txt`
 - **Description**: Table of places parameters and initial conditions;
 - **Source**: imported by user;
 - **File sample**: [param_places.txt](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_places.txt);
 - **Format**: Data Table;
 - **Formating example**:
```
Id;  x; Trait;   D;    Name; Alias
 1;  0;     5; 0.1; Place A;    PA
 2;  1;     5; 0.1; Place A;    PA
 3;  2;     5; 0.1; Place A;    PA
 4;  3;     5; 0.1; Place A;    PA
 5;  4;     5; 0.1; Place A;    PA
 6;  5;     5; 0.1; Place A;    PA
 7;  6;     5; 0.1; Place A;    PA
 8;  7;     5; 0.1; Place A;    PA
 9;  8;     5; 0.1; Place A;    PA
10;  9;     5; 0.1; Place A;    PA
11; 10;     5; 0.1; Place A;    PA
12; 11;     5; 0.1; Place A;    PA
13; 12;     5; 0.1; Place A;    PA
14; 13;     5; 0.1; Place A;    PA
15; 14;     5; 0.1; Place A;    PA
16; 15;     5; 0.1; Place A;    PA
17; 16;     5; 0.1; Place A;    PA
18; 17;     5; 0.1; Place A;    PA
19; 18;     5; 0.1; Place A;    PA
20; 19;     5; 0.1; Place A;    PA
21; 20;     5; 0.1; Place B;    PB
22; 21;     5; 0.1; Place B;    PB
23; 22;     5; 0.1; Place B;    PB
24; 23;     5; 0.1; Place B;    PB
25; 24;     5; 0.1; Place B;    PB
26; 25;     5; 0.1; Place B;    PB
27; 26;     5; 0.1; Place B;    PB
28; 27;     5; 0.1; Place B;    PB
29; 28;     5; 0.1; Place B;    PB
30; 29;     5; 0.1; Place B;    PB
31; 30;     5; 0.1; Place B;    PB
32; 31;     5; 0.1; Place B;    PB
33; 32;     5; 0.1; Place B;    PB
34; 33;     5; 0.1; Place B;    PB
35; 34;     5; 0.1; Place B;    PB
36; 35;     5; 0.1; Place B;    PB
37; 36;     5; 0.1; Place B;    PB
38; 37;     5; 0.1; Place B;    PB
39; 38;     5; 0.1; Place B;    PB
40; 39;     5; 0.1; Place B;    PB
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
|` D` | positive real number | Agent-to-place degree of interaction influence (places openness to change) | -|
 - **Optional Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Name ` | text | Category name | -|
|` Alias ` | text | Category alias (one-word only) | -|
|` Color` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | -|
 - **Data view**:

missing file

## `param_simulation.txt`
 - **Description**: Table of simulation parameters;
 - **Source**: imported by user;
 - **File sample**: [param_simulation.txt](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_simulation.txt);
 - **Format**: Data Table;
 - **Formating example**:
```
     Metadata;                                                        Value
    Timestamp;                                       2022/07/12 10:31:09.36
 Input Folder;                  /home/ipora/PycharmProjects/abm-cue/samples
   Run Folder;                                    /home/ipora/Documents/bin
  Agents File; /home/ipora/PycharmProjects/abm-cue/samples/param_agents.txt
  Places File; /home/ipora/PycharmProjects/abm-cue/samples/param_places.txt
        Steps;                                                          100
Return Agents;                                                        False
   Trace Back;                                                         True
 Plot Results;                                                         True
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Metadata ` | text | Name of metadata | -|
|` Value` | miscellaneus | Value of data | -|
 - **Data view**:

missing file

# Output files
These files are generated by the program. Note that the user may source it as input to other processes.

|File | Source | Format|
|:--- | :--- | :---|
|[param_agents_start.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_agents_starttxt) | process output | Data Table|
|[param_agents_end.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_agents_endtxt) | process output | Data Table|
|[param_places_start.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_places_starttxt) | process output | Data Table|
|[param_places_end.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_places_endtxt) | process output | Data Table|
|[hist_agents_start.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#hist_agents_starttxt) | process output | Data Table|
|[hist_agents_end.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#hist_agents_endtxt) | process output | Data Table|
|[hist_places_start.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#hist_places_starttxt) | process output | Data Table|
|[hist_places_end.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#hist_places_endtxt) | process output | Data Table|
|[traced_agents_traits.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#traced_agents_traitstxt) | process output | Time Series|
|[traced_agents_x.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#traced_agents_xtxt) | process output | Time Series|
|[traced_places_traits.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#traced_places_traitstxt) | process output | Time Series|

## `param_agents_start.txt`
 - **Description**: Table of agents parameters and initial conditions;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
```
Id;  x; Trait; Alpha; Beta;    C;    Name; Alias ;  Color
 1;  5;  20.0;    20;    5;  0.0; Agent A;    AgA;    red
 2; 10;  20.0;    20;    5;  0.0; Agent B;    AgB;   blue
 3; 15;   1.0;    20;    5; 0.01; Agent C;    AgC; orange
 4; 35;   1.0;    20;    3; 0.01; Agent C;    AgC; orange
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
|` Alpha ` | positive real number | Trait orientation threshold for agent-place interaction | -|
|` Beta ` | positive integer number | Distance threshold for agent movement. | cell units|
|` C` | positive real number | Place-to-agent degree of interaction influence (agents openness to change) | -|
 - **Data view**:

missing file

## `param_agents_end.txt`
 - **Description**: Table of agents parameters and final conditions;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
```
Id;  x;             Trait; Alpha; Beta;    C;    Name; Alias ;  Color
 1; 34;              20.0;    20;    5;  0.0; Agent A;    AgA;    red
 2; 13;              20.0;    20;    5;  0.0; Agent B;    AgB;   blue
 3; 12; 4.300367305551827;    20;    5; 0.01; Agent C;    AgC; orange
 4; 24; 4.040588456680487;    20;    3; 0.01; Agent C;    AgC; orange
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
|` Alpha ` | positive real number | Trait orientation threshold for agent-place interaction | -|
|` Beta ` | positive integer number | Distance threshold for agent movement. | cell units|
|` C` | positive real number | Place-to-agent degree of interaction influence (agents openness to change) | -|
 - **Data view**:

missing file

## `param_places_start.txt`
 - **Description**: Table of places parameters and initial conditions;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
```
Id;  x; Trait;   D;    Name; Alias
 1;  0;   5.0; 0.1; Place A;    PA
 2;  1;   5.0; 0.1; Place A;    PA
 3;  2;   5.0; 0.1; Place A;    PA
 4;  3;   5.0; 0.1; Place A;    PA
 5;  4;   5.0; 0.1; Place A;    PA
 6;  5;   5.0; 0.1; Place A;    PA
 7;  6;   5.0; 0.1; Place A;    PA
 8;  7;   5.0; 0.1; Place A;    PA
 9;  8;   5.0; 0.1; Place A;    PA
10;  9;   5.0; 0.1; Place A;    PA
11; 10;   5.0; 0.1; Place A;    PA
12; 11;   5.0; 0.1; Place A;    PA
13; 12;   5.0; 0.1; Place A;    PA
14; 13;   5.0; 0.1; Place A;    PA
15; 14;   5.0; 0.1; Place A;    PA
16; 15;   5.0; 0.1; Place A;    PA
17; 16;   5.0; 0.1; Place A;    PA
18; 17;   5.0; 0.1; Place A;    PA
19; 18;   5.0; 0.1; Place A;    PA
20; 19;   5.0; 0.1; Place A;    PA
21; 20;   5.0; 0.1; Place B;    PB
22; 21;   5.0; 0.1; Place B;    PB
23; 22;   5.0; 0.1; Place B;    PB
24; 23;   5.0; 0.1; Place B;    PB
25; 24;   5.0; 0.1; Place B;    PB
26; 25;   5.0; 0.1; Place B;    PB
27; 26;   5.0; 0.1; Place B;    PB
28; 27;   5.0; 0.1; Place B;    PB
29; 28;   5.0; 0.1; Place B;    PB
30; 29;   5.0; 0.1; Place B;    PB
31; 30;   5.0; 0.1; Place B;    PB
32; 31;   5.0; 0.1; Place B;    PB
33; 32;   5.0; 0.1; Place B;    PB
34; 33;   5.0; 0.1; Place B;    PB
35; 34;   5.0; 0.1; Place B;    PB
36; 35;   5.0; 0.1; Place B;    PB
37; 36;   5.0; 0.1; Place B;    PB
38; 37;   5.0; 0.1; Place B;    PB
39; 38;   5.0; 0.1; Place B;    PB
40; 39;   5.0; 0.1; Place B;    PB
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
|` D` | positive real number | Agent-to-place degree of interaction influence (places openness to change) | -|
 - **Data view**:

missing file

## `param_places_end.txt`
 - **Description**: Table of places parameters and final conditions;
 - **Source**: process output;
 - **Format**: Data Table;
 - **Formating example**:
```
Id;  x;              Trait;   D;    Name; Alias
 1;  0;  5.414165230996299; 0.1; Place A;    PA
 2;  1;   6.98635141334472; 0.1; Place A;    PA
 3;  2; 14.752933246345897; 0.1; Place A;    PA
 4;  3; 12.536042956640964; 0.1; Place A;    PA
 5;  4;  8.995569328528745; 0.1; Place A;    PA
 6;  5;  4.962942010646876; 0.1; Place A;    PA
 7;  6;  8.394079590459404; 0.1; Place A;    PA
 8;  7;  7.488562910007846; 0.1; Place A;    PA
 9;  8;  9.638537727789052; 0.1; Place A;    PA
10;  9; 12.728270756222434; 0.1; Place A;    PA
11; 10;  3.903013330552041; 0.1; Place A;    PA
12; 11; 14.386719412197335; 0.1; Place A;    PA
13; 12;  9.022765376781873; 0.1; Place A;    PA
14; 13; 16.050031185408788; 0.1; Place A;    PA
15; 14; 15.102062894329176; 0.1; Place A;    PA
16; 15;  7.585665937173897; 0.1; Place A;    PA
17; 16;  7.324003759747553; 0.1; Place A;    PA
18; 17;  4.919325642777743; 0.1; Place A;    PA
19; 18;  9.163935269943732; 0.1; Place A;    PA
20; 19;  9.240384075260994; 0.1; Place A;    PA
21; 20; 5.7259940502715585; 0.1; Place B;    PB
22; 21;  5.906209110137535; 0.1; Place B;    PB
23; 22;  10.49489458660072; 0.1; Place B;    PB
24; 23;  8.888642952451589; 0.1; Place B;    PB
25; 24;   4.54961826233062; 0.1; Place B;    PB
26; 25;  5.670714910441478; 0.1; Place B;    PB
27; 26;  9.862154509837739; 0.1; Place B;    PB
28; 27;  4.431043332383357; 0.1; Place B;    PB
29; 28;  9.141778725950623; 0.1; Place B;    PB
30; 29;  4.970479911078091; 0.1; Place B;    PB
31; 30;  4.667607055484053; 0.1; Place B;    PB
32; 31; 10.263800082090642; 0.1; Place B;    PB
33; 32;  4.302994543788251; 0.1; Place B;    PB
34; 33;  6.977218067994902; 0.1; Place B;    PB
35; 34; 13.313464050745093; 0.1; Place B;    PB
36; 35; 3.3504522433272856; 0.1; Place B;    PB
37; 36;  6.582482904059928; 0.1; Place B;    PB
38; 37;  7.739054432134676; 0.1; Place B;    PB
39; 38;  18.61556002734402; 0.1; Place B;    PB
40; 39;  8.672768432486476; 0.1; Place B;    PB
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
|` D` | positive real number | Agent-to-place degree of interaction influence (places openness to change) | -|
 - **Data view**:

missing file

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
Step; A_1_Trait; A_2_Trait; A_3_Trait; A_4_Trait
   0;      20.0;      20.0;       1.0;       1.0
   1;      20.0;      20.0;  1.039604;  1.039604
   2;      20.0;      20.0; 1.0788158; 1.0788158
   3;      20.0;      20.0; 1.1311407; 1.1140391
   4;      20.0;      20.0; 1.2063798; 1.1489491
   5;      20.0;      20.0; 1.2439404; 1.1870784
   6;      20.0;      20.0; 1.2775286; 1.2248302
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
|` A_Id_Trait` | positive real number | Trait orientaiton of Agent A_Id (ex: A_12_Trait) | trait units|
 - **Data view**:

![traced_agents_traits](https://github.com/ipo-exe/abm-cue/blob/main/samples/view_traced_agents_traits.png "traced_agents_traits")

## `traced_agents_x.txt`
 - **Description**: Time series table of agents positions;
 - **Source**: process output;
 - **Format**: Time Series;
 - **Formating example**:
```
Step; A_1_x; A_2_x; A_3_x; A_4_x
   0;   5.0;  10.0;  15.0;  35.0
   1;   7.0;   7.0;  13.0;  36.0
   2;  10.0;   5.0;  12.0;  37.0
   3;  15.0;   9.0;  10.0;  36.0
   4;  10.0;   7.0;   7.0;  37.0
   5;  15.0;  10.0;  11.0;  38.0
   6;  10.0;  14.0;  13.0;   0.0
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

## `traced_places_traits.txt`
 - **Description**: Time series table of places traits;
 - **Source**: process output;
 - **Format**: Time Series;
 - **Formating example**:
```
Step; P_1_Trait; P_2_Trait; P_3_Trait; P_4_Trait; P_5_Trait; P_6_Trait; P_7_Trait; P_8_Trait; P_9_Trait; P_10_Trait; P_11_Trait; P_12_Trait; P_13_Trait; P_14_Trait; P_15_Trait; P_16_Trait; P_17_Trait; P_18_Trait; P_19_Trait; P_20_Trait; P_21_Trait; P_22_Trait; P_23_Trait; P_24_Trait; P_25_Trait; P_26_Trait; P_27_Trait; P_28_Trait; P_29_Trait; P_30_Trait; P_31_Trait; P_32_Trait; P_33_Trait; P_34_Trait; P_35_Trait; P_36_Trait; P_37_Trait; P_38_Trait; P_39_Trait; P_40_Trait
   0;       5.0;       5.0;       5.0;       5.0;       5.0;       5.0;       5.0;       5.0;       5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0
   1;       5.0;       5.0;       5.0;       5.0;       5.0;       5.0;       5.0;  7.603306;       5.0;        5.0;        5.0;        5.0;        5.0;  4.6363635;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;  4.6363635;        5.0;        5.0;        5.0
   2;       5.0;       5.0;       5.0;       5.0;       5.0; 6.3636365;       5.0;  7.603306;       5.0;        5.0;  6.3636365;        5.0;   4.639964;  4.6363635;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;  4.6363635;   4.639964;        5.0;        5.0
   3;       5.0;       5.0;       5.0;       5.0;       5.0; 6.3636365;       5.0;  7.603306;       5.0;  6.3636365;  5.8831983;        5.0;   4.639964;  4.6363635;        5.0;  6.3636365;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;    4.31295;   4.639964;        5.0;        5.0
   4;       5.0;       5.0;       5.0;       5.0;       5.0; 6.3636365;       5.0;  8.039448;       5.0;  6.3636365;   7.166544;        5.0;   4.639964;  4.6363635;        5.0;  6.3636365;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;    4.31295;  4.3194256;        5.0;        5.0
   5;       5.0;       5.0;       5.0;       5.0;       5.0; 6.3636365;       5.0;  8.039448;       5.0;  6.3636365;   8.333221;  4.6551256;   4.639964;  4.6363635;        5.0;   7.603306;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;    4.31295;  4.3194256;  4.6499043;        5.0
   6;  4.653371;       5.0;       5.0;       5.0;       5.0; 6.3636365;       5.0;  8.039448;       5.0;  6.3636365;   9.393838;  4.6551256;   4.639964;  4.3279614;  6.3636365;   7.603306;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;        5.0;    4.31295;  4.3194256;  4.6499043;        5.0
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
|` P_Id_Trait` | positive integer number | Trait orientaiton of Place P_Id (ex: P_10_Trait) | trait units|
 - **Data view**:

![traced_places_traits](https://github.com/ipo-exe/abm-cue/blob/main/samples/view_traced_places_traits.png "traced_places_traits")

## Glossary

### By A-Z order
|Keyword | Data Type | Description | Units | Category|
|:--- | :--- | :--- | :--- | :---|
|`A_Id_Trait` | positive real number | Trait orientaiton of Agent A_Id (ex: A_12_Trait) | trait units | variable|
|`A_Id_x` | positive integer number | Position coordinate in the x axis of Agent A_Id (ex: A_12_x) | cell units | variable|
|`Agents File` | text | File path to the agents parameter file (ex: C:/data/param_agents.txt) | - | keyword|
|`Alias` | text | Category alias (one-word only) | - | field|
|`Alpha` | positive real number | Trait orientation threshold for agent-place interaction | - | parameter|
|`Beta` | positive integer number | Distance threshold for agent movement. | cell units | parameter|
|`C` | positive real number | Place-to-agent degree of interaction influence (agents openness to change) | - | parameter|
|`Color` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | - | field|
|`Count` | positive integer number | Couting units | - | field|
|`Count` | positive integer number | Keyword for `Counting` | - | keyword|
|`D` | positive real number | Agent-to-place degree of interaction influence (places openness to change) | - | parameter|
|`Date` | date | Date of record | - | field|
|`Id` | unique integer number | Category numerical identifyier | - | field|
|`Input Folder` | text | Folder path to the input data folder (ex: C:/data) | - | keyword|
|`Max` | positive real number | Keyword for `Maximum` | - | keyword|
|`Mean` | positive real number | Keyword for `Mean` | - | keyword|
|`Med` | positive real number | Keyword for `Median` | - | keyword|
|`Metadata` | text | Name of metadata | - | field|
|`Min` | positive real number | Keyword for `Minimum` | - | keyword|
|`Name` | text | Category name | - | field|
|`P_Id_Trait` | positive integer number | Trait orientaiton of Place P_Id (ex: P_10_Trait) | trait units | variable|
|`P_Id_x` | positive integer number | Position coordinate in the x axis of Place P_Id (ex: P_10_x) | cell units | variable|
|`Places File` | text | File path to the places parameter file (ex: C:/data/param_places.txt) | - | keyword|
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

### By category

#### Variable
|Keyword | Data Type | Description | Units | Category|
|:--- | :--- | :--- | :--- | :---|
|`A_Id_Trait` | positive real number | Trait orientaiton of Agent A_Id (ex: A_12_Trait) | trait units | variable|
|`A_Id_x` | positive integer number | Position coordinate in the x axis of Agent A_Id (ex: A_12_x) | cell units | variable|
|`P_Id_Trait` | positive integer number | Trait orientaiton of Place P_Id (ex: P_10_Trait) | trait units | variable|
|`P_Id_x` | positive integer number | Position coordinate in the x axis of Place P_Id (ex: P_10_x) | cell units | variable|
|`Trait` | positive real number | Trait orientation value | trait units | variable|
|`x` | positive integer number | Position coordinate in the x axis | cell units | variable|

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

#### Field
|Keyword | Data Type | Description | Units | Category|
|:--- | :--- | :--- | :--- | :---|
|`Alias` | text | Category alias (one-word only) | - | field|
|`Color` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | - | field|
|`Count` | positive integer number | Couting units | - | field|
|`Date` | date | Date of record | - | field|
|`Id` | unique integer number | Category numerical identifyier | - | field|
|`Metadata` | text | Name of metadata | - | field|
|`Name` | text | Category name | - | field|
|`Step` | positive integer number | Time step number | - | field|
|`Value` | miscellaneus | Value of data | - | field|

#### Parameter
|Keyword | Data Type | Description | Units | Category|
|:--- | :--- | :--- | :--- | :---|
|`Alpha` | positive real number | Trait orientation threshold for agent-place interaction | - | parameter|
|`Beta` | positive integer number | Distance threshold for agent movement. | cell units | parameter|
|`C` | positive real number | Place-to-agent degree of interaction influence (agents openness to change) | - | parameter|
|`D` | positive real number | Agent-to-place degree of interaction influence (places openness to change) | - | parameter|
|`Steps` | positive integer number | Number of time steps in the simulation | - | parameter|
