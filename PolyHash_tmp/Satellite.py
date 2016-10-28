'''
Created on 23 oct. 2016

@author: Nicolas
'''

class Satellite:
    
    def __init__(self, latitude, longitude, vitesse, changementOrientationMax, orientationMax, numero):
        self.latitude = latitude
        self.longitude = longitude
        self.vitesse = vitesse
        self.changementOrientationMax = changementOrientationMax
        self.orientationMax = orientationMax
        self.deltaLatitude = 0
        self.deltaLongitude = 0
        self.pointageLatitude = self.latitude + self.deltaLatitude
        self.pointageLongitude = self.longitude + self.deltaLongitude
        self.pointageLongitude = 0
        self.delaiPhoto = 1
        self.numero = numero
        
    def changerOrientationLatitude(self, valeur):
        if valeur > self.changementOrientationMax or valeur < -self.changementOrientationMax:
            raise ValueError("Changement trop important")
        elif (self.deltaLatitude + valeur) < -self.orientationMax or (self.deltaLatitude + valeur) > self.orientationMax:
            raise ValueError("Hors des limites de l'orientation maximum")
        else:
            self.deltaLatitude += valeur  
              
    def changerOrientationLongitude(self, valeur):
        if valeur > self.changementOrientationMax or valeur < -self.changementOrientationMax:
            raise ValueError("Changement trop important")
        elif (self.deltaLongitude + valeur) < -self.orientationMax or (self.deltaLongitude + valeur) > self.orientationMax:
            raise ValueError("Hors des limites de l'orientation maximum")
        else:
            self.deltaLongitude += valeur  
    
    def calculePosition(self):
        #Si latitude + vitesse se trouve entre -90° et 90°
        if self.latitude <= 324000 and self.latitude >= -324000:
            self.latitude = self.latitude + self.vitesse
            self.longitude = self.longitude - 15
        #Si latitude + vitesse se trouve superieur à 90° (il vient de depasser le Pole Nord)
        elif self.latitude > 324000:
            self.latitude = (324000*2) - (self.latitude + self.vitesse)
            self.longitude = -(324000*2) + (self.longitude - 15)
            self.vitesse = -self.vitesse
        #Si latitude + vitesse se trouve infenieur à 90° (il vient de depasser le Pole Sud)
        else:
            self.latitude = -(324000*2) - (self.latitude + self.vitesse)
            self.longitude = -(324000*2) + (self.longitude - 15)
            self.vitesse = -self.vitesse
        #Si longitude depasse -648000" alors longitude repasse à 647999"
        if self.longitude < -648000:
            self.longitude = 648000 - (-self.longitude - 648000)
        print("Latitude : " , self.latitude , "; Longitude : " , self.longitude , "; Vitesse : " , self.vitesse)
    
    def getOrientationSatellite(self):
        return self.deltaLatitude, self.deltaLongitude
    
    def getPosition(self):
        return self.latitude, self.longitude
    
    def calculPointageCamera(self):
        self.pointageLatitude = self.latitude + self.deltaLatitude
        self.pointageLongitude = self.longitude + self.deltaLongitude
    
    def prendrePhoto(self, tour):
        ret = [4]
        ret[0] = self.latitude + self.deltaLatitude
        ret[1] = self.longitude + self.deltaLongitude
        ret[2] = self.numero
        ret[3] = tour
        return ret
    
    def nombrePhotoPossible(liste):
	   return 0

    def getPointageCamera():
	   return self.pointageLatitude, self.pointageLongitude
