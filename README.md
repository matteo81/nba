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
Either way, the application show career stats like:
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