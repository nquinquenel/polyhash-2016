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
            self.listeCoordonnes = []
            self.tempsRequis = []

    def getvaleur():
        return self.valeurPoints
	
    def getCoordonnees():
        return self.listeCoordonnees

    def getTemps():
        return self.tempsRequis
    
    def getCoordonneesReussies():
        return self.getCoordonneesReussies
			
    def suppressionElement(liste):
            self.listeCoordonnees.remove(liste)
            return estVide()

    def estVide():
        if not self.listeCoordonnees:
            return True
        else:
            return False
   
