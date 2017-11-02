import random
import math
from random import randint
from turtle import *

colormode(255)

texto = Turtle()
colorboy = Turtle()

texto.shape("turtle")
colorboy.shape("turtle")

texto.color(45, 88, 158)
colorboy.color(randint(0, 255), randint(0, 255), randint(0, 255))

texto.pensize(10)


#letter functions
               

def write_R():
    texto.pendown()
    texto.forward(100)
    texto.back(100)
    texto.left(90)
    texto.fd(50)
    texto.right(90)
    texto.fd(40)
    texto.right(90)
    texto.fd(50)
    texto.left(135)
    texto.fd(78)
    texto.penup()

def write_U():
    texto.pendown()
    texto.right(180)
    texto.fd(100)
    texto.left(90)
    texto.fd(40)
    texto.left(90)
    texto.fd(100)
    texto.penup()
    
def write_M():
    texto.pendown()
    texto.left(90)
    texto.back(100)
    texto.fd(100)
    texto.right(120)
    texto.fd(30)
    texto.left(60)
    texto.fd(30)
    texto.right(120)
    texto.fd(100)
    texto.penup()

def write_O():
    texto.pendown()
    texto.left(90)
    texto.fd(100)
    texto.right(90)
    texto.fd(60)
    texto.right(90)
    texto.fd(100)
    texto.left(90)
    texto.back(60)
    texto.fd(60)
    texto.penup()

def write_S():
    texto.pendown()
    texto.fd(60)
    texto.left(90)
    texto.fd(50)
    texto.left(90)
    texto.fd(60)
    texto.right(90)
    texto.fd(50)
    texto.right(90)
    texto.fd(50)
    texto.penup()

def write_rumors(color):
    texto.right(180)
    texto.penup()
    texto.fd(200)
    texto.left(90)
    texto.back(100)

    write_R()

    texto.left(45)
    texto.fd(20)
    texto.left(90)
    texto.fd(100)

    write_U()

    texto.right(90)
    texto.fd(20)

    write_M()

    texto.left(90)
    texto.fd(20)

    write_O()

    texto.fd(20)
    texto.left(90)
    texto.fd(100)
    texto.left(180)

    write_R()

    texto.left(45)
    texto.fd(20)

    write_S()

def draw_star(size):
    colorboy.pendown()
    for i in range (5):
        colorboy.fd(size)
        colorboy.left(144)
    colorboy.penup()

#arrow keys

def right_arrow():
    colorboy.right(randint(10, 90))

def left_arrow():
    colorboy.left(randint(10, 90))

#run

for i in range (1):  
    write_rumors("blue")

while True:
    draw_star(100)
    colorboy.right(randint(1, 360))
    colorboy.fd(150)
    colorboy.color(randint(0, 255), randint(0, 255), randint(0, 255))
    onkeypress(left_arrow)
    onkeypress(right_arrow)
    listen()

    


    
    


    


