Read Me:

Main file name: rdMaze.py
Python version: 3.5.1
Required packages: matplotlib, numpy
If the required packages are not installed in your machine, then please comment the line number ( 11, 12 ), method defination 'plot' starting from line number 222 to 246, and lastly line number 272.

Below are the options to run the python file:

1. python3 rdMaze.py <Maze's filename>
2. python3 rdMaze.py <Maze's filename> <Heuristics name>
3. python3 rdMaze.py

- <filename> is a string e.g.: "map1.txt"
- <Heuristics name> is a string e.g.: "manhattan"

For the 1st option, you will see the output in the console for the Maze file you provided for all the Heuristics( 'fancy_manhattan', 'manhattan', 'euclidean', 'diagonal' )
For the 2nd option, You will see the output in the console for the Maze file and specific Heuristics you provided.
For the 3rd option, you will be prompted to enter the Maze's filename and also the heuristics you want to use in A* search. And you will see the output in the console for the Maze file and specific Heuristics you provided.