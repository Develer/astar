"""
A* search algorithm simple implementation
"""

from map_types import Cell


class PathFinder():

    def __init__(self, world):
        self.world = world

    def G(self, cell, parent):
        if parent is None:
            print "parent cell is None"
            return 0
        x, y = parent.point
        point = cell.point
        if (point == (x-1, y) or
            point == (x+1, y) or
            point == (x, y+1) or
            point == (x, y-1)):
            return 10
        if (point == (x-1, y+1) or
            point == (x+1, y+1) or
            point == (x-1, y-1) or
            point == (x+1, y-1)):
            return 14
    
    def H(self, cell, finish):
        xc, yc = cell.point
        xf, yf = finish.point
        h = 10 * (abs(xc-xf) + abs(yc-yf))
        return h

    def near_cells(self, cell):
        x, y = cell.point
        near_cells = [
            (x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y),
            (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)
        ]
        return near_cells

    def find_path(self):
        # Calc start params and add start to open_list
        self.world.start.G = self.G(self.world.start, self.world.start.parent)
        self.world.start.H = self.H(self.world.start, self.world.finish)
        self.world.start.F = self.world.start.G + self.world.start.H
        self.world.add_to_open_list(self.world.start)
        while not self.world.open_list_is_empty():
            # print "Open list"
            # for i, j in self.world._open_list.items():
            #     print "Cell=%s H=%d, G=%d, F=%d" % (i, j.H, j.G, j.F)
            # print "Closed list"
            # for i, j in self.world._closed_list.items():
            #     print "Cell=%s H=%d, G=%d, F=%d" % (i, j.H, j.G, j.F)
            # import pdb;pdb.set_trace()
            # from time import sleep;sleep(0.01)
            if self.world.cell_in_open_list(self.world.finish):
                print "Path found!"
                # Compose path
                import pdb;pdb.set_trace()
                return
            curr_cell = self.world.get_minF_cell()
            self.world.move_to_closed_list(curr_cell)
            near_cells = self.near_cells(curr_cell)
            for cell in near_cells:
                near_cell = self.world.field[cell]
                if (not near_cell.is_wall and \
                    not self.world.cell_in_closed_list(near_cell)):
                    if not self.world.cell_in_open_list(near_cell):
                        near_cell.parent = curr_cell
                        near_cell.G = curr_cell.G + self.G(near_cell, curr_cell)
                        near_cell.H = self.H(near_cell, self.world.finish)
                        near_cell.F = near_cell.G + near_cell.H
                        self.world.add_to_open_list(near_cell)
                    else:
                        if near_cell.G > curr_cell.G + self.G(near_cell, curr_cell):
                            near_cell.parent = curr_cell
                            near_cell.G = curr_cell.G + self.G(near_cell, curr_cell)
                            near_cell.F = near_cell.G + near_cell.H
        print "Path not found!"