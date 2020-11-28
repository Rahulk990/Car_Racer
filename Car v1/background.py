import random as rn
from tkinter import *


class Road_Marking:
    def __init__(self, cvs, x, y):
        self.base = cvs.create_rectangle(
            x-3, y, x+3, y+30, fill='White', outline='')


class Tree:
    def __init__(self, cvs, x, y):
        self.base = cvs.create_rectangle(
            x+2, y, x+18, y+30, fill='Saddle Brown', outline='')
        self.cir1 = cvs.create_oval(
            x-15, y-15, x+15, y+15, fill='Spring Green4', outline='')
        self.cir4 = cvs.create_oval(
            x+3, y-30, x+33, y, fill='Spring Green3', outline='')
        self.cir2 = cvs.create_oval(
            x+2, y-15, x+32, y+15, fill='Spring Green4', outline='')
        self.cir3 = cvs.create_oval(
            x-12, y-30, x+18, y, fill='Spring Green3', outline='')


def draw_road(cvs, height):
    cvs.create_rectangle(300, -1, 500, height+5, fill='gray', outline='')

    markings = []
    for i in range(12):
        markings.append(Road_Marking(cvs, 400, 50*i + 10))
    for i in range(12):
        markings.append(Road_Marking(cvs, 450, 50*i + 10))
    for i in range(12):
        markings.append(Road_Marking(cvs, 350, 50*i + 10))


def left_terrain(cvs, height):
    cvs.create_rectangle(295, -1, 300, height+5,
                         fill='Black', outline='')
    cvs.create_rectangle(-1, -1, 295, height+5,
                         fill='SpringGreen2', outline='')
    trees = []

    x_choice = [20, 80, 140, 200, 260]
    y_choice = [40, 115, 190, 265, 340, 415, 490, 565]
    for i in range(20):
        trees.append(Tree(cvs, rn.choice(x_choice), rn.choice(y_choice)))


def right_terrain(cvs, height):
    cvs.create_rectangle(500, -1, 505, height+5,
                         fill='Black', outline='')
    cvs.create_rectangle(505, -1, 805, height+5,
                         fill='SpringGreen2', outline='')
    trees = []

    x_choice = [520, 580, 640, 700, 760]
    y_choice = [40, 115, 190, 265, 340, 415, 490, 565]
    for i in range(20):
        trees.append(Tree(cvs, rn.choice(x_choice), rn.choice(y_choice)))