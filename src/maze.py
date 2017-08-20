"""
File: maze.py
Language: Python 3.5.1
Author: Aravindh Kuppusamy ( axk8776@rit.edu )
        Deepak Sharma ( ds5930@rit.edu )
        Karan Jariwala( kkj1811@rit.edu )
Description: Representation of the maze configuration and
             methods to operate on it
"""

__author__ = "Deepak Sharma, Karan Jariwala, Aravindh Kuppusamy"

class Maze:
    """
    The class Maze represents the maze configuration. The maze is
    represented as a 2-D matrix. It includes starting position and goal
    position as tuple (x-coordinate, y-coordinate), a nodeMap which contain
    key as ( x-coordinate, y-coordinate, dice top, dice right, dice north ) and
    value as node object, and width and height of the maze.
    """
    def __init__(self, layoutText):
        """
        The parameterized constructor which initializes the maze
        configuration
        :param layoutText: The 2-D array of the maze
        """
        self.width = len(layoutText[0])
        self.height = len(layoutText)
        self.obstacles = [[False for y in range(self.height)] for x in range(self.width)]
        self.mazeOrientation = [[None for y in range(self.height)] for x in range(self.width)]
        self.startingPos = (None, None)
        self.goalPos = (None, None)
        self.processLayout(layoutText)
        self.nodeMap = {}

    def processLayout(self, layoutText):
        """
        Processing each character in the 2-D array and append that to the
        maze orientation where top left location is (0,0).
        :param layoutText: The 2-D array of the maze
        :return: None
        """
        maxY = self.height - 1
        for y in range(self.height):
            for x in range(self.width):
                layoutChar = layoutText[maxY - y][x]
                self.mazeOrientation[x][y] = layoutChar
                self.processLayoutChar(x, y, layoutChar)

    def processLayoutChar(self, x, y, layoutChar):
        """
        Process each character where obstacles represent as boolean True and
        store the starting position and goal location based on the maze
        configuration
        :param x: x-coordinate of maze
        :param y: y-coordinate of maze
        :param layoutChar: The 2-D array of the maze
        :return: None
        """
        if layoutChar == '*':
            self.obstacles[x][y] = True
        elif layoutChar == 'S':
            self.startingPos = (x, y)
        elif layoutChar == 'G':
            self.goalPos = (x, y)

    def isObstacle(self, pos):
        """
        This method will check whether there is an obstacles or not at the
        provided position
        :param pos: Tuple ( x-coordinate, y-coordinate )
        :return: True if an obstacles else otherwise
        """
        if self.isPosInMaze(pos):
            x, y = pos
            return self.obstacles[x][y]

    def isPosInMaze(self, pos):
        """
        The method will check whether the coordinates provided is a valid
        coordinate in the maze
        :param pos: Tuple ( x-coordinate, y-coordinate )
        :return: True if it is a valid position else otherwise
        """
        x, y = pos
        return 0 <= x <= self.width - 1 and 0 <= y <= self.height - 1

    def getValidNeighbors(self, x, y, dice):
        """
        This method will return the list of valid neighbors from the current
        node which excludes the obstacles neighbors
        :param x: current object x-coordinate
        :param y: current object y-coordinate
        :param dice: current dice configuration
        :return: List of valid neighbors
        """
        neighbors = list()
        if self.isPosInMaze((x - 1, y)) and not self.obstacles[x - 1][y]:
            dice.moveLeft()
            top = dice.top
            right = dice.right
            north = dice.north
            dice.moveRight()
            neighbors.append((x - 1, y, top, right, north))

        if self.isPosInMaze((x + 1, y)) and not self.obstacles[x + 1][y]:
            dice.moveRight()
            top = dice.top
            right = dice.right
            north = dice.north
            dice.moveLeft()
            neighbors.append((x + 1, y, top, right, north))

        if self.isPosInMaze((x, y - 1)) and not self.obstacles[x][y - 1]:
            dice.moveSouth()
            top = dice.top
            right = dice.right
            north = dice.north
            dice.moveNorth()
            neighbors.append((x, y - 1, top, right, north))

        if self.isPosInMaze((x, y + 1)) and not self.obstacles[x][y + 1]:
            dice.moveNorth()
            top = dice.top
            right = dice.right
            north = dice.north
            dice.moveSouth()
            neighbors.append((x, y + 1, top, right, north))

        return neighbors

    def isGoal(self, x, y, diceTop):
        """
        It checks whether the current node is a goal node by checking the
        x-coordinate and y-coordinate and dice top position
        :param x: current x-coordinate
        :param y: current y-coordinate
        :param diceTop: The dice top position
        :return: True if it's goal else False
        """
        return self.goalPos == (x, y) and diceTop == 1

    def isGoalLocation(self, x, y):
        """
        It checks whether the current node location is a goal node location
        :param x: current x-coordinate
        :param y: current y-coordinate
        :return: True if it's the goal location else False
        """
        return self.goalPos == (x, y)

    def getStartPos(self):
        """
        A getter method to get the starting position
        :return: starting position as tuple ( x-coordinate, y-coordinate )
        """
        return self.startingPos

    def getGoalPos(self):
        """
        A getter method to get the goal position
        :return: goal position as tuple ( x-coordinate, y-coordinate )
        """
        return self.goalPos

    def updateMaze(self, x, y, symbol):
        """
        It will update the current position we are in maze with character pound to
        track the path
        :param symbol: Node name
        :param x: current x-coordinate
        :param y: current y-coordinate
        :return: None
        """
        self.mazeOrientation[x][y] = symbol

    def printMaze(self):
        """
        It prints the current maze configuration.
        :return: None
        """
        for i in range(self.height - 1, -1, -1):
            for j in range(self.width):
                print(self.mazeOrientation[j][i], end=" ")
            print()


def loadMaze(fileName):
    """
    It reads the maze text file and return the 2-D array
    :param fileName: A maze text file
    :return: A 2-D array
    """
    layout = open(fileName)
    try:
        return [line.strip() for line in layout]
    finally:
        layout.close()
