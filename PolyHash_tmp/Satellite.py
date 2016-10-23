'''
Created on 23 oct. 2016

@author: Nicolas
'''

from Camera import Camera

class Satellite:
    
    def __init__(self, latitude, longitude, vitesse, orientationMax, delaiPhoto):
        self.latitude = latitude
        self.longitude = longitude
        self.vitesse = vitesse
        self.orientationMax = orientationMax
        self.deltaLatitude = 0
        self.deltaLongitude = 0
        self.delaiPhoto = delaiPhoto
        self.changementOrientationMax = 200
        self.orientationMax = 10000
        self.camera = Camera(self.latitude, self.longitude, self.deltaLatitude, self.deltaLongitude)
        
    def changerOrientation(self):
        return True
    
    def calculePosition(self):
        print("Latitude : " , self.latitude , "; Longitude : " , self.longitude , "; Vitesse : " , self.vitesse)
        if self.latitude <= 324000 and self.latitude >= -324000:
            self.latitude = self.latitude + self.vitesse
            self.longitude = self.longitude - 15
        elif self.latitude > 324000:
            self.latitude = (324000*2) - (self.latitude + self.vitesse)
            self.longitude = -(324000*2) + (self.longitude - 15)
            self.vitesse = -self.vitesse
        else:
            self.latitude = -(324000*2) - (self.latitude + self.vitesse)
            self.longitude = -(324000*2) + (self.longitude - 15)
            self.vitesse = -self.vitesse
        if self.longitude < -648000:
            self.longitude = 648000 - (-self.longitude - 648000)
        print("Latitude : " , self.latitude , "; Longitude : " , self.longitude , "; Vitesse : " , self.vitesse)
        return 0
    
    def getOrientationSatellite(self):
        return self.deltaLatitude, self.deltaLongitude
    
    def getPosition(self):
        return self.latitude, self.longitude