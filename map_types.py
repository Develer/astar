from PIL import Image
from xml.dom import minidom

from map_renderer import VPythonRenderer
from path_finder import PathFinder


class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Cell():

    def __init__(self, point, is_wall=False):
        self.point = point
        self.is_wall = is_wall


class AStarCell():

    def __init__(self, cell, parent=None):
        self.cell = cell
        self.parent = parent


class Map():
    
    def __init__(self):
        self.__canvas = VPythonRenderer()
        self.width = 0
        self.length = 0
        
        self.start = None
        self.finish = None
        
        self.list_of_cells = []
        self.path = []
        self.closed_list = []
        self.open_list = []

    def load_map(self, path):
        image = Image.open(path)
        if (image.mode != "RGB"):
            print "Image object not in RGB mode!"
            return
        self.width = image.size[0]
        self.length = image.size[1]
        for x in range(self.width):
            for y in range(self.length):
                point = Point(x, y)
                xy = (x, y)
                rgb = image.getpixel(xy)
                if (rgb[0] < 255 and rgb[1] < 255 and rgb[2] < 255 ):
                    cell = Cell(point, is_wall=True)
                else:
                    cell = Cell(point, is_wall=False)
                self.list_of_cells.append(cell)

    def draw_map(self):
        self.__canvas.draw_axes()
        self.__canvas.draw_grid(self.width, self.length)
        self.__canvas.draw_walls(self.list_of_cells)

    def draw_path(self):
        self.__canvas.draw_path(self.path)
        self.__canvas.draw_start(self.start)
        self.__canvas.draw_finish(self.finish)
    
    def draw_calculated_cells(self):
        self.__canvas.draw_calculated_cells(self.closed_list, self.open_list)
    
    def find_path(self):
        path_finder = PathFinder(
            self.start, self.finish, self.list_of_cells)
        # result = path_finder.find_path()
        # self.path = result[0]
        # self.closed_list = result[1]
        # self.open_list = result[2]