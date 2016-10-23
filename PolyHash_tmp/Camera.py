'''
Created on 23 oct. 2016

@author: Nicolas
'''

class Camera:
    
    def __init__(self, latitude, longitude, deltaLatitude, deltaLongitude):
        self.pointageLatitude = latitude - deltaLatitude
        self.pointageLongitude = longitude - deltaLongitude
    
    def prendrePhoto(self):
        return True
    
    def nombrePhotoPossible(self, list):
        return 0
    
    def getPointageCamera(self):
        return self.pointageLatitude, self.pointageLongitude