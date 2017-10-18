from turtle import *

texto = Turtle()


#positioning start

texto.left(150)
texto.penup()
texto.forward(100)
texto.left(120)

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

def write_U():
    texto.pendown()
    texto.right(180)
    texto.fd(100)
    texto.left(90)
    texto.fd(40)
    texto.right(90)
    texto.fd(100)
    
write_R()


