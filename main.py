import os

from map_types import Map, Cell
from path_finder import PathFinder


def main():
    # Create AStar map
    world = Map()
    # Load map from bmp file
    bmp_path = os.path.join(os.getcwd(), 'map2.bmp')
    world.load_map(bmp_path)

    # world.start = Cell(1, 20)
    # world.finish = Cell(85, 20)
    world.start = Cell(1, 1)
    world.finish = Cell(700, 350)
    # world.start = Cell(1, 1)
    # world.finish = Cell(6, 6)

    world.draw_map()

    a_star_algorithm = PathFinder(world)
    a_star_algorithm.find_path()

if __name__ == "__main__":
    main()
