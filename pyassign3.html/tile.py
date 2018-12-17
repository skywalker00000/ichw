"""tile.py
To find all methods to fill a wall
with bricks given,
and draw a picture of one possible answer
using turtle.

__author__="Liyuhao"
__pkuid__="1800011761"
__email__="1800011761@pku.edu.cn"
"""


import turtle


def draw(lst):
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == 1:   # 判断砖的有无和横竖
                bobgo(b, a, j, i)
                clear(i, j, b, a)
            elif lst[i][j] == 2:
                bobgo(a, b, j, i)
                clear(i, j, a, b)
            elif lst[i][j] == 0:
                continue


def clear(i, j, x, y):   # 清除掉已描出轮廓的砖
    for i1 in range(y):
        for j1 in range(x):
            lst[i + i1][j + j1] = 0


def bobgo(x, y, j, i):
    bob.up()
    bob.goto(j * 50, i * 50)
    bob.down()
    bob.fd(x * 50)
    bob.left(90)
    bob.fd(y * 50)
    bob.left(90)
    bob.fd(x * 50)
    bob.left(90)
    bob.fd(y * 50)
    bob.left(90)


def can(i, j, x, y, num):
    if i + x > m or j + y > n:
        return False
    for i1 in range(x):
        for j1 in range(y):
            if wall[i + i1][j + j1] != 0:
                return False
    for i1 in range(x):
        for j1 in range(y):
            wall[i + i1][j + j1] = num
    return True


def put():
    for i in range(m):
        for j in range(n):
            if wall[i][j] == 0:   # 未铺砖
                if can(i, j, a, b, 1):   # 1表示砖横放
                    put()
                    for i1 in range(a):
                        for j1 in range(b):
                            wall[i + i1][j + j1] = 0   # 清除已放置的砖
                if can(i, j, b, a, 2):   # 2表示砖竖放
                    put()
                    for i1 in range(b):
                        for j1 in range(a):
                            wall[i + i1][j + j1] = 0
                return
    print(wall)
    return


m = int(input('输入墙高'))
n = int(input('输入墙长'))
a = int(input('输入砖高'))
b = int(input('输入砖长'))
wall = [[0 for i in range(n)] for j in range(m)]   # 建立一堵空的墙
put()
bg = turtle.Screen()
bob = turtle.Turtle()
turtle.setworldcoordinates(0, 1000, 1000, 0)
lst = eval(input('输入你想画出的结果'))
draw(lst)
