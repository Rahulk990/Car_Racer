import random as rn
from tkinter import *


class Car:
    def __init__(self, cvs, x, y, color):
        self.body = cvs.create_rectangle(x-10, y-10, x+10, y+10, fill=color)
        self.score = 100

    def alter_score(self, value):
        self.score = self.score + value

    def move(self, top, cvs, x, y):
        pos = cvs.coords(self.body)
        if pos[0] <= 300:
            x = 1
        if pos[1] <= 0:
            T = Text(top, height = 4, width = 50) 
            b2 = Button(top, text = "Exit", command = top.destroy) 
            T.pack()  
            b2.pack() 
            T.insert(END, "You Won!!") 

        if pos[2] >= 500:
            x = -1
        if pos[3] >= 600:
            y = -1

        if(y < 0):
            self.alter_score(10)

        cvs.move(self.body, x, y)


def create_obstacles(cvs):
    obstacles = []
    y_choice = [50 + x*30 for x in range(0, 16)]

    for i in range(8):
        y = rn.choice(y_choice)
        obstacles.append(Car(cvs, 324, y, 'blue'))

    for i in range(8):
        y = rn.choice(y_choice)
        obstacles.append(Car(cvs, 376, y, 'blue'))

    for i in range(8):
        y = rn.choice(y_choice)
        obstacles.append(Car(cvs, 424, y, 'blue'))

    for i in range(8):
        y = rn.choice(y_choice)
        obstacles.append(Car(cvs, 476, y, 'blue'))

    return obstacles
