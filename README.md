# A star search algorithm for solving rolling-die maze

### Members:

1. Karan Jariwala (kkj1811@rit.edu)
2. Deepak Sharma (ds5930@rit.edu)
3. Aravindh Kuppusamy (axk8776@rit.edu)

------

### Problem Statement:

Implement an A* search algorithm in python for solving rolling-die mazes. The objective is to "roll" a die along its edges through a grid until a goal location is reached. The initial state of the search is given by the die location and orientation. Rolling die mazes contain obstacles, as well as restrictions on which numbers may face “UP”

#### These are the following constraints:

1. The die begins with 1 on top, 2 facing up/north, and 3 facing right/east.

2. All opposite die faces add to 7 (e.g./ 2 on top + 5 on bottom = 7).

3. The number 6 should never be face up on the die.

4. The number 1 must be on top of the die when the goal location is reached.

   ​

------

### Approach:

**Graph search** is perfectly fit for this project, allowing paths to previously visited nodes to be pruned, and equally importantly, ensuring that the program will terminate when we have exhausted the state space when a solution does not exist, rather than repeatedly visiting previous states, producing an infinite loop. We have Implemented different heuristics that are admissible and consistent for use with our A* search function. The heuristics we implemented are **Manhattan Distance**, **Diagonal Distance**, **Euclidean Distance**, and our customized Fancy Manhattan Distance which is a modified version of Manhattan Distance.

------

### Execution of program:

**Main file name:** rdMaze.py

**Python version:** 3.5.1

**Required packages:** matplotlib, numpy

If the required packages are not installed in your machine, then please comment the line number ( 11, 12 ), method definition 'plot' starting from line number 222 to 246, and lastly line number 272.

#### Below are the options to run the python file:

1. ```shell
   # python3 rdMaze.py <Maze's filename>
   - You will see the output in the console for the Maze file you provided for all the Heuristics( 'fancy_manhattan', 'manhattan', 'euclidean', 'diagonal' )
   ```

2. ```python
   # python3 rdMaze.py <Maze's filename> <Heuristics name>
   - You will see the output in the console for the Maze file and specific Heuristics you provided.
   ```

3. ```python
   # python3 rdMaze.py
   - you will be prompted to enter the Maze filename and also the heuristics you want to use in A* search. And you will see the output in the console for the Maze file and specific Heuristics you provided.
   ```

   where,

   | Parameters          | E.g:        |
   | ------------------- | ----------- |
   | <Maze's filename>   | "map1.txt"  |
   | \<Heuristics name\> | "manhattan" |



### Output:

Below is the short snapshot of the output when it run on map4.txt with Euclidean distance.

```shell
python rdMaze.py map4.txt euclidean
```

```shell
|------------- STARTING MAZE--------------|

. G * . S . 
. . . * . . 
. * . . . * 
. . . . . . 
. . . * . . 

|------------- STARTING DICE ORIENTATION--------------|

	  2							 NORTH
	  |	 	 	 	 	 	 	  |
4 - 1 / 6 - 3		 LEFT - TOP / BOTTOM - RIGHT
	  |	 	 	 	 	 	 	  |
	  5							 SOUTH
|==================== MOVE: 0====================|

|------------- MAZE--------------|

. G * . # . 
. . . * . . 
. * . . . * 
. . . . . . 
. . . * . . 
|==================== MOVE: 1====================|

|------------- MAZE--------------|

. G * . # . 
. . . * # . 
. * . . . * 
. . . . . . 
. . . * . . 

and so on.....

|==================== MOVE: 21====================|

|------------- MAZE--------------|

# # * . # # 
# . . * # # 
# * . . # * 
# # # # # # 
# # . * # # 

|---------------- PERFORMANCE METRICS -----------------|

No. of moves in the solution                    :  21
No. of nodes put on the queue                   :  107
No. of nodes visited / removed from the queue   :  86

|------------------------------------------------------|
```

### Performance:

Following graph shows the number of nodes generated and visited for Euclidean distance for map4

![](https://github.com/karan6181/AStarSearchAlgorithm/blob/master/Output_Map4/Euclidean.png)

------

### Other Details:

To read more about this project, please refer to the project [report](https://github.com/karan6181/AStarSearchAlgorithm/blob/master/Report/project01_axk8776_ds5930_kkj1811.pdf).
