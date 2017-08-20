"""
File: rdMaze.py
Language: Python 3.5.1
Author: Aravindh Kuppusamy (axk8776@g.rit.edu)
        Deepak Sharma (ds5930@g.rit.edu)
        Karan Jariwala (kkj1811@g.rit.edu)
Description: Rolling Die Maze game using A* search algorithm along with its
             problem representation
"""

import sys
import numpy as np
import matplotlib.pyplot as plot
from maze import *
from dice import Dice
from node import Node
from heuristic import Heuristic
from priorityQueue import PriorityQueue


__author__ = 'Aravindh Kuppusamy, Deepak Sharma, Karan Jariwala'


class Problem:
    """
    A search problem defines the state space, start state, goal state, goal test,
    successor function and cost function. This search problem can be used to find
    paths to a particular point on the maze.
    """

    __slots__ = 'maze'

    def __init__(self, maze):
        """
        Initializes the problem with state space as a representation of the maze.
        :param maze: Default Maze representation.
        """
        self.maze = maze

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        x, y = self.maze.getStartPos()
        if (x, y, 1, 3, 2) not in self.maze.nodeMap.keys():
            aDice = Dice()
            aNode = Node(self.maze, aDice, 'S', 0, None, x, y, None)
            self.maze.nodeMap[(x, y, 1, 3, 2)] = aNode
        return self.maze.nodeMap[(x, y, 1, 3, 2)]

    def getSuccessors(self, state):
        """
        :param state: Search state

        For a given state, this should return a Node object which has maze,
        current position, dice orientation at that position, gCost, fCost and
        its parent.
        """
        return state.getSuccessorState()

    def isGoalState(self, state):
        """
        Returns whether the state is a goal state or not!
        :param state: Search state
        :return : Boolean
        """
        return state.getName() == 'G' and state.dice.top == 1

    def getGoalState(self):
        """
        Returns the goal state for the search problem.
        """
        x, y = self.maze.getGoalPos()
        if (x, y, 1) not in self.maze.nodeMap.keys():
            aDice = Dice()
            aNode = Node(self.maze, aDice, 'G', None, None, x, y, None)
            self.maze.nodeMap[(x, y, 1)] = aNode
        return self.maze.nodeMap[(x, y, 1)]

    def getStartPosition(self):
        """
        Returns the start position in the maze for the search problem.
        """
        return self.maze.getStartPos()

    def getGoalPosition(self):
        """
        Returns the goal position in the maze for the search problem.
        """
        return self.maze.getGoalPos()

    def getCostOfActions(self, actions = None):
        """
        Returns the gCost of a sequence of legal actions.
        """
        return 1


def aStarSearch(problem, heuristicName, fringe, visitedNodes):
    """
    Search the nodes which is having the lowest fCost which is equal to the
    actual cost (gCost) and the heuristic cost(hCost) which is provided by
    the heuristics.
    :param visitedNodes: States that has been visited once. i.e., states whose
           children have been generated
    :param fringe: Priority Queue in which the nodes have been put up
    :param heuristicName: The heuristic which is to be used in helping A*
           search algorithm
    :param problem: A problem consist of initial state, goal test, successor
                    functions and a path cost
    """

    startState = problem.getStartState()
    heuristic = getattr(Heuristic, heuristicName)
    startState.setFCost(0 + heuristic(startState, problem))
    fringe.insert(startState)

    while not fringe.isEmpty():
        curState = fringe.pop()

        if problem.isGoalState(curState):
            print('SUCCESS')
            visitedNodes.add(curState)
            return curState

        if curState not in visitedNodes:
            visitedNodes.add(curState)

            for childState in problem.getSuccessors(curState):
                # Check whether the node is in fringe
                # If it is in fringe and new cost is less than the previously estimated one
                #   then change its cost and parent
                # Rearrange the nodes in heap

                if childState not in visitedNodes:

                    if childState in fringe.queue:

                        location = fringe.find(childState)
                        tempNode = fringe.queue[location]
                        childStateFCost = curState.getGCost() + problem.getCostOfActions() + \
                                          heuristic(childState, problem)

                        if childStateFCost < tempNode.getFCost():
                            childState.setGCost(curState.getGCost() + problem.getCostOfActions())
                            hDist = heuristic(childState, problem)
                            childState.setFCost(childState.getGCost() + hDist)
                            childState.setParent(curState)
                            fringe.update(childState)
                    else:
                        childState.setGCost(curState.getGCost() + problem.getCostOfActions())
                        hDist = heuristic(childState, problem)
                        childState.setFCost(childState.getGCost() + hDist)
                        fringe.insert(childState)

    print("FAILURE")
    return None


class Game:
    """
    The game class consist of initializing the parameters and run the a star
    search algorithm on the provided maze file and print the output on the
    console.
    """
    @staticmethod
    def run(layout, heuristic):
        """
        It initialize the configuration parameters and run the a star
        algorithm on the maze data and gets the output.
        :param layout: Two dimensional array of maze configuration
        :param heuristic: Type of heuristic
        :return: return a list which contains heuristic name, number of moves
                 it took, number of node generated and visited
        """
        layoutText = loadMaze(layout)
        currentMaze = Maze(layoutText)
        aMaze = Maze(layoutText)
        aProblem = Problem(aMaze)
        numberOfMoves = 0

        fringe = PriorityQueue()
        visitedNodes = set()

        goal = aStarSearch(aProblem, heuristic, fringe, visitedNodes)
        path = list()

        while goal is not None:
            path.insert(0, goal)
            numberOfMoves += 1
            goal = goal.getParent()

        move = 0
        print("For Heuristics: ", heuristic)
        if len(path) > 0:
            print("|------------- STARTING MAZE--------------|\n")
            currentMaze.updateMaze(path[0].getxCoordinate(), path[0].getyCoordinate(), "S")
            currentMaze.printMaze()
            print("\n|------------- STARTING DICE ORIENTATION--------------|\n")
            path[0].dice.display()

        for currentNode in path:

            print("\n|==================== MOVE: " + str(move) + "====================|\n")
            print("|------------- MAZE--------------|\n")
            currentMaze.updateMaze(currentNode.getxCoordinate(), currentNode.getyCoordinate(), '#')
            currentMaze.printMaze()
            print("\n|------------- DICE--------------|\n")
            currentNode.dice.display()
            move += 1

        print("\n|---------------- PERFORMANCE METRICS -----------------|\n")
        print("No. of moves in the solution                    : ", numberOfMoves - 1)
        print("No. of nodes put on the queue                   : ", fringe.nodesPutOnQueue)
        print("No. of nodes visited / removed from the queue   : ", len(visitedNodes))
        print("\n|------------------------------------------------------|\n")

        result = [heuristic, numberOfMoves - 1, fringe.nodesPutOnQueue, len(visitedNodes)]
        return result


def plots(results):
    """
    Plot the graph with y-axis as number of nodes generated and visited vs
    x-axis as type of heuristics
    :param results: a list which contains heuristic name, number of moves
                    it took, number of node generated and visited
    :return: None
    """
    bars = len(results)
    heuristic = [results[counter][0] for counter in range(len(results))]
    nodesPutOnQueue = [results[counter][2] for counter in range(len(results))]
    visitedNodes = [results[counter][3] for counter in range(len(results))]

    plot.subplots()
    index = np.arange(bars)
    bars_width = 0.25
    opacity = 1
    plot.bar(index, nodesPutOnQueue, bars_width, alpha=opacity, color='g', label = 'Nodes Generated')
    plot.bar(index + bars_width, visitedNodes, bars_width, alpha=opacity, color='y', label='Nodes Visited')
    plot.xlabel('Heuristic')
    plot.ylabel('Number of Nodes')
    plot.title('Heuristic Performance')
    plot.xticks(index + bars_width, heuristic )
    plot.legend( loc="upper left" )
    plot.show()


def main():
    """
    A main method which takes the parameter from the user and perform a star
    algorithm
    :return: None
    """
    results = []
    print(sys.argv)
    if len(sys.argv) == 3:
        layout = sys.argv[1]
        heuristic = sys.argv[2]
        results.append(Game().run(layout, heuristic))
    elif len(sys.argv) == 2:

        layout = sys.argv[1]
        heuristics = ['fancy_manhattan', 'manhattan', 'euclidean', 'diagonal']
        for heuristic in heuristics:
            results.append(Game.run(layout, heuristic))

    else:
        layout = input("Please enter the filename( e.g: map1.txt ): ")
        heuristic = input("Please enter the heuristic( 'fancy_manhattan', 'manhattan', 'euclidean', 'diagonal' ): ")
        results.append(Game().run(layout, heuristic))
    plots(results)

if __name__ == '__main__':
    main()
