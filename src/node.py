"""
File: node.py
Language: Python 3.5.1
Author: Karan Jariwala( kkj1811@rit.edu )
        Aravindh Kuppusamy ( axk8776@rit.edu )
        Deepak Sharma ( ds5930@rit.edu )
Description: Representation of the state configuration and methods
             to operate on it.
"""

from dice import Dice

__author__ = "Karan Jariwala, Aravindh Kuppusamy, Deepak Sharma"


class Node:
    """
    This class represents the state configuration which includes
    x-coordinate, y-coordinate, g cost, f cost, parent reference,
    current dice configuration, and maze configuration
    """
    __slots__ = ('maze', 'dice', '__name', '__gCost', '__fCost', '__x', '__y', 'parent')

    def __init__(self, maze, dice, name, gCost, fCost, x, y, parent):
        """
        A paramterized constructor to initialize the parameters.
        :param maze: A maze configuration
        :param dice: A dice configuration
        :param name: The name according the current position in a maze
        :param gCost: Actual cost from starting node to current node
        :param fCost: Addition of g cost and h cost
        :param x: x-coordinate of the current position in a maze
        :param y: y-coordinate of the current position in a maze
        :param parent: The parent node's reference
        """
        self.__name = name
        self.__gCost = gCost
        self.__fCost = fCost
        self.__x = x
        self.__y = y
        self.parent = parent
        self.maze = maze
        self.dice = dice

    def getName(self):
        """
        The getter method to return the name of the node
        :return: It returns a name
        """
        return self.__name

    def getParent(self):
        """
        The getter method which returns the parent node reference
        :return: parent node reference
        """
        return self.parent

    def getxCoordinate(self):
        """
        The getter method to return the current position's x-coordinate inside
        a maze
        :return: current x-coordinate
        """
        return self.__x

    def getyCoordinate(self):
        """
        The getter method to return the current position's y-coordinate inside
        a maze
        :return: current y-coordinate
        """
        return self.__y

    def getPos(self):
        """
        The getter method to return the current position's x-coordinate and
        y-coordinate inside a maze
        :return: tuple of x-coordinate and y-coordinate
        """
        return self.__x, self.__y

    def getFCost(self):
        """
        The getter method to return the f cost
        :return: f cost
        """
        return self.__fCost

    def getGCost(self):
        """
        The getter method to return the g cost
        :return: g cost
        """
        return self.__gCost

    def getDice(self):
        """
        The getter method to get the current dice configurations
        :return: current dice configuration object
        """
        return self.dice

    def __str__(self):
        """
        The string representation of the node object which will return
        name of the nodes, current position of the node, the f cost, and
        the dice top position
        :return: string representation of name of the nodes, current position
                 of the node, the f cost, and the dice top position
        """
        return "(Symbol: '" + str(self.getName()) + \
               "' Position: (" + str(self.__x) + "," + str(self.__y) + \
               ") Cost: " + str(self.__fCost) + \
               " DiceTop: " + str(self.dice.top) + ")"

    def setName(self, name):
        """
        The setter method to set the name of the node
        :param name: A string type name
        :return: None
        """
        self.__name = name

    def setParent(self, node):
        """
        The setter method to set the parent reference
        :param node: The parent node
        :return: None
        """
        self.parent = node

    def setFCost(self, cost):
        """
        The setter method to set the f cost of the node
        :param cost: f cost
        :return: None
        """
        self.__fCost = cost

    def setGCost(self, cost):
        """
        The setter method to set the g cost of the node
        :param cost: g cost
        :return: None
        """
        self.__gCost = cost

    def getSuccessorState(self):
        """
        This method returns the list of valid neighbors. Below are the steps
        it performed:
        1. Extracts the current node neighbors which excludes the obstacles
           neighbors
        2. If the neighbor is already in the dictionary, then return the
           reference node point instead of creating a new node.
        3. Otherwise, create a new node with the current configurations and
           add it to the list of neighbors if current dice top position is
           not 6.
        :return: List of valid neighbors which excludes obstacles and current
        dice top position 6.
        """
        successors = list()
        neighbors = self.maze.getValidNeighbors(self.__x, self.__y, self.dice)

        for neighbor in neighbors:
            if neighbor in self.maze.nodeMap.keys():
                if self.maze.nodeMap[neighbor].getName() == 'G':
                    goal_parent = self.maze.nodeMap[neighbor].getParent()
                    if goal_parent is None:
                        self.maze.nodeMap[neighbor].setParent(self)
                successors.append(self.maze.nodeMap[neighbor])
            else:
                x, y = neighbor[0], neighbor[1]
                neighborDice = Dice(neighbor[2], neighbor[3], neighbor[4])
                if self.maze.isGoal(x, y, neighborDice.top):
                    name = 'G'
                elif self.maze.getStartPos == (x, y):
                    name = 'S'
                else: name = '.'
                if neighborDice.top != 6:
                    # Avoiding the goal location with wrong configuration
                    if self.maze.isGoalLocation(x, y) and \
                            not self.maze.isGoal(x, y, neighborDice.top):
                        continue
                    aNode = Node(self.maze, neighborDice, name, None, None, x, y, self)
                    self.maze.nodeMap[neighbor] = aNode
                    successors.append(aNode)

        return successors