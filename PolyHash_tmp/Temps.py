'''
Created on 23 oct. 2016

@author: Nicolas
'''

class Temps:
    
    def __init__(self, tempsTotal):
        self.temps = 0
        self.tempsTotal = tempsTotal
        
    def incrementer(self):
        self.temps += 1
        
    def tempsEcoule(self):
        ret = False
        if (self.temps >= self.tempsTotal):
            ret = True
        return ret