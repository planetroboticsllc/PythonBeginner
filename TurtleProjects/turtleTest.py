from turtle import *

def polygon(sides = 3, length = 100):
    counter = 0
    while(counter < sides):
        forward(length)
        left(360/sides)
        counter += 1


def multigon(sides = 4, length=50):
    color('red', 'yellow')
    n = 0
    while(n < sides):
        polygon(sides=sides, length=length)
        n += 1
        left(360/sides)
        penup()
        forward(50)
        pendown()


def flower(angle = 135):
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(angle)
        if abs(pos()) < 1:
            break
    end_fill()




flower(150)

penup()
home()
goto(-100,0)
pendown()

multigon(sides=20, length=25)

done()

