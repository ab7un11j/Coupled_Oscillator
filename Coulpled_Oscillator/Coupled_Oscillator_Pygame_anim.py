"""
Created on Sun Oct  1 00:01:39 2023

@author: Ab7un11j

Main file that draws on window 


"""

from Coupled_Oscillator import *
from Mass_Obj import *


pos1 = (400,400)
pos2 = (800,400)

m1 = 10
k1 = 300

#initiating a Coupled Oscillator

mass1 = Mass(pos1, m1, k1)
mass2 =Mass(pos2, m1, k1)
C_occ = Couple_Occ(mass1, mass2, 30)


C_occ.inital_displacement(-60, 0)

C_occ.inial_velocity(0 ,0)




t=0
fps=100# frames per second
delay = 1000//fps
it=1/fps



pg.init()
pg.display.set_caption("Coupled Occilator")
Win =pg.display.set_mode((1200,800))
Win.fill('white')

run = True
while run:
    

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

    
pg.quit()
pg.display.quit()









