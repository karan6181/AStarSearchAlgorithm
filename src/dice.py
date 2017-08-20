"""
File: dice.py
Language: Python 3.5.1
Author: Karan Jariwala( kkj1811@rit.edu )
        Aravindh Kuppusamy ( axk8776@rit.edu )
        Deepak Sharma ( ds5930@rit.edu )
Description: Representation of the dice configuration and
             methods to change the configurations
"""

__author__ = "Karan Jariwala, Aravindh Kuppusamy, and Deepak Sharma"


class Dice:
    """
    A dice will have six unique faces. But here we represent a dice with
    just 3 faces, since we can deduce the other 3 from these.
    """
    __slots__ = ("top", "right", "north", "sum")

    def __init__(self, top =1, right=3, north=2):
        """
        This will initialize the six unique dice position.
        :param top: The top face of a dice
        :param right: The right face of a dice
        :param north: The north face of a dice
        """
        self.top = top
        self.right = right
        self.north = north
        self.sum = 7

    def moveRight(self):
        """
        Shift the dice one position to the right.
        :return: None
        """
        self.top, self.right = self.sum - self.right, self.top

    def moveLeft(self):
        """
        Shift the dice one position to the left.
        :return: None
        """
        self.top, self.right = self.right, self.sum - self.top

    def moveNorth(self):
        """
        Shift the dice one position to the north.
        :return: None
        """
        self.top, self.north = self.sum - self.north, self.top

    def moveSouth(self):
        """
        Shift the dice one position to the south.
        :return: None
        """
        self.top, self.north = self.north, self.sum - self.top

    def move(self, moveName):
        """
        Move the dice based on the string provided.
        :param moveName: String name based on available function
        :return: None
        """
        if moveName == 'moveLeft':
            self.moveLeft()
        elif moveName == 'moveRight':
            self.moveRight()
        elif moveName == 'moveSouth':
            self.moveSouth()
        elif moveName == 'moveNorth':
            self.moveNorth()

    def display(self):
        """
        Display the dice configuration.
        :return: None
        """
        print("\t ", self.north, end="")
        print("\t" * 7, "NORTH")
        print("\t ", "|", end="")
        print("\t " * 7, "|")
        print(self.sum - self.right, "-", self.top, "/", self.sum - self.top, "-", self.right, end="")
        print("\t" * 2, "LEFT", "-", "TOP", "/", "BOTTOM", "-", "RIGHT")
        print("\t ", "|", end="")
        print("\t " * 7, "|")
        print("\t ", self.sum - self.north, end="")
        print("\t" * 7, "SOUTH", end="\n")
