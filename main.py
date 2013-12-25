import os

from map_types import Map, Point


def main():
    # Create AStar map
    astar_map = Map()
    # Load map from bmp file
    bmp_path = os.path.join(os.getcwd(), 'map.bmp')
    astar_map.load_map(bmp_path)

    astar_map.start = Point(1, 20)
    astar_map.finish = Point(85, 20)
    astar_map.draw_map()
    astar_map.find_path()
    astar_map.draw_path()
    
    # Optional drawing
    astar_map.draw_calculated_cells()

if __name__ == "__main__":
    main()