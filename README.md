# NBA command-line client
The aim of this project is to create a command-line client to access NBA-related information, such as boxscores, team and player stats. The client is written in Python and uses the excellent [nba-api](https://github.com/swar/nba_api) library.

### Installation
Info to be added

### Usage
A full description of the command-line options can be obtained by invoking
```
nba --help
```

The main commands that are corrently available are:
- boxscore
- player
- team

##### Boxscore
This command lets you visualize the last boxscore of the specified team
```
nba boxscore lal
```
An example is shown below:
```
LAL
PLAYER                    MIN    FG     FG3    FT       REB    AST    STL    BLK    TO    PF    PTS
------------------------  -----  -----  -----  -----  -----  -----  -----  -----  ----  ----  -----
Brandon Ingram            34:46   6-11    1-1    2-6      5      0      0      1     3     0     15
Kyle Kuzma                36:17   4-18    0-5    3-4      8      1      1      0     1     0     11
JaVale McGee              15:55    2-8    0-1    0-0      8      1      0      2     1     2      4
Josh Hart                 29:31    2-6    1-4    1-2      5      1      0      0     2     6      6
Lonzo Ball                31:14   3-13    1-5    0-0      7      6      2      0     1     5      7
Tyson Chandler            05:19    1-1    0-0    0-0      3      1      0      0     0     1      2
Kentavious Caldwell-Pope  26:41   5-13    1-4    1-2      5      0      1      0     2     2     12
Michael Beasley           17:43   6-15    0-3    5-6      3      1      2      1     1     3     17
Lance Stephenson          14:10    2-3    1-2    0-0      3      1      2      0     0     1      5
Ivica Zubac               14:03   4-10    0-0    2-2      5      1      0      1     0     3     10
Moritz Wagner             07:45    2-4    0-1    2-2      3      0      1      0     0     0      6
Svi Mykhailiuk            06:36    0-1    0-1    0-0      0      1      0      0     1     0      0
UTA
PLAYER                    MIN    FG     FG3    FT       REB    AST    STL    BLK    TO    PF    PTS
------------------------  -----  -----  -----  -----  -----  -----  -----  -----  ----  ----  -----
Joe Ingles                31:03   5-11    2-5    2-2     12      4      1      0     3     1     14
Derrick Favors            25:43   4-10    0-2    7-9     13      1      0      1     0     1     15
Rudy Gobert               31:39   4-10    0-0    4-8     18      2      2      2     2     4     12
Royce O'Neale             39:38   5-13   5-12    2-2      7      1      2      0     2     4     17
Donovan Mitchell          32:53  14-24    4-5    1-2      4      9      1      2     3     3     33
Jae Crowder               28:32   2-11    1-5    3-6      8      2      1      2     2     2      8
Kyle Korver               20:55    2-7    2-6    3-3      2      2      0      1     2     2      9
Georges Niang             20:34    1-8    1-6    0-0      0      2      2      1     1     3      3
Naz Mitrou-Long           03:01    1-1    0-0    0-0      0      0      0      0     1     0      2
Ekpe Udoh                 03:01    0-0    0-0    0-0      0      1      0      0     0     0      0
Tyler Cavanaugh           03:01    0-1    0-1    0-0      1      0      0      0     0     0      0
```

##### Player
This command fetches career stats of the specified player. A player can
be specified either by team and jersey number
```
nba player lal 23
```
or by full name
```
nba player 'lebron james'
```
Either way, the application will show career stats like:
```
      Name: LeBron James
    Height: 6-8
    Weight: 250
Experience: 15
  Position: Forward
       Age: 34.1
     Draft: 2003 (1, 1)

SEASON    TEAM      PTS    REB    AST    STL    BLK    TOV    FG_PCT    FG3_PCT    FT_PCT    MIN
--------  ------  -----  -----  -----  -----  -----  -----  --------  ---------  --------  -----
2003-04   CLE      20.9    5.5    5.9    1.6    0.7    3.5     0.417      0.290     0.754   39.5
2004-05   CLE      27.2    7.4    7.2    2.2    0.7    3.3     0.472      0.351     0.750   42.3
2005-06   CLE      31.4    7.0    6.6    1.6    0.8    3.3     0.480      0.335     0.738   42.5
2006-07   CLE      27.3    6.7    6.0    1.6    0.7    3.2     0.476      0.319     0.698   40.9
2007-08   CLE      30.0    7.9    7.2    1.8    1.1    3.4     0.484      0.315     0.712   40.4
2008-09   CLE      28.4    7.6    7.2    1.7    1.1    3.0     0.489      0.344     0.780   37.7
2009-10   CLE      29.7    7.3    8.6    1.6    1.0    3.4     0.503      0.333     0.767   39
2010-11   MIA      26.7    7.5    7.0    1.6    0.6    3.6     0.510      0.330     0.759   38.8
2011-12   MIA      27.1    7.9    6.2    1.9    0.8    3.4     0.531      0.362     0.771   37.5
2012-13   MIA      26.8    8.0    7.3    1.7    0.9    3.0     0.565      0.406     0.753   37.9
2013-14   MIA      27.1    6.9    6.3    1.6    0.3    3.5     0.567      0.379     0.750   37.7
2014-15   CLE      25.3    6.0    7.4    1.6    0.7    3.9     0.488      0.354     0.710   36.1
2015-16   CLE      25.3    7.4    6.8    1.4    0.6    3.3     0.520      0.309     0.731   35.6
2016-17   CLE      26.4    8.6    8.7    1.2    0.6    4.1     0.548      0.363     0.674   37.8
2017-18   CLE      27.5    8.6    9.1    1.4    0.9    4.2     0.542      0.367     0.731   36.9
2018-19   LAL      27.3    8.3    7.1    1.3    0.7    3.4     0.518      0.356     0.682   34.7
```

##### Team
This command displays the roster of the specified team, along with
basic player information. For example:
```
nba team lal
```
shows
```
  NUM  PLAYER                    POSITION      AGE  HEIGHT      WEIGHT_KG  EXP
-----  ------------------------  ----------  -----  --------  -----------  -----
    0  Kyle Kuzma                F              23  6-9               100  1
    1  Kentavious Caldwell-Pope  G              25  6-5                93  5
    2  Lonzo Ball                G              21  6-6                86  1
    3  Josh Hart                 G              23  6-5                98  1
    4  Alex Caruso               G              24  6-5                84  1
    5  Tyson Chandler            C              36  7-1               109  17
    6  Lance Stephenson          G              28  6-6               104  8
    7  JaVale McGee              C              30  7-0               122  10
    9  Rajon Rondo               G              32  6-1                84  12
   10  Svi Mykhailiuk            G              21  6-8                93  R
   11  Michael Beasley           F              30  6-9               107  10
   14  Brandon Ingram            F              21  6-9                86  2
   15  Moritz Wagner             C              21  6-11              111  R
   17  Isaac Bonga               G              19  6-8                82  R
   19  Johnathan Williams        F              23  6-9               103  R
   23  LeBron James              F              34  6-8               113  15
   40  Ivica Zubac               C              21  7-1               109  2
```
You can optionally add the flag `-s` (or `--stats`) to show stats of
the players. For example
```
nba team lal -s
```
shows
```
PLAYER_NAME                 GP    MIN  SCORING      PTS    REB    AST    TOV    STL    BLK
------------------------  ----  -----  ---------  -----  -----  -----  -----  -----  -----
LeBron James                34   34.7  52/36/68    27.3    8.3    7.1    3.4    1.3    0.7
Kyle Kuzma                  41   32.7  46/30/77    18.6    5.8    2.4    1.9    0.6    0.4
Brandon Ingram              32   32.0  46/30/62    16.3    4.8    2.6    2.5    0.6    0.7
Lonzo Ball                  43   30.0  40/33/41     9.5    5.2    5.1    2.2    1.5    0.4
Josh Hart                   43   27.2  42/36/68     9.3    4.0    1.4    0.9    1.1    0.6
Rajon Rondo                 14   24.3  45/36/62     8.4    4.4    6.7    2.1    1.0    0.0
Kentavious Caldwell-Pope    43   23.2  43/36/88    10.1    2.7    1.1    0.6    0.8    0.1
JaVale McGee                36   23.1  60/17/66    11.3    6.9    0.8    1.6    0.7    2.3
Tyson Chandler              31   19.4  60/0/65      3.8    6.9    0.8    0.8    0.5    0.5
Lance Stephenson            42   15.3  45/37/64     7.2    3.0    2.0    1.2    0.6    0.1
Ivica Zubac                 22   13.2  56/0/89      6.5    4.2    0.7    0.7    0.2    0.8
Johnathan Williams           7   12.8  55/0/20      3.3    3.0    0.6    0.3    0.1    0.6
Michael Beasley             15    9.9  56/25/71     7.3    1.9    0.7    1.0    0.3    0.3
Svi Mykhailiuk              29    9.8  34/33/53     2.9    0.6    0.8    0.6    0.3    0.0
Moritz Wagner               13    6.7  37/35/67     3.5    1.7    0.5    0.5    0.2    0.1
Isaac Bonga                  6    3.6  25/0/67      1.0    0.7    0.7    0.3    0.5    0.0
Alex Caruso                  2    2.6  0/0/0        0.0    0.5    0.0    0.0    0.0    0.0
```