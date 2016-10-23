'''
Created on 23 oct. 2016

@author: Nicolas
'''

from Temps import Temps
from Satellite import Satellite

class Lanceur:
    
    def __init__(self):
        self.listeSatellite = []
        self.listeSatellite.append(Satellite(176400, 7200, 120, 100, 1))
        self.listeCollection = []
        self.score = 0
        self.temps = Temps(3600)
        self.lancerSimulation()
    
    def lancerSimulation(self) :
        while not self.temps.tempsEcoule():
            self.listeSatellite[0].calculePosition()
            self.temps.incrementer()
        return 0
    
l1 = Lanceur()