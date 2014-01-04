import os

from map_types import Map, Cell
from path_finder import PathFinder


def main():
    # Create AStar map
    astar_map = Map()
    # Load map from bmp file
    bmp_path = os.path.join(os.getcwd(), 'map.bmp')
    astar_map.load_map(bmp_path)

    astar_map.start = Cell(1, 20)
    astar_map.finish = Cell(85, 20)
    astar_map.draw_map()

    a_star_algorithm = PathFinder(astar_map)
    a_star_algorithm.find_path()


if __name__ == "__main__":
    main()