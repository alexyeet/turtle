from turtle import *

import random
import math
from random import randint

colormode(255)

jaden = Turtle()
alex = Turtle()
chase = Turtle()

jaden.shape("turtle")
alex.shape("turtle")
chase.shape("turtle")

jaden.color("firebrick1")
alex.color("dodgerblue2")
chase.color("orchid4")

jaden.left(90)
alex.left(90)
chase.left(90)


while True:
    #color((randint(0,255)),(randint(0,255)),(randint(0,255)))

    jaden.penup()
    jaden.forward(randint(1, 10))
    jaden.right(randint(-20, 20))
    jaden.pendown()
        
    alex.penup()
    alex.forward(randint(1, 10))
    alex.right(randint(-20, 20))
    alex.pendown()

    chase.penup()
    chase.fd(randint(1, 10))
    chase.right(randint(-20, 20))
    chase.pendown()
        
