import turtle
from turtle import *
from time import sleep

color('blue', 'green')

name = "junk"
specialDate = "junk"
name = input("What is your name (write Coachy Roachy)")
specialDate = input("Is it your birthday? (write yes)")

if specialDate.lower() == "yes" and name.lower() == "coachy roachy":

    print("Happy Birthday Coachy Roachy")
    print("Thank you for helping our team succeed and achieve our goals! ")
    print("Don't close the shell yet! There's more!!!!")

    t = turtle

    counter = 1
    begin_fill()
    fillcolor('blue')
    t.pencolor('blue')
    t.left(45)
    t.forward(60)
    while counter < 280:
        t.forward(1)
        t.left(1)
        counter += 1
    t.right(15)
    t.forward(50.5)
    end_fill()
    t.pensize(3.52)
    t.pencolor('green')
    t.right(45)
    t.forward(100)

    print("Btw, that was a balloon if u didn't get it :|")
    print("Well, that's about it. One final thing:")
    print("We used google for learning all turtle commands.")
    print("As you say, Google is our FRIEND. :)")

sleep(10)

 
