"""
File: heuristic.py
Language: Python 3.5.1
Author: Aravindh Kuppusamy (axk8776@g.rit.edu)
        Deepak Sharma (ds5930@g.rit.edu)
        Karan Jariwala (kkj1811@g.rit.edu)
Description: Various heuristic functions that returns the heuristic distance
             from one state to the goal state.
"""

import copy
import math

__author__ = 'Aravindh Kuppusamy, Deepak Sharma, Karan Jariwala'


class Heuristic:
    """
    The class Heuristic contains all the static methods to calculate
    various heuristics.
    """

    @staticmethod
    def manhattan(curState, problem):
        """
        The Manhattan distance heuristic for the current state.
        :param curState: The current search state
        :param problem: The A* search problem instance for this maze
        :return: The Manhattan distance between the current's state position &
                 goal position
        """

        # Manhattan distance is the sum of the vertical and horizontal
        # distances between two points.
        pos1 = curState.getPos()
        pos2 = problem.getGoalPosition()
        dx, dy = Heuristic.finddXdY(pos1, pos2)
        return dx + dy

    @staticmethod
    def euclidean(curState, problem):
        """
        The Euclidean distance heuristic for the current state.
        :param curState: The current search state
        :param problem: The A* search problem instance for this maze
        :return: The Euclidean distance between the current's state position &
                 goal position
        """

        # Euclidean distance is the distance of the straight line that
        # connects two points.
        pos1 = curState.getPos()
        pos2 = problem.getGoalPosition()
        dx, dy = Heuristic.finddXdY(pos1, pos2)
        return math.sqrt(dx * dx + dy * dy)

    @staticmethod
    def diagonal(curState, problem):
        """
        The Diagonal distance heuristic for the current state.
        :param curState: The current search state
        :param problem: The A* search problem instance for this maze
        :return: The Diagonal distance between the current's state position &
                 goal position
        """
        pos1 = curState.getPos()
        pos2 = problem.getGoalPosition()
        dx, dy = Heuristic.finddXdY(pos1, pos2)
        return min(dx, dy) * math.sqrt(2) + abs(dx - dy)

    @staticmethod
    def finddXdY(pos1, pos2):
        """
        Calculates the Horizontal and Vertical distances between two points.
        :param pos1: First position
        :param pos2: Second Position
        :return: The Diagonal distance between the current's state position &
                 goal position
        """
        dx = abs(pos1[0] - pos2[0])
        dy = abs(pos1[1] - pos2[1])
        return dx, dy

    @staticmethod
    def fancy_manhattan(curState, problem):
        """The fancy Manhattan distance heuristic for the current state.
        :param curState: The current search state
        :param problem: The A* search problem instance for this maze
        :return: The Manhattan distance between the current's state position &
                 goal position with additional award based on success rate of
                 passing goal test
        """
        manhattanDist = Heuristic.manhattan(curState, problem)
        pos1 = curState.getPos()
        pos2 = problem.getGoalPosition()
        dx = (pos1[0] - pos2[0])
        dy = (pos1[1] - pos2[1])

        rewardA = rewardB = 0

        if abs(dx) < 2 or abs(dy) < 2:

            temp_dice = copy.deepcopy(curState.getDice())
            if dx > 0:
                for moves in range(abs(dx) % 4):
                    temp_dice.moveLeft()
            else:
                for moves in range(abs(dx) % 4):
                    temp_dice.moveRight()
            if dy > 0:
                for moves in range(abs(dy) % 4):
                    temp_dice.moveNorth()
            else:
                for moves in range(abs(dy) % 4):
                    temp_dice.moveSouth()

            if temp_dice.top == 1:
                rewardA = -.50

            temp_dice = copy.deepcopy(curState.getDice())
            if dy > 0:
                for moves in range(abs(dy) % 4):
                    temp_dice.moveNorth()
            else:
                for moves in range(abs(dy) % 4):
                    temp_dice.moveSouth()
            if dx > 0:
                for moves in range(abs(dx) % 4):
                        temp_dice.moveLeft()
            else:
                for moves in range(abs(dx) % 4):
                    temp_dice.moveRight()

            if temp_dice.top == 1:
                rewardB = -.50

        return manhattanDist + min(rewardA, rewardB)

    @staticmethod
    def forecast_manhattan(curState, problem):
        """The Forecast Manhattan distance heuristic for the current state.
        :param curState: The current search state
        :param problem: The A* search problem instance for this maze
        :return: The Manhattan distance between the current's state position &
                 goal position with additional penalty based on success rate
                 of neighbour's legality.
        """
        manhattanDist = Heuristic.manhattan(curState, problem)
        neighbours = problem.maze.getValidNeighbors(curState.getxCoordinate(),
                                                    curState.getyCoordinate(),
                                                    curState.getDice())
        validNeighbours = [neighbour for neighbour in neighbours
                           if neighbour[2] != 6]

        totalPenalty = 0
        if len(validNeighbours) == 1:
            return manhattanDist + 1

        # penalty = []
        # for childState in validNeighbours:
        #     childDice = Dice(childState[2], childState[3], childState[4])
        #     temp = problem.maze.getValidNeighbors(childState[0], childState[1], childDice)
        #     validChildNeighbours = [childNeighbour for childNeighbour in temp if childNeighbour[2] != 6]
        #     penalty += [1 if len(validChildNeighbours) == 1 else 0]
        #
        # childPenalty = len([p for p in penalty if p == 1])
        #
        # if len(validNeighbours) == childPenalty:
        #     totalPenalty = 2
        # else:
        #     totalPenalty = 1 + childPenalty * .2

        return manhattanDist + totalPenalty