"""Planet.py:
To draw a picture to imitate how planets
run around the sun using turtle.

__author__="Liyuhao"
__pkuid__="1800011761"
__email__="1800011761@pku.edu.cn"
"""

import turtle
import math
m = turtle.Screen()
sun = turtle.Turtle()
sun.hideturtle()
sun.up()
sun.goto(100, 0)
sun.dot(50, "red")
alexa = turtle.Turtle()
alexa.color("red")
alexa.shape("circle")
alexb = turtle.Turtle()
alexb.color("green")
alexb.shape("circle")
alexc = turtle.Turtle()
alexc.color("blue")
alexc.shape("circle")
alexd = turtle.Turtle()
alexd.color("yellow")
alexd.shape("circle")
alexe = turtle.Turtle()
alexe.color("orange")
alexe.shape("circle")
alexf = turtle.Turtle()
alexf.color("purple")
alexf.shape("circle")
alexg = turtle.Turtle()
alexg.color("gray")
alexg.shape("circle")
alexh = turtle.Turtle()
alexh.color("brown")
alexh.shape("circle")
alexa.up()
alexa.goto(20000 ** 0.5, 0)
alexa.down()
alexb.up()
alexb.goto(30000 ** 0.5, 0)
alexb.down()
alexc.up()
alexc.goto(40000 ** 0.5, 0)
alexc.down()
alexd.up()
alexd.goto(50000 ** 0.5, 0)
alexd.down()
alexe.up()
alexe.goto(60000 ** 0.5, 0)
alexe.down()
alexf.up()
alexf.goto(70000 ** 0.5, 0)
alexf.down()
alexg.up()
alexg.goto(80000 ** 0.5, 0)
alexg.down()
alexh.up()
alexh.goto(90000 ** 0.5, 0)
alexh.down()
for i in range(1000000):
    alexa.speed(0)
    alexa.goto(20000 ** 0.5 * math.cos(math.pi/90 * i),
               10000 ** 0.5 * math.sin(math.pi/90 * i))
    alexb.speed(0)
    alexb.goto(30000 ** 0.5 * math.cos(math.pi/110 * i),
               20000 ** 0.5 * math.sin(math.pi/110 * i))
    alexc.speed(0)
    alexc.goto(40000 ** 0.5 * math.cos(math.pi/130 * i),
               30000 ** 0.5 * math.sin(math.pi/130 * i))
    alexd.speed(0)
    alexd.goto(50000 ** 0.5 * math.cos(math.pi/150 * i),
               40000 ** 0.5 * math.sin(math.pi/150 * i))
    alexe.speed(0)
    alexe.goto(60000 ** 0.5 * math.cos(math.pi/170*i),
               50000 ** 0.5*math.sin(math.pi/170 * i))
    alexf.speed(0)
    alexf.goto(70000**0.5*math.cos(math.pi/190*i),
               60000**0.5*math.sin(math.pi/190*i))
    alexg.speed(0)
    alexg.goto(80000**0.5*math.cos(math.pi/210*i),
               70000**0.5*math.sin(math.pi/210*i))
    alexh.speed(0)
    alexh.goto(90000**0.5*math.cos(math.pi/230*i),
               80000**0.5*math.sin(math.pi/230*i))
