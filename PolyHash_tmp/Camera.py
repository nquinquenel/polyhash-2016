'''
Created on 23 oct. 2016

@author: Nicolas
'''

class Camera:
    
    def __init__(self, pointageLatitude, pointageLongitude):
        self.pointageLatitude = pointageLatitude
        self.pointageLongitude = pointageLongitude
    
    def prendrePhoto(self):
        return True
    
    def nombrePhotoPossible(self, list):
        return 0
    
    def getPointageCamera(self):
        return self.pointageLatitude, self.pointageLongitude