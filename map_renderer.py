from visual import scene, curve, box, color, arrow, label


class VPythonRenderer():

    def draw_axes(self):
        # scene.forward = (0, 0, -1) # Default view direction
        zero = (0, 0, 0)
        x_direction = (5, 0, 0)
        y_direction = (0, 5, 0)
        z_direction = (0, 0, 5)
        # Axis X
        pointerX = arrow(pos=zero, axis=x_direction,
                         shaftwidth=0.5, color=color.red)
        labelX = label(pos=x_direction, text='X')
        # Axis Y
        pointerY = arrow(pos=zero, axis=y_direction,
                         shaftwidth=0.5, color=color.blue)
        labelY = label(pos=y_direction, text='Y')
        # Axis Z
        pointerZ = arrow(pos=zero, axis=z_direction,
                         shaftwidth=0.5, color=color.yellow)
        labelZ = label(pos=z_direction, text='Z')

    def draw_grid(self, width, length):
        scene.center = (int(width / 2), int(length / 2))
        scene.forward = (0, 0, -1) # Default view direction
        for x in range(-5, width * 10 + 5, 10):
            curve(pos=[(x / 10 + 0.5, -0.5), (x / 10 + 0.5, length - 0.5)],
                  color=color.green)
        for y in range(-5, length * 10 + 5, 10):
            curve(pos=[(-0.5, y / 10 + 0.5), (width - 0.5, y / 10 + 0.5)],
                  color=color.green)

    def draw_walls(self, cells):
        for cell in cells:
            if cell.is_wall:
                box(pos=(cell.x, cell.y, 0.5),
                    width=1, length=1, heigth=1, color=color.blue)

    def draw_path(self, path):
        for cell in path:
            self.draw_cell(cell, color.green)
            
    def draw_calculated_cells(self, closed_list, open_list):
        for cell in closed_list:
            self.draw_cell(cell, color.yellow)
        for cell in open_list:
            self.draw_cell(cell, color.cyan)
                    
    def draw_start(self, start):
        self.draw_cell(start, color.white)

    def draw_finish(self, finish):
        self.draw_cell(finish, color.red)
        
    def draw_cell(self, cell, clr):
        box(pos=(cell.x, cell.y, 0.5),
            width=1, length=1, heigth=1, color=clr)
