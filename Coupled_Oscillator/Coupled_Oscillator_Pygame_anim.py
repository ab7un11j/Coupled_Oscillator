"""
Created on Sun Oct  1 00:01:39 2023

@author: Ab7un11j

Main file that draws on window 


"""
import numpy as np
from PIL import Image
from Coupled_Oscillator import *
from Mass_Obj import *


pos1 = (50,100)
pos2 = (200,100)

m1 = 10
k1 = 2000

#initiating a Coupled Oscillator

mass1 = Mass(pos1, m1, k1)
mass2 =Mass(pos2, m1, k1)
C_occ = Couple_Occ(mass1, mass2, 200)


C_occ.inital_displacement(-40, 0)

C_occ.inial_velocity(0 ,0)

frms = []


t=0
fps=100# frames per second
delay = 1000//fps
it=1/fps



pg.init()
pg.display.set_caption("Coupled Occilator")
Win =pg.display.set_mode((250,200),pg.SRCALPHA)
Win.fill('white')

run = True
while run:
    
    t+=1
    M_pos = pg.mouse.get_pos()
    M_press = pg.mouse.get_pressed()
    
    Win.fill('white')
    pg.time.delay(delay)   
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False

    C_occ.motion(it)
    C_occ.draw_ini_wp(Win) 
    C_occ.draw_Cople_Occ(Win)
    C_occ.Mouse_control(M_pos, M_press[0]) 
    
    pg.display.update()

    
    fdata = pg.surfarray.array3d(Win)
    fimg = Image.fromarray(np.transpose(fdata,(1,0,2)))
    frms.append(fimg)
    
    

    condition1 = -38 > (C_occ.x1)
    condition2 = abs(C_occ.x2) <4
    if condition1 and condition2 and t>400:
        run = False
   
pg.quit()
pg.display.quit()

frms[0].save("Coupled_Oscil1ator2.gif", save_all=True,append_images=frms[1:],duration=delay,loop=2)








