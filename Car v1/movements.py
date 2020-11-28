from tkinter import *


def car_movement(top, cvs, car, speed, keycode):
    if keycode == 37 or keycode == 100:
        car.move(top, cvs, -speed, 0)
    if keycode == 38 or keycode == 104:
        car.move(top, cvs, 0, -speed)
    if keycode == 39 or keycode == 102:
        car.move(top, cvs, speed, 0)
    if keycode == 40 or keycode == 98:
        car.move(top, cvs, 0, speed)
    if keycode == 97:
        car.move(top, cvs, -speed, speed)
    if keycode == 99:
        car.move(top, cvs, speed, speed)
    if keycode == 103:
        car.move(top, cvs, -speed, -speed)
    if keycode == 105:
        car.move(top, cvs, speed, -speed)


def check_intersection(A, B):
    if (A[0] > B[2] or B[0] > A[2]) or (A[1] > B[3] or B[1] > A[3]):
        return False
    return True


def check_collision(top, cvs, player, obstacles):
    player_pos = cvs.coords(player.body)
    for obstacle in obstacles:
        obstacle_pos = cvs.coords(obstacle.body)

        if check_intersection(player_pos, obstacle_pos):
            T = Text(top, height=4, width=50)
            b2 = Button(top, text="Exit", command=top.destroy)
            T.pack()
            b2.pack()
            T.insert(END, "Game Over")


def Key(event, top, cvs, car, obstacles):
    car_movement(top, cvs, car, 3, event.keycode)
    # for obstacle in obstacles:
    #     car_movement(cvs, obstacle, 1, 38)
    check_collision(top, cvs, car, obstacles)
