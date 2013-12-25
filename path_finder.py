"""
A* search algorithm simple implementation
"""


class PathFinder():

    def __init__(self, start, finish, astar_map):
        self.start = start
        self.finish = finish
        self.astar_map = astar_map