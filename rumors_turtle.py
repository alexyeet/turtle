import random
import math
from random import randint
from turtle import *

texto = Turtle()
colorboy = Turtle()

texto.shape("turtle")
colorboy.shape("turtle")

texto.color("dark blue")
colorboy.color("chartreuse")

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
        

#run
    
#write_rumors("blue")

while True:
    draw_star(100)
    colorboy.right(randint(1, 360))
    colorboy.fd(150)
    

    


    
    


    


