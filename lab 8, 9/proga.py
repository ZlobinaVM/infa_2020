from random import randrange as rnd, choice
import tkinter as tk
import math
import time
import os

print(os.path.abspath('/Users/verazlobina/Desktop/module.py'))

import \\Users\\verazlobina\\Desktop\\module.py

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
module.canv = canv

screen1 = canv.create_text(400, 300, text='', font='28')
global ab
def a():
    ab -= 1

g1=module.gun()

def new_game():
    global gun, screen1, balls, bullet
    canv.itemconfig(screen1, text='')
    module.bullet = 0
    module.balls = []
    targets = []
    tlive = 0
    for i in range(2):
        new_target = module.target()
        targets.append(new_target)
        tlive += targets[i].live
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
 
    while tlive or module.balls:

        for j in range(2):
            targets[j].move()
        for i, b in enumerate(module.balls):
            b.move()
            for j in range(2):
                if b.hittest(targets[j]) and targets[j].live:
                    tlive -= targets[j].live
                    targets[j].live = 0
                    targets[j].hit()
        
            
        canv.update()
        time.sleep(0.02)
        g1.targetting()
        g1.power_up()
        if tlive==0:

            canv.update()
                
            for b in module.balls:
            
                b.die()
            
                canv.delete(b.id)
            break
            
        #time.sleep(2)
    module.balls = []
    canv.itemconfig(screen1, text='')
    canv.update()
    balls = []

    
    canv.bind('<Button-1>', '')
    canv.bind('<ButtonRelease-1>', '')
    canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(module.bullet) + ' выстрелов')
    canv.delete(g1)
    root.after(1500, new_game)


new_game()

root.mainloop()
