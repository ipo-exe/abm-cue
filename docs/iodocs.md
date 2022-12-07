# I/O documentation
 - [Imported files](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#imported-files)
 - [Output files](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#output-files)
 - [Glossary](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#glossary)

# Imported files
These files must be prepared and sourced by the user. Samples are provided for proper formatting.

|File | Source | Format | Sample|
|:--- | :--- | :--- | :---|
|[param_agents.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_agentstxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_agents.txt)|
|[param_agents_2d.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_agents_2dtxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_agents_2d.txt)|
|[param_places.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_placestxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_places.txt)|
|[param_places_2d.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_places_2dtxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_places_2d.txt)|
|[map_places_2d.asc](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#map_places_2dasc) | imported by user | Raster Map | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/map_places_2d.asc)|
|[param_simulation.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_simulationtxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_simulation.txt)|
|[param_simulation_2d.txt](https://github.com/ipo-exe/abm-cue/blob/main/docs/iodocs.md#param_simulation_2dtxt) | imported by user | Data Table | [Sample file](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_simulation_2d.txt)|

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
 4; 20;     1;    20;    3; 0.01; Agent C;    AgC; orange
 5; 25;     1;    20;    3; 0.01; Agent C;    AgC; orange
 6; 30;     1;    20;    3; 0.01; Agent C;    AgC; orange
 7; 35;     1;    20;    3; 0.01; Agent C;    AgC; orange
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
|` C ` | positive real number | Place-to-agent degree of interaction influence (agents openness to change) | -|
|` Name ` | text | Category name | -|
|` Alias ` | text | Category alias (one-word only) | -|
|` Color` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | -|
 - **Data view**:

missing file

## `param_agents_2d.txt`
 - **Description**: Table of agents parameters and initial conditions;
 - **Source**: imported by user;
 - **File sample**: [param_agents_2d.txt](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_agents_2d.txt);
 - **Format**: Data Table;
 - **Formating example**:
```
Id;  x;  y; Trait; Alpha; Beta;   C;    Name; Alias ;  Color
 1; 12;  5;   5.0;     3;    1; 0.1; Agent A;    AgA;    red
 2; 12; 10;   5.0;     3;    5; 0.2; Agent B;    AgB;   blue
 3; 12; 15;   5.0;     3;    3; 0.0; Agent C;    AgC; orange
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
|` Alpha ` | positive real number | Trait orientation threshold for agent-place interaction | -|
|` Beta ` | positive integer number | Distance threshold for agent movement. | cell units|
|` C ` | positive real number | Place-to-agent degree of interaction influence (agents openness to change) | -|
|` Name ` | text | Category name | -|
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
Id;  x; Trait;   D;    Name; Alias; Color
 1;  0;     5; 0.1; Place A;    PA;  blue
 2;  1;     5; 0.1; Place A;    PA;   NaN
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
|` D ` | positive real number | Agent-to-place degree of interaction influence (places openness to change) | -|
|` Name ` | text | Category name | -|
|` Alias ` | text | Category alias (one-word only) | -|
|` Color` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | -|
 - **Data view**:

missing file

## `param_places_2d.txt`
 - **Description**: Table of places parameters and initial conditions;
 - **Source**: imported by user;
 - **File sample**: [param_places_2d.txt](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_places_2d.txt);
 - **Format**: Data Table;
 - **Formating example**:
```
 Id; Trait;   D; Name; Alias;   color
 12;     9; 0.1;  P12;   P12; #1EA12E
 13;     3; 0.1;  P13;   P13; #2AAA16
 14;     6; 0.1;  P14;   P14; #FA288D
 15;     7; 0.1;  P15;   P15; #94560A
 16;     6; 0.1;  P16;   P16; #4BBC55
 23;     5; 0.1;  P23;   P23; #74F3EC
 38;     3; 0.1;  P38;   P38; #522FF0
 39;     6; 0.1;  P39;   P39; #81F2BD
 40;     1; 0.1;  P40;   P40; #1E4E2F
 41;     1; 0.1;  P41;   P41; #A03D3F
 49;     6; 0.1;  P49;   P49; #BB1220
 50;     4; 0.1;  P50;   P50; #A9C849
 55;     5; 0.1;  P55;   P55; #34090A
 56;    10; 0.1;  P56;   P56; #F0DF62
 57;     6; 0.1;  P57;   P57; #AAE7D2
 58;     1; 0.1;  P58;   P58; #44F560
 60;     7; 0.1;  P60;   P60; #F30C03
 61;     8; 0.1;  P61;   P61; #F1B57D
 62;     6; 0.1;  P62;   P62; #E98BE9
 63;     2; 0.1;  P63;   P63; #58B45B
 64;     8; 0.1;  P64;   P64; #7C0159
 65;    10; 0.1;  P65;   P65; #8F4841
 66;     2; 0.1;  P66;   P66; #2B0AB8
 67;     7; 0.1;  P67;   P67; #CC7D75
 68;     3; 0.1;  P68;   P68; #642331
 69;     7; 0.1;  P69;   P69; #392757
 70;     7; 0.1;  P70;   P70; #B2179C
 71;     4; 0.1;  P71;   P71; #6E25AB
 72;     7; 0.1;  P72;   P72; #FA2E2C
 73;     1; 0.1;  P73;   P73; #6FDAFB
 74;     2; 0.1;  P74;   P74; #3626A5
 75;     5; 0.1;  P75;   P75; #5F76EF
 76;     2; 0.1;  P76;   P76; #F429A8
 77;     3; 0.1;  P77;   P77; #335766
 78;     4; 0.1;  P78;   P78; #06DE45
 79;     9; 0.1;  P79;   P79; #E8C5A4
 80;     4; 0.1;  P80;   P80; #FDC8A6
 81;     9; 0.1;  P81;   P81; #08DE34
 82;     7; 0.1;  P82;   P82; #57BAC2
 83;    10; 0.1;  P83;   P83; #34318D
 84;     2; 0.1;  P84;   P84; #BBB690
 85;    10; 0.1;  P85;   P85; #17BEC4
 86;    10; 0.1;  P86;   P86; #E9B017
 87;     6; 0.1;  P87;   P87; #ABC410
 88;     3; 0.1;  P88;   P88; #DC5F98
 89;     4; 0.1;  P89;   P89; #1EC8C2
 90;     5; 0.1;  P90;   P90; #24D592
 91;     8; 0.1;  P91;   P91; #858883
 92;     3; 0.1;  P92;   P92; #7D4BC7
 93;     5; 0.1;  P93;   P93; #02D2B6
 94;     2; 0.1;  P94;   P94; #B11E49
 95;     9; 0.1;  P95;   P95; #8CEAA6
 96;     5; 0.1;  P96;   P96; #AC743A
 97;     5; 0.1;  P97;   P97; #07AA64
 98;     1; 0.1;  P98;   P98; #E330E9
 99;     8; 0.1;  P99;   P99; #E7C1F5
100;     6; 0.1; P100;  P100; #28050C
101;     6; 0.1; P101;  P101; #E6A230
102;     8; 0.1; P102;  P102; #0E2241
103;    10; 0.1; P103;  P103; #FE756A
104;    10; 0.1; P104;  P104; #5C158D
105;     2; 0.1; P105;  P105; #255E18
106;     7; 0.1; P106;  P106; #A0BFE3
107;     7; 0.1; P107;  P107; #8BD8CB
108;     6; 0.1; P108;  P108; #07C674
109;     2; 0.1; P109;  P109; #630E58
110;     7; 0.1; P110;  P110; #C480B9
111;     3; 0.1; P111;  P111; #43FCE7
112;     1; 0.1; P112;  P112; #D26ADD
113;     8; 0.1; P113;  P113; #A59A03
114;     9; 0.1; P114;  P114; #89C720
115;     1; 0.1; P115;  P115; #D45E92
116;     8; 0.1; P116;  P116; #6D1E70
117;     4; 0.1; P117;  P117; #260970
118;     4; 0.1; P118;  P118; #1945F7
119;     7; 0.1; P119;  P119; #5E91E1
120;     7; 0.1; P120;  P120; #8C3E05
121;     8; 0.1; P121;  P121; #253269
122;     2; 0.1; P122;  P122; #696429
123;     4; 0.1; P123;  P123; #B0A739
124;     9; 0.1; P124;  P124; #0CA751
125;    10; 0.1; P125;  P125; #08A1ED
126;     8; 0.1; P126;  P126; #7991BC
127;     9; 0.1; P127;  P127; #CD8525
128;     8; 0.1; P128;  P128; #C98B80
129;    10; 0.1; P129;  P129; #0E14EC
130;     6; 0.1; P130;  P130; #7FD0F7
131;     9; 0.1; P131;  P131; #7916E3
132;     3; 0.1; P132;  P132; #86E09A
133;     1; 0.1; P133;  P133; #0A2C3B
134;     4; 0.1; P134;  P134; #9C0DEF
135;     3; 0.1; P135;  P135; #A2C689
136;     4; 0.1; P136;  P136; #D1BA45
137;     9; 0.1; P137;  P137; #930CAE
138;     2; 0.1; P138;  P138; #CB4585
139;    10; 0.1; P139;  P139; #139E80
140;     4; 0.1; P140;  P140; #94D9E1
141;    10; 0.1; P141;  P141; #B5B29E
142;     9; 0.1; P142;  P142; #754207
143;     7; 0.1; P143;  P143; #C30CAC
144;     6; 0.1; P144;  P144; #F3E526
145;     3; 0.1; P145;  P145; #7CFC51
146;     6; 0.1; P146;  P146; #5BF3D6
147;    10; 0.1; P147;  P147; #4597B3
148;     8; 0.1; P148;  P148; #29721E
149;    10; 0.1; P149;  P149; #7BE3D3
150;     6; 0.1; P150;  P150; #D519F8
151;     8; 0.1; P151;  P151; #079042
152;     8; 0.1; P152;  P152; #97F7C3
153;     6; 0.1; P153;  P153; #49C83E
154;     6; 0.1; P154;  P154; #9C5BFE
155;     9; 0.1; P155;  P155; #3F777C
156;     5; 0.1; P156;  P156; #D2C6A0
157;     7; 0.1; P157;  P157; #F99B05
158;     9; 0.1; P158;  P158; #093EEE
159;     5; 0.1; P159;  P159; #B1217A
160;     4; 0.1; P160;  P160; #BBCC72
161;     6; 0.1; P161;  P161; #B47CDE
162;     1; 0.1; P162;  P162; #D163EE
163;     7; 0.1; P163;  P163; #ACBBDD
164;     2; 0.1; P164;  P164; #31E78A
165;     5; 0.1; P165;  P165; #3035E1
166;     4; 0.1; P166;  P166; #525721
167;     3; 0.1; P167;  P167; #E37FF7
168;     5; 0.1; P168;  P168; #DF09B4
169;     5; 0.1; P169;  P169; #36F16F
170;     7; 0.1; P170;  P170; #4FFC8D
171;     7; 0.1; P171;  P171; #31F90F
172;     4; 0.1; P172;  P172; #D6D66E
173;     4; 0.1; P173;  P173; #EA55E8
174;     1; 0.1; P174;  P174; #B0F392
175;    10; 0.1; P175;  P175; #3B3F4E
176;     1; 0.1; P176;  P176; #F85C50
177;     7; 0.1; P177;  P177; #6D5276
178;     7; 0.1; P178;  P178; #B33721
179;     2; 0.1; P179;  P179; #A66DAF
180;     1; 0.1; P180;  P180; #DD50BD
181;     8; 0.1; P181;  P181; #DD0258
182;     9; 0.1; P182;  P182; #44FEC2
183;    10; 0.1; P183;  P183; #3C1EA4
184;     2; 0.1; P184;  P184; #0CEE4B
185;     4; 0.1; P185;  P185; #B9E09D
186;     5; 0.1; P186;  P186; #880588
187;     5; 0.1; P187;  P187; #E6F706
188;    10; 0.1; P188;  P188; #C30C6A
189;     9; 0.1; P189;  P189; #80E834
190;     5; 0.1; P190;  P190; #A4F37E
191;     4; 0.1; P191;  P191; #41B4B4
192;     7; 0.1; P192;  P192; #3B7C20
193;     8; 0.1; P193;  P193; #8D6088
194;     2; 0.1; P194;  P194; #4ACAEF
195;     9; 0.1; P195;  P195; #A7572E
196;     1; 0.1; P196;  P196; #A1242D
197;     8; 0.1; P197;  P197; #C177F2
198;     4; 0.1; P198;  P198; #29EB59
199;     6; 0.1; P199;  P199; #FFA4BF
202;     6; 0.1; P202;  P202; #8C63C5
205;     7; 0.1; P205;  P205; #127A9D
211;     4; 0.1; P211;  P211; #7BE933
214;     2; 0.1; P214;  P214; #B72079
215;    10; 0.1; P215;  P215; #0E6D2A
217;     7; 0.1; P217;  P217; #2C71AA
218;     9; 0.1; P218;  P218; #0DEA3C
220;     1; 0.1; P220;  P220; #7C3084
222;     1; 0.1; P222;  P222; #7CAA12
223;    10; 0.1; P223;  P223; #F528E7
224;     9; 0.1; P224;  P224; #870F2C
225;     7; 0.1; P225;  P225; #B7E2D0
226;     7; 0.1; P226;  P226; #47D9F9
227;     3; 0.1; P227;  P227; #FE2DAA
228;     7; 0.1; P228;  P228; #ADFBCE
229;     7; 0.1; P229;  P229; #FAB243
230;     1; 0.1; P230;  P230; #FF4DAB
234;     5; 0.1; P234;  P234; #E176BF
235;     2; 0.1; P235;  P235; #787128
236;     5; 0.1; P236;  P236; #E2DDF0
237;     3; 0.1; P237;  P237; #1D5CF4
238;     9; 0.1; P238;  P238; #7CF616
239;     4; 0.1; P239;  P239; #E91C57
240;     4; 0.1; P240;  P240; #1615C5
241;     8; 0.1; P241;  P241; #A4049F
242;     9; 0.1; P242;  P242; #C3FD50
243;     2; 0.1; P243;  P243; #376AE9
244;     6; 0.1; P244;  P244; #033951
245;     5; 0.1; P245;  P245; #210108
246;     4; 0.1; P246;  P246; #49587D
247;     7; 0.1; P247;  P247; #AAA403
248;    10; 0.1; P248;  P248; #5943F9
249;     7; 0.1; P249;  P249; #6A6AEB
250;     6; 0.1; P250;  P250; #544796
251;     7; 0.1; P251;  P251; #9611C6
252;     7; 0.1; P252;  P252; #DF399B
253;     4; 0.1; P253;  P253; #C85C32
254;     9; 0.1; P254;  P254; #745CF9
255;     7; 0.1; P255;  P255; #DF5B2E
256;     2; 0.1; P256;  P256; #396314
257;     2; 0.1; P257;  P257; #55D0CB
258;     2; 0.1; P258;  P258; #3D6818
259;     4; 0.1; P259;  P259; #8DEE9F
260;    10; 0.1; P260;  P260; #8E2BB9
261;     3; 0.1; P261;  P261; #E6063C
262;     2; 0.1; P262;  P262; #F39544
263;     1; 0.1; P263;  P263; #143EE4
264;     5; 0.1; P264;  P264; #01EC4B
265;     7; 0.1; P265;  P265; #F92768
266;     2; 0.1; P266;  P266; #74A285
267;     1; 0.1; P267;  P267; #172595
268;     5; 0.1; P268;  P268; #40976F
269;     2; 0.1; P269;  P269; #D4E4BC
270;     2; 0.1; P270;  P270; #3EBA9D
271;     7; 0.1; P271;  P271; #53D53A
272;     3; 0.1; P272;  P272; #7AA76F
273;     5; 0.1; P273;  P273; #80391D
274;     9; 0.1; P274;  P274; #217071
275;    10; 0.1; P275;  P275; #FEE953
276;     2; 0.1; P276;  P276; #34BBDD
277;     6; 0.1; P277;  P277; #4ED101
278;     5; 0.1; P278;  P278; #3CAC9C
279;     7; 0.1; P279;  P279; #02BD58
280;     5; 0.1; P280;  P280; #C109BC
281;     1; 0.1; P281;  P281; #19B178
282;     3; 0.1; P282;  P282; #D261ED
283;     8; 0.1; P283;  P283; #80486A
284;     8; 0.1; P284;  P284; #D1D0C6
285;     4; 0.1; P285;  P285; #DC958B
286;     5; 0.1; P286;  P286; #349AC4
287;     6; 0.1; P287;  P287; #FE2D71
288;     8; 0.1; P288;  P288; #9EB4C9
289;    10; 0.1; P289;  P289; #3D74DC
290;    10; 0.1; P290;  P290; #319D41
291;    10; 0.1; P291;  P291; #B9EBCA
292;     1; 0.1; P292;  P292; #6E6931
293;     2; 0.1; P293;  P293; #BCF44B
294;     1; 0.1; P294;  P294; #551C51
295;     7; 0.1; P295;  P295; #A38D7D
296;     7; 0.1; P296;  P296; #2C5B2E
297;    10; 0.1; P297;  P297; #6EDA0F
298;     6; 0.1; P298;  P298; #6F2841
299;     2; 0.1; P299;  P299; #688793
300;     7; 0.1; P300;  P300; #792864
301;     2; 0.1; P301;  P301; #206F0C
302;     8; 0.1; P302;  P302; #EBAE86
303;     6; 0.1; P303;  P303; #9E1728
304;     5; 0.1; P304;  P304; #3929E1
305;     3; 0.1; P305;  P305; #8A2719
306;     3; 0.1; P306;  P306; #A2A0D3
307;     7; 0.1; P307;  P307; #8297DD
308;     3; 0.1; P308;  P308; #D10098
309;     2; 0.1; P309;  P309; #CC4EC6
310;     2; 0.1; P310;  P310; #CE0762
311;     4; 0.1; P311;  P311; #C443AF
312;     5; 0.1; P312;  P312; #404594
313;     6; 0.1; P313;  P313; #0855F7
314;     3; 0.1; P314;  P314; #A1596A
315;     9; 0.1; P315;  P315; #8C13D8
316;    10; 0.1; P316;  P316; #FA2932
317;     6; 0.1; P317;  P317; #E4B4CB
318;     1; 0.1; P318;  P318; #05F6A6
319;     5; 0.1; P319;  P319; #DEEB67
320;     5; 0.1; P320;  P320; #273B29
321;    10; 0.1; P321;  P321; #628BF7
322;     5; 0.1; P322;  P322; #36B200
323;     9; 0.1; P323;  P323; #777EAC
324;     3; 0.1; P324;  P324; #90F42E
325;     5; 0.1; P325;  P325; #38FF0A
326;     5; 0.1; P326;  P326; #272CB3
327;     2; 0.1; P327;  P327; #4AA757
328;     1; 0.1; P328;  P328; #B6032E
329;     4; 0.1; P329;  P329; #BE45D8
330;     8; 0.1; P330;  P330; #0BE74F
331;     8; 0.1; P331;  P331; #3C8C58
332;     1; 0.1; P332;  P332; #ADC3EF
333;     5; 0.1; P333;  P333; #0F8609
340;     6; 0.1; P340;  P340; #61127C
341;     4; 0.1; P341;  P341; #25F6BA
342;     7; 0.1; P342;  P342; #5A0ED8
343;     2; 0.1; P343;  P343; #1F8E6D
344;     3; 0.1; P344;  P344; #ECBAD6
346;     4; 0.1; P346;  P346; #CFEAFA
347;    10; 0.1; P347;  P347; #875485
348;     1; 0.1; P348;  P348; #4042AA
349;    10; 0.1; P349;  P349; #B76E9A
350;     3; 0.1; P350;  P350; #B36E20
352;     3; 0.1; P352;  P352; #BF9B8D
354;     7; 0.1; P354;  P354; #C6DD41
356;    10; 0.1; P356;  P356; #7F2FD4
367;     6; 0.1; P367;  P367; #CD749C
372;     4; 0.1; P372;  P372; #81296E
374;     9; 0.1; P374;  P374; #B3BBAE
376;     9; 0.1; P376;  P376; #020B26
377;     2; 0.1; P377;  P377; #D139D0
378;     4; 0.1; P378;  P378; #F5DDE5
380;     2; 0.1; P380;  P380; #AB46EF
381;     5; 0.1; P381;  P381; #7A29E3
382;     8; 0.1; P382;  P382; #C07C1C
383;     7; 0.1; P383;  P383; #1C2AE0
384;     9; 0.1; P384;  P384; #6AD781
385;     1; 0.1; P385;  P385; #EBBAFC
386;     6; 0.1; P386;  P386; #BECD82
387;     2; 0.1; P387;  P387; #192D8B
388;     8; 0.1; P388;  P388; #706991
389;     4; 0.1; P389;  P389; #50E4AF
390;     4; 0.1; P390;  P390; #D53907
391;     9; 0.1; P391;  P391; #354E75
392;     4; 0.1; P392;  P392; #C648D0
393;     8; 0.1; P393;  P393; #34D431
394;     5; 0.1; P394;  P394; #3B22F4
395;     9; 0.1; P395;  P395; #9F17E7
396;     6; 0.1; P396;  P396; #66649C
398;    10; 0.1; P398;  P398; #047CE6
399;     2; 0.1; P399;  P399; #BDA98C
400;     5; 0.1; P400;  P400; #985CC5
401;     9; 0.1; P401;  P401; #3C5981
402;     4; 0.1; P402;  P402; #BB14AF
403;     7; 0.1; P403;  P403; #D0C154
404;    10; 0.1; P404;  P404; #EB663F
405;     7; 0.1; P405;  P405; #267637
430;    10; 0.1; P430;  P430; #C03F70
431;     3; 0.1; P431;  P431; #4A5150
437;     6; 0.1; P437;  P437; #01408C
452;     3; 0.1; P452;  P452; #01FF84
453;     9; 0.1; P453;  P453; #E92D82
454;     9; 0.1; P454;  P454; #E52A90
455;     3; 0.1; P455;  P455; #7AE169
456;     2; 0.1; P456;  P456; #7346D4
457;     5; 0.1; P457;  P457; #C3E954
458;     7; 0.1; P458;  P458; #93232C
459;     5; 0.1; P459;  P459; #122410
460;    10; 0.1; P460;  P460; #80082E
461;     9; 0.1; P461;  P461; #374F79
462;     7; 0.1; P462;  P462; #1EE334
463;     8; 0.1; P463;  P463; #242B35
464;     4; 0.1; P464;  P464; #8CA110
465;     6; 0.1; P465;  P465; #2206C7
466;     1; 0.1; P466;  P466; #CB370C
467;     2; 0.1; P467;  P467; #0A1C86
468;     4; 0.1; P468;  P468; #9A7910
469;     6; 0.1; P469;  P469; #7B8074
470;     1; 0.1; P470;  P470; #BAAB5A
471;     4; 0.1; P471;  P471; #04D554
472;     6; 0.1; P472;  P472; #8C1A36
473;     1; 0.1; P473;  P473; #133139
474;     2; 0.1; P474;  P474; #C31CAC
475;     2; 0.1; P475;  P475; #2D1885
476;     6; 0.1; P476;  P476; #93B36D
477;     1; 0.1; P477;  P477; #514218
478;     8; 0.1; P478;  P478; #DD2C18
479;     9; 0.1; P479;  P479; #AAC147
480;     3; 0.1; P480;  P480; #BFB3A3
481;     7; 0.1; P481;  P481; #0E59E9
482;     7; 0.1; P482;  P482; #A035BD
483;     6; 0.1; P483;  P483; #75ECAF
484;     6; 0.1; P484;  P484; #D4B305
485;     7; 0.1; P485;  P485; #26A932
486;     6; 0.1; P486;  P486; #AAC788
487;     9; 0.1; P487;  P487; #46EE0E
488;     3; 0.1; P488;  P488; #760624
489;     7; 0.1; P489;  P489; #890A97
490;     8; 0.1; P490;  P490; #907AC8
491;     7; 0.1; P491;  P491; #452CD3
492;     5; 0.1; P492;  P492; #FC5C9F
493;     6; 0.1; P493;  P493; #9C5600
494;     7; 0.1; P494;  P494; #AC298E
```
 - **Requirements**:
	 - Field separator: semicolon `;`;
	 - Decimal separator: period `.`;
 - **Mandatory Fields**:

|Field Name | Data Type | Description | Units|
|:--- | :--- | :--- | :---|
|`Id ` | unique integer number | Category numerical identifyier | -|
|` Trait ` | positive real number | Trait orientation value | trait units|
|` D ` | positive real number | Agent-to-place degree of interaction influence (places openness to change) | -|
|` Name ` | text | Category name | -|
|` Alias ` | text | Category alias (one-word only) | -|
|` Color` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | -|
 - **Data view**:

missing file

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
 - **Data view**:

missing file

## `param_simulation.txt`
 - **Description**: Table of simulation parameters;
 - **Source**: imported by user;
 - **File sample**: [param_simulation.txt](https://github.com/ipo-exe/abm-cue/blob/main/samples/param_simulation.txt);
 - **Format**: Data Table;
 - **Formating example**:
```
     Metadata;                                                   Value
    Timestamp;                                  2022/08/25 16:48:07.86
 Input Folder;                  C:/000_myFiles/myCodes/abm-cue/samples
   Run Folder;                                                  C:/bin
  Agents File; C:/000_myFiles/myCodes/abm-cue/samples/param_agents.txt
  Places File; C:/000_myFiles/myCodes/abm-cue/samples/param_places.txt
        Steps;                                                     100
Return Agents;                                                    True
   Trace Back;                                                    True
   Plot Steps;                                                   False
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
  Agents File; C:/000_myFiles/myCodes/abm-cue/samples/param_agents_2d.txt
  Places File; C:/000_myFiles/myCodes/abm-cue/samples/param_places_2d.txt
   Places Map;   C:/000_myFiles/myCodes/abm-cue/samples/map_places_2d.asc
        Steps;                                                        100
Return Agents;                                                       True
   Trace Back;                                                       True
   Plot Steps;                                                      False
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
|` Alpha ` | positive real number | Trait orientation threshold for agent-place interaction | -|
|` Beta ` | positive integer number | Distance threshold for agent movement. | cell units|
|` C` | positive real number | Place-to-agent degree of interaction influence (agents openness to change) | -|
 - **Data view**:

missing file

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
|` Alpha ` | positive real number | Trait orientation threshold for agent-place interaction | -|
|` Beta ` | positive integer number | Distance threshold for agent movement. | cell units|
|` C` | positive real number | Place-to-agent degree of interaction influence (agents openness to change) | -|
 - **Data view**:

missing file

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
|` D` | positive real number | Agent-to-place degree of interaction influence (places openness to change) | -|
 - **Data view**:

missing file

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
 - **Data view**:

missing file

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
 - **Data view**:

missing file

## Glossary

### By A-Z order
|Keyword | Data Type | Description | Units | Category|
|:--- | :--- | :--- | :--- | :---|
|`A_Id_Trait` | positive real number | Trait orientation of Agent A_Id (ex: A_12_Trait) | trait units | variable|
|`A_Id_x` | positive integer number | Position coordinate in the x axis of Agent A_Id (ex: A_12_x) | cell units | variable|
|`A_Id_y` | positive integer number | Position coordinate in the y axis of Agent A_Id (ex: A_12_y) | cell units | variable|
|`Agents File` | text | File path to the agents parameter file (ex: C:/data/param_agents.txt) | - | keyword|
|`Alias` | text | Category alias (one-word only) | - | field|
|`Alpha` | positive real number | Trait orientation threshold for agent-place interaction | - | parameter|
|`Beta` | positive integer number | Distance threshold for agent movement. | cell units | parameter|
|`C` | positive real number | Place-to-agent degree of interaction influence (agents openness to change) | - | parameter|
|`Color` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | - | field|
|`Count` | positive integer number | Counting units | - | field|
|`Count` | positive integer number | Keyword for `Counting` | - | keyword|
|`D` | positive real number | Agent-to-place degree of interaction influence (places openness to change) | - | parameter|
|`Date` | date | Date of record | - | field|
|`H` | real number | Shannon Entropy | Bits | field|
|`H_agents` | real number | Shannon Entropy of Agents | Bits | field|
|`H_places` | real number | Shannon Entropy of Places | Bits | field|
|`Id` | unique integer number | Category numerical identifyier | - | field|
|`Input Folder` | text | Folder path to the input data folder (ex: C:/data) | - | keyword|
|`Max` | positive real number | Keyword for `Maximum` | - | keyword|
|`Mean` | positive real number | Keyword for `Mean` | - | keyword|
|`Med` | positive real number | Keyword for `Median` | - | keyword|
|`Metadata` | text | Name of metadata | - | field|
|`Min` | positive real number | Keyword for `Minimum` | - | keyword|
|`Name` | text | Category name | - | field|
|`P_Id_Trait` | positive integer number | Trait orientation of Place P_Id (ex: P_10_Trait) | trait units | variable|
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
|`y` | positive integer number | Position coordinate in the y axis | cell units | variable|

### By category

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

#### Field
|Keyword | Data Type | Description | Units | Category|
|:--- | :--- | :--- | :--- | :---|
|`Alias` | text | Category alias (one-word only) | - | field|
|`Color` | text | CSS color name available in [matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html) (ex: `blue`) or hexadecimal code of color (ex: `#5234eb`). | - | field|
|`Count` | positive integer number | Counting units | - | field|
|`Date` | date | Date of record | - | field|
|`H` | real number | Shannon Entropy | Bits | field|
|`H_agents` | real number | Shannon Entropy of Agents | Bits | field|
|`H_places` | real number | Shannon Entropy of Places | Bits | field|
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
