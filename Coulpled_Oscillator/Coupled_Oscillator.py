"""
Created on Thu Sep 28 21:37:58 2023

@author: Ab7Un11j

/Module that Creates a coupled Oscillator obj that have 2 obj- mass obj and 1 property spring constant k.
/Calculates and defines drawing functions of two mass obj.


"""
import pygame as pg


class Couple_Occ:
    
    
    def __init__(self, mass1 , mass2, k2):
        #mass1 and mass2 are mass obj
        
        self.m1 = mass1
        self.m2 = mass2
        self.k2 = k2
        self.m1.ini_dis(50)
        self.m2.ini_dis(0)
        self.m1.ini_vel(0)
        self.m2.ini_vel(0)
        self.Rng = [10,15]
        
    def inital_displacement(self,dis1, dis2):
        self.m1.ini_dis(dis1)
        self.m2.ini_dis(dis2)
        
    def inial_velocity(self,vel1,vel2):
        self.m1.ini_vel(vel1)
        self.m2.ini_vel(vel2)
        
    
    def motion(self,it):
        self.x1 = self.m1.x - self.m1.pos[0]
        self.x2 = self.m2.x - self.m2.pos[0]
        
        # Differential Equation ============================
        
        #Note:  'iix' is accilaration, 'ix' is velocity, 'x' is displacement; 'it' is differential time element. 
        
        self.m1.iix = -(self.m1.k/self.m1.mass)*(self.x1)+(self.k2/self.m1.mass)*(self.x2 - self.x1)
        self.m1.ix+= it*self.m1.iix
        self.m1.x+= it*self.m1.ix
        
        self.m2.iix = -(self.m2.k/self.m2.mass)*(self.x2)+(self.k2/self.m2.mass)*(self.x1 - self.x2)
        self.m2.ix+= it*self.m2.iix
        self.m2.x+= it*self.m2.ix
        
        
        
        #++++++++++++++++++++++++++++++++++++
        
        self.movpos1 = (self.m1.x,self.m1.y)
        self.movpos2 = (self.m2.x,self.m2.y)
    
    def Mouse_control(self, M_pos,M_press):
        
        
        if M_press:
            condition11 = abs(M_pos[0]-self.movpos1[0]) < self.Rng[0]
            condition12 = abs(M_pos[1]-self.movpos1[1]) < self.Rng[1]
            condition21 = abs(M_pos[0]-self.movpos2[0]) < self.Rng[0]
            condition22 = abs(M_pos[1]-self.movpos2[1]) < self.Rng[1]
            
            if condition11 and condition12:
                self.m1.x = M_pos[0]
                self.m1.ix = 0
                self.Rng = (100,175)
                
                
                
            elif condition21 and condition22:
                self.m2.x = M_pos[0]
                self.m2.ix = 0
                self.Rng = (100,105)
            else:
                pass
        else:
            self.Rng = (10,15)
    def draw_Cople_Occ(self,win):
        
        pg.draw.line(win,(60,180,160),self.movpos1,self.movpos2, 7)
        
        pg.draw.circle(win, (0,0,0),self.movpos1,12)
        pg.draw.circle(win, (0,0,0),self.movpos2,12)
        
    
            
        
    def draw_ini_wp(self,win):
        
        d = 150
        C1 = 'black'
        
        #drawing point where horizontal Springs are connected
        pg.draw.circle(win,C1,(self.m1.pos[0],self.m1.pos[1]+d),6)
        pg.draw.circle(win,C1,(self.m2.pos[0],self.m2.pos[1]+d),6)
        pg.draw.circle(win,C1,(self.m1.pos[0],self.m1.pos[1]-d),6)
        pg.draw.circle(win,C1,(self.m2.pos[0],self.m2.pos[1]-d),6)
        
        #drawing Hoizontal spring
        pg.draw.line(win,'red',(self.m1.pos[0],self.m1.pos[1]+d), self.movpos1,5)
        pg.draw.line(win,'red',(self.m2.pos[0],self.m2.pos[1]+d), self.movpos2,5)
        pg.draw.line(win,'red',(self.m1.pos[0],self.m1.pos[1]-d), self.movpos1,5)
        pg.draw.line(win,'red',(self.m2.pos[0],self.m2.pos[1]-d), self.movpos2,5)
        