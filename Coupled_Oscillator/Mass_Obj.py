"""
Created on Sun Oct  8 16:13:57 2023

@author: Ab7un11j

Module that creates Mass objwith properties: 
    Mass , Spring constant of an invisible sprinfg connected to itinitial velocity an Initial Distance.
   
"""
class Mass:
    def __init__(self,pos, mass,k):
        if isinstance(pos, tuple) and ( isinstance(mass, float) or isinstance(mass, int)):
            self.mass = mass
            self.pos=pos #initial position
            self.k =k #spring constant

            self.y = pos[1]            
            # Standerd Initial condition That will be updated using Methods below
            self.x = pos[0] +100 #X position
            self.ix = 0 #Velocity
            self.iix= 0#Accelaretion
            
            
        else :
            raise TypeError('Position 1 not a tuple of position 2 not a float or int ')
            
   #intial distanse defibning function            
    def ini_dis(self,initialdistance):       
        self.x = self.pos[0]+ initialdistance
        
    #intial vel defibning function       
    def ini_vel(self,velocity):
        self.ix =velocity