'''
Created on 23 oct. 2016

@author: Nicolas
'''

from Temps import Temps
from Satellite import Satellite

class Lanceur:
    
    def __init__(self):
        self.listeSatellite = []
        self.listeSatellite.append(Satellite(176400, 7200, 120, 200, 10000))
        self.listeCollection = []
        self.score = 0
        self.temps = Temps(3600)
        self.lancerSimulation()
        
    def lectureFichier(self):
        return True
    
    def fichierSortie(self):
        return 0
    
    def validationCollection(self):
        return -1
    
    def lancerSimulation(self) :
        #Tant que le temps de la simulation n'est pas ecoule
        while not self.temps.tempsEcoule():
            for sat in self.listeSatellite:
                sat.calculePosition()
            self.temps.incrementer()
    
l1 = Lanceur()