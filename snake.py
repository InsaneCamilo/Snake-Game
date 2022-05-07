import turtle
import time

posponer = 0.1

#Conf ventana
win = turtle.Screen()
win.title("Play Snake")
win.bgcolor("orange")
win.setup(width = 600, height = 600) 
win.tracer(0)

#SnakeHead
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("purple")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Funciones
def up():
    head.direction = "up"

def down():
    head.direction = "down"

def left():
    head.direction = "left"

def right():
    head.direction = "right"


def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    head.direction="stop"
    


#keyboard
win.listen()
win.onkeypress(up, "Up")
win.onkeypress(down, "Down")
win.onkeypress(left, "Left")
win.onkeypress(right, "Right")

while True:
    win.update()

    print(head.direction)
    mov()
    time.sleep(posponer)


    