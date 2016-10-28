'''
Created on 27 oct. 2016

@authors: Mathieu Soyer, Nicolas Ehresmann
'''

class Collection:

    def __init__(self,valeurPoints,listeCoordonnees=None,tempsRequis=None):
        self.listeCoordoneesReussies= []
        self.valeurPoints = valeurPoints
        if(tempsRequis != None or listeCoordonnees != None):
            self.listeCoordonnees = listeCoordonnees
            self.tempsRequis = tempsRequis
        else:
            self.listeCoordonnees = []
            self.tempsRequis = []

    def getvaleur(self):
        return self.valeurPoints
	
    def getCoordonnees(self):
        return self.listeCoordonnees

    def getTemps(self):
        return self.tempsRequis
    
    def getCoordonneesReussies(self):
        return self.getCoordonneesReussies
			
    def suppressionElement(self,liste):
            self.listeCoordonnees.remove(liste)
            return estVide()

    def estVide(self):
        if not self.listeCoordonnees:
            return True
        else:
            return False
   
