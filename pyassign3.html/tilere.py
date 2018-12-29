import turtle


def check(i, j, x, y):
    if i + x > m or j + y > n:
        return False
    for i1 in range(i, i + x):
        for j1 in range(j, j + y):
            index = i1 * n + j1
            if wall[index] != 0:
                return False
    return True


def fill(nowans, i, j, x, y, val):
    tmp = []
    for i1 in range(i, i + x):
        for j1 in range(j, j + y):
            index = i1 * n + j1
            wall[index] = val
            tmp.append(index)
    if val == 1:
        nowans.append(tmp)
    if val == 0:
        nowans.remove(tmp)
    return


def put(nowans, i, j):
    if i == m - 1 and j == n:
        ans.append(nowans.copy())
        return
    elif j == n:
        put(nowans, i + 1, 0)
        return
    if wall[i * n + j] == 1:
        put(nowans, i, j + 1)
        return
    if check(i, j, a, b):
        fill(nowans, i, j, a, b, 1)
        put(nowans, i, j + b)
        fill(nowans, i, j, a, b, 0)
    if a != b and check(i, j, b, a):
        fill(nowans, i, j, b, a, 1)
        put(nowans, i, j + a)
        fill(nowans, i, j, b, a, 0)
        return


def bobgo(x, y):
    bob.down()
    bob.fd(x * 50)
    bob.left(90)
    bob.fd(y * 50)
    bob.left(90)
    bob.fd(x * 50)
    bob.left(90)
    bob.fd(y * 50)
    bob.left(90)
    bob.up()
    return


def draw1(lst):
    for ele in lst:
        bob.goto(ele[0] % n * 50, ele[0] // n * 50)
        if ele[a - 1] - ele[0] + 1 == max(a, b):
            bobgo(a, b)
        else:
            bobgo(b, a)
    return


m = int(input('输入墙高'))
n = int(input('输入墙长'))
a = int(input('输入砖高'))
b = int(input('输入砖长'))
wall = [0] * (m * n)
ans = []
put([], 0, 0)
print(ans)
choice = eval(input('输入你想画出的结果'))
bg = turtle.Screen()
bob = turtle.Turtle()
turtle.setworldcoordinates(0, 1000, 1000, 0)
draw1(choice)
