"""
File: priorityQueue.py
Language: Python 3.5.1
Author: Deepak Sharma ( ds5930@rit.edu )
        Karan Jariwala( kkj1811@rit.edu )
        Aravindh Kupusamy ( axk8776@rit.edu )

Description: The priorityQueue.py file represents the priority queue as a list
             and methods to operate on it
"""

__author__ = "Deepak Sharma, Karan Jariwala, Aravindh Kuppusamy"


class PriorityQueue:
    """
    This class represents a priority queue as a list
    """
    __slots__ = 'queue', 'nodesPutOnQueue', 'nodesTakenOff'

    def __init__(self):
        """
        A parameterless constructor which initializes the queue, number of
        nodes added into the queue, and number of nodes remove from the queue.
        """
        self.queue = list()
        self.nodesPutOnQueue = 0
        self.nodesTakenOff = 0

    def insert(self, node):
        """
        It will insert a node in a queue at the end location and call the
        heapify method to bubbleUp the value in the queue.
        :param node: A node object
        :return:
        """
        self.queue.append(node)
        self.nodesPutOnQueue += 1
        self.__heapify(len(self.queue) - 1)

    def replace(self, node, location):
        """
        It will replace the old node with the current node object at the
        location provided and calls the heapify method to bubbleUp the value
        in the queue.
        :param node: A node object
        :param location: The location for which to swap the node object
        :return: None
        """
        self.queue.insert(node, location)
        self.__heapify(location - 1)

    def pop(self):
        """
        Remove the zero index location node from the queue, insert the last
        index location node to the zero index location and calls the
        bubbleDown method to rearrange the node in ascending order
        :return: Zero index location node which we removed first
        """
        if len(self.queue) > 0:
            node = self.queue.pop(0)
            self.nodesTakenOff += 1
            if len(self.queue) > 0:
                self.queue.insert(0, self.queue.pop(-1))
                self.__bubble_down(0)
            return node

    def __heapify(self, loc):
        """
        It compares the value from that location to up the tree or till front
        of the tree unless a property is satisfy which says the parent node F
        cost value should be less than the child node F cost value
        :param loc: location from which heapify operation perform
        :return: None
        """
        while loc > 0:
            parent_loc = self.getParent(loc)
            if self.queue[loc].getFCost() < self.queue[parent_loc].getFCost():
                self.queue[loc], self.queue[parent_loc] = self.queue[parent_loc], self.queue[loc]
                loc = parent_loc
            else:
                break

    def __bubble_down(self, loc):
        """
        It compares the value from that location down the tree or queue unless
        a property is satisfy which says the parent node F cost value should
        be less than the child node F cost value
        :param loc: location from which bubble down operation perform
        :return: None
        """
        while 2 * loc + 1 <= len(self.queue) - 1:
            swap_loc = self.__get_min_neighbour(loc)
            if swap_loc == loc:
                break
            else:
                self.queue[loc], self.queue[swap_loc] = self.queue[swap_loc], self.queue[loc]
                loc = swap_loc

    def __get_min_neighbour(self, loc):
        """
        It returns the location of the child which is having minimum F cost
        if it founds one.
        :param loc: Location of parent in a queue
        :return: minimum F cost location of a node
        """
        child1 = self.queue[2 * loc + 1]
        if len(self.queue) - 1 < 2 * loc + 2:
            min_val = min(self.queue[loc].getFCost(), child1.getFCost())
            if self.queue[loc].getFCost() == min_val:
                return loc
            elif child1.getFCost() == min_val:
                return 2 * loc + 1

        else:
            child2 = self.queue[2 * loc + 2]
            min_val = min(self.queue[loc].getFCost(), child1.getFCost(), child2.getFCost())
            if self.queue[loc].getFCost() == min_val:
                return loc
            elif child1.getFCost() == min_val:
                return 2 * loc + 1
            else:
                return 2 * loc + 2

    def find(self, node):
        """
        It finds the location of the node inside the queue
        :param node: A node object
        :return: returns the location of the node if found else None
        """
        for loc in range(len(self.queue)):
            if node is self.queue[loc]:
                return loc
        return None

    def update(self, node):
        """
        It finds the location of the node inside the queue and bubbleUp
        the value in the queue to satisfy the heap property
        :param node: A node object
        :return: None
        """
        loc = self.find(node)
        self.__heapify(loc)

    def isEmpty(self):
        """
        It checkts whether the queue is empty or not
        :return: True if empty else False
        """
        return len(self.queue) == 0

    def getParent(self, loc):
        """
        It returns the parent location from the queue
        :param loc: location of child
        :return: location of parent
        """
        return (loc - 1) // 2