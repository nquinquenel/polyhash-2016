'''
Created on 23 oct. 2016

@author: Nicolas
'''

from Camera import Camera

class Satellite:
    
    def __init__(self, latitude, longitude, vitesse):
        self.latitude = latitude
        self.longitude = longitude
        self.vitesse = vitesse
        self.deltaLatitude = 0
        self.deltaLongitude = 0
        self.delaiPhoto = 1
        self.changementOrientationMax = 200
        self.orientationMax = 10000
        self.camera = Camera(self.latitude + self.deltaLatitude, self.deltaLongitude + self.deltaLongitude)
        
    def changerOrientation(self):
        return True
    
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