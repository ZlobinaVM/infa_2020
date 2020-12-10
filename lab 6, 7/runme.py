from tkinter import *
from random import randrange as rnd, choice
import time
import math
import array
root = Tk()


c = Canvas(root, width=760, height=760, bg='white')
c.pack()
root.geometry('760x760')


lvl = 0
k = 0


canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)


'''
создание двух фигур
'''


colors = ['red','orange','yellow','green','blue']
def new_ball():
    global x, y, r, dx, dy, ball, n, x1, y1, r1, dx1, dy1, shape, n1
    c.delete(ALL)
    n = rnd(1,10)    #шарики от 1 до 10
    x = [0]*n
    y = [0]*n
    dx = [0]*n
    dy = [0]*n
    r = [0]*n
    for i in range (n):
        x[i] = rnd(60,700)
        y[i] = rnd(60,700)
        dx[i] = rnd(-1,1)
        dy[i] = rnd(-1,1)
        r[i] = rnd(30,50)
    
    ball = [0]*n
    for i in range(n):
        ball[i] = c.create_oval(x[i]-r[i],y[i]-r[i],x[i]+r[i],y[i]+r[i],fill = choice(colors), width=0)

    n1 = rnd(1,3)      #прямоугольники от 1 до 3
    x1 = [0]*n1
    y1 = [0]*n1
    dx1 = [0]*n1
    dy1 = [0]*n1
    r1 = [0]*n1
    for i in range (n1):
        x1[i] = rnd(60,700)
        y1[i] = rnd(120,640)
        dx1[i] = rnd(-3,3)
        dy1[i] = rnd(-3,3)
        r1[i] = rnd(30,70)
    
    shape = [0]*n1
    for i in range(n1):
        m = choice(colors)
        shape[i] = c.create_rectangle(x1[i],y1[i], x1[i]+r1[i], y1[i]+2*r1[i],fill = m, outline = m, width=3 )
    root.after(500000,new_ball)


'''
движение шара
'''


def move_ball():
    global x,y,dx,dy,ball,n
    for i in range(n):
        c.move(ball[i],dx[i],dy[i])
        y[i] += dy[i]
        x[i] += dx[i]
    root.after(10, move_ball)
    rebound_ball()


'''
отскок шара
'''


def rebound_ball():
    global x,y,dx,dy,ball,n
    for i in range(n):
        if y[i] <= r[i] or y[i] >= 760-r[i]:
            dy[i] = -dy[i]
        if x[i] <= r[i] or x[i] >= 760-r[i]:
            dx[i] = -dx[i]


'''
движение прямоугольника
'''


def move_shape():
    global x1,y1,dx1,dy1,shape,n1
    for i in range(n1):
        c.move(shape[i],dx1[i],dy1[i])
        y1[i] += dy1[i]
        x1[i] += dx1[i]
    root.after(10, move_shape)
    rebound_shape()


'''
отражение прямоугольника
'''


def rebound_shape():
    global x1,y1,dx1,dy1,shape,n1
    for i in range(n1):
        if y1[i] <= 0 or y1[i] >= 760-2*r1[i]:
            dy1[i] = -dy1[i]
   
        if x1[i] <= 0 or x1[i] >= 760-r1[i]:
           dx1[i] = -dx1[i]


'''
прокликивания
'''


def click(event):
    global x,y,r,n,xe,ye, a, k, x1,y1,r1,n1, lvl
    xe = event.x
    ye = event.y
    
    for i in range(n):
        a = ((xe-x[i])**2 + (ye-y[i])**2)**0.5
        if a < r[i]:
            k += 1
            lvl += 1
            #print (k)
            new_ball()
            move_ball()
            move_shape()
    for i in range (n1):
        if (xe>=x1[i])*(xe<=x1[i]+r1[i])*(ye>=y1[i])*(ye<=y1[i]+2*r1[i])==1:
            k += 5
            lvl += 1
            #print (k)
            new_ball()
            move_ball()
            move_shape()


'''
функции: *вызываються*
'''


c.bind('<Button-1>', click)
new_ball()
move_ball()
move_shape()


'''
представьтесь
'''


print('представьтесь, когда закончите')
name = input()


'''
работа с файлом
'''


s = 0

f = open('text.txt', 'a')
f.write("\n")
f.write(name)
f.write(' ')
f.write(str(k))
f.write(' ')
f.write(str(lvl))

f = open('text.txt', 'r')
for line in f:
    s += 1
    
f = open('text.txt', 'r')
Name = [0]*s
BRS = [0]*s
LVL = [0]*s
for i in range (s):
    se = f.readline().split()
    Name[i] = se[0]
    BRS[i] = se[1]
    LVL[i] = se[2]

for i in range (s):
    BRS[i] = int(BRS[i])

for j in range (s-1):
    for i in range (s-j-1 ):
        if (BRS[i+1] > BRS [i]):
            BRS[i], BRS[1+i] = BRS[1+i], BRS[i]
            Name[i], Name[1+i] = Name[1+i], Name[i]
            LVL[i], LVL[1+i] = LVL[1+i], LVL[i]

for i in range(s):
    BRS[i] = str(BRS[i])

f = open('text.txt', 'w')
for i in range (s-1):
    f.write(Name[i])
    f.write(' ')
    f.write(BRS[i])
    f.write(' ')
    f.write(LVL[i])
    f.write("\n")
f.write(Name[s])
f.write(' ')
f.write(BRS[s])
f.write(' ')
f.write(LVL[s])

#f = open('text.txt', 'r')
#for line in f:
    #print(line)

f.close()


mainloop()
