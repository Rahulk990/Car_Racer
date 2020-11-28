import car as cr
from tkinter import *
import movements as mv
import background as bg

WIDTH = 800
HEIGHT = 600

if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root, width=WIDTH, height=HEIGHT)
    root.title('The Car Racer')
    canvas.pack()

    # Rendering Background
    bg.draw_road(canvas, HEIGHT)
    bg.left_terrain(canvas, HEIGHT)
    bg.right_terrain(canvas, HEIGHT)

    # Rendering Cars
    player = cr.Car(canvas, 475, 550, 'red')
    obstacles = cr.create_obstacles(canvas)

    root.bind('<Escape>', lambda event: root.destroy())
    root.bind('<Key>', lambda event: mv.Key(
        event, root, canvas, player, obstacles))

    canvas.mainloop()
