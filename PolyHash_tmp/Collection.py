'''
Created on 27 oct. 2016

@authors: Mathieu Soyer, Nicolas Ehresmann
'''

from Satellite import Satellite

class Collection:

    def __init__(self,valeurPoints,listeCoordonnees,tempsRequis):
	self.valeurPoints=valeurPoints
	self.listeCoordonnees=listeCoordonnees
	self.listeCoordoneesReussies=[]
	self.tempsRequis=tempsRequis
    @classmethod
    def valeurs(cls,valeurs):                                  //2eme constructeur
	return cls(valeurs,listeCoordonnees=[],tempsRequis=[])	
    

    def getvaleur():
	return self.valeurPoints
	
    def getCoordonnees():
	return self.listeCoordonnees
    def getCoordonneesReussies():
	return self.getCoordonneesReussies
			
    def suppresionElement(liste):
	if estVide():
		return False
	else:
		self.listeCoordonnees.remove(liste)
		return True

    def estVide():
	if not self.listeCoordonnees:
		return True
	else:
		return False
   
