from PIL import Image
from xml.dom import minidom

from map_renderer import VPythonRenderer


class Cell():

    def __init__(self, x, y, is_wall=False,
                 G=None, H=None, F=None, parent=None):
        self.x = x
        self.y = y
        self.is_wall = is_wall
        self.G = G
        self.H = H
        self.F = F
        self.parent = parent


class Map():
    
    def __init__(self):
        self.__canvas = VPythonRenderer()
        self.width = 0
        self.length = 0
        
        self.start = None
        self.finish = None
        
        self.field = {}
        self._closed_list = {}
        self._open_list = {}
        self.path = []

    def load_map(self, path):
        image = Image.open(path)
        if (image.mode != "RGB"):
            print "Image object not in RGB mode!"
            return
        self.width = image.size[0]
        self.length = image.size[1]
        for x in range(self.width):
            for y in range(self.length):
                point = (x, y)
                rgb = image.getpixel(point)
                if (rgb[0] < 255 and rgb[1] < 255 and rgb[2] < 255):
                    cell = Cell(x, y, is_wall=True)
                else:
                    cell = Cell(x, y, is_wall=False)
                self.field[point] = cell

    def draw_map(self):
        # self.__canvas.draw_axes()
        self.__canvas.draw_grid(self.width, self.length)
        self.__canvas.draw_walls(self.field)
        self.__canvas.draw_start(self.start)
        self.__canvas.draw_finish(self.finish)

    def open_list_is_empty(self):
        if self._open_list:
            return False
        return True

    def cell_in_open_list(self, cell):
        if self._open_list.has_key((cell.x, cell.y)):
            return True
        return False

    def cell_in_closed_list(self, cell):
        if self._closed_list.has_key((cell.x, cell.y)):
            return True
        return False

    def add_to_open_list(self, cell):
        self._open_list[(cell.x, cell.y)] = cell
        if (cell.x, cell.y) != (self.start.x, self.start.y) and \
            (cell.x, cell.y) != (self.finish.x, self.finish.y):
            self.__canvas.draw_open_list_cell(cell)

    def add_to_closed_list(self, cell):
        self._closed_list[(cell.x, cell.y)] = cell
        if (cell.x, cell.y) != (self.finish.x, self.finish.y) and \
            (cell.x, cell.y) != (self.start.x, self.start.y):
            self.__canvas.draw_closed_list_cell(cell)

    def remove_from_open_list(self, cell):
        del self._open_list[(cell.x, cell.y)]
        if (cell.x, cell.y) != (self.start.x, self.start.y) and \
            (cell.x, cell.y) != (self.finish.x, self.finish.y):
            self.__canvas.hide_cell(cell)

    def get_minF_cell(self):
        return min(self._open_list.values(),
                   key=lambda cell: cell.F)

    def move_to_closed_list(self, cell):
        self.remove_from_open_list(cell)
        self.add_to_closed_list(cell)
