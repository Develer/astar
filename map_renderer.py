from visual import scene, curve, box, color, arrow, label


class VPythonRenderer():

    def draw_axes(self):
        # scene.forward = (0, 0, -1) # Default direction
        pointerX = arrow(pos=(0,0,0), axis=(5,0,0), shaftwidth=0.5, color=color.red)
        label(pos=(5,0,0), text='X')
        pointerY = arrow(pos=(0,0,0), axis=(0,5,0), shaftwidth=0.5, color=color.blue)
        label(pos=(0,5,0), text='Y')
        pointerZ = arrow(pos=(0,0,0), axis=(0,0,5), shaftwidth=0.5, color=color.yellow)
        label(pos=(0,0,5), text='Z')

    def draw_grid(self, width, length):
        scene.center = (int(width / 2), int(length / 2))
        scene.forward = (0, 0, -1) # Default direction
        for i in range(-5, width * 10 + 5, 10):
            curve(pos=[(i / 10 + 0.5, -0.5), (i / 10 + 0.5, length - 0.5)],
                  color=color.green)
        for i in range(-5, length * 10 + 5, 10):
            curve(pos=[(-0.5, i / 10 + 0.5), (width - 0.5, i / 10 + 0.5)],
                  color=color.green)

    def draw_walls(self, cells):
        for cell in cells:
            if cell.is_wall:
                box(pos=(cell.point.x, cell.point.y, 0.5),
                    width=1, length=1, heigth=1, color=color.blue)

    def draw_path(self, path):
        for cell in path:
            self.draw_cell(cell)
            
    def draw_calculated_cells(self, closed, open):
        for cell in closed:
            self.draw_cell(cell, color.yellow)
        
        for cell in open:
            self.draw_cell(cell, color.cyan)
                    
    def draw_start(self, start):
        self.draw_cell(start, color.white)

    def draw_finish(self, finish):
        self.draw_cell(finish, color.red)
        
    def draw_cell(self, cell, clr):
        self.draw_box(cell, clr)
        
    def draw_box(self, point, clr):
        box(pos=(point.x, point.y, 0.5),
            width=1,
            length=1,
            heigth=1,
            color=clr)
