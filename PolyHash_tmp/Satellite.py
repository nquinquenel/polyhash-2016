from math import *
import copy

class Satellite:
    """
    Cette classe s occupe des interactions avec le satellite et la camera
    """

    def __init__(self, latitude, longitude, vitesse, changementOrientationMax, orientationMax, numero):
        """
        Constructeur de Satellite

        :param latitude: la latitude de depart en arcsec
        :param longitude: la longitude de depart en arcsec
        :param vitesse: la vitesse de depart en arcsec
        :param changementOrientationMax: le changement d'orientation max du satellite d un tour a l autre en arcsec (0 < changementOrientationMax < 200)
        :param orientationMax: l orientation max du satellite en arcsec (0 < orientationMax < 10000)
        :param numero: le numero donne a l objet de type Satellite
        :type latitude: int
        :type longitude: int
        :type vitesse: int
        :type changementOrientationMax: int
        :type orientationMax: int
        :type numero: int
        """

        self.latitude = latitude
        self.longitude = longitude
        self.vitesse = vitesse
        self.changementOrientationMax = changementOrientationMax
        self.orientationMax = orientationMax
        self.deltaLatitude = 0
        self.deltaLongitude = 0
        self.pointageLatitude = self.latitude + self.deltaLatitude
        self.pointageLongitude = self.longitude + self.deltaLongitude
        self.delaiPhoto = 1
        self.numero = numero
        self.temps = 0
        self.latitudeDefaut = latitude
        self.longitudeDefaut = longitude
        self.vitesseDefaut = vitesse
        self.rotMaxLat = 0
        self.rotMaxLong = 0
            
    def getPolygone(self, tempsTotal):
        """
        Renvoie les polygones du satellite qui correspond a son projete sur Terre pendant la duree de la simulation

        :param tempsTotal: le temps total de la conversation
        :type tempsTotal: int
        :return: le polygone du satellite
        :rtype: [int]
        """
        res = []
        longitude = self.longitude
        latitude = self.latitude
        vit = copy.deepcopy(self.vitesse)
        totalDistance = vit * tempsTotal
        first = True
        longiTour = False
        while (totalDistance != 0):
            tab = []
            #Permet de définir le début
            if longiTour:
                if (vit > 0):
                    tab.append([latitude - self.orientationMax, longitude - self.orientationMax])
                    tab.append([latitude - self.orientationMax, longitude])
                    tab.append([latitude + self.orientationMax, longitude])
                    longiTour = False
                else:
                    tab.append([latitude + self.orientationMax, longitude + self.orientationMax])
                    tab.append([latitude + self.orientationMax, longitude])
                    tab.append([latitude - self.orientationMax, longitude])
                    longiTour = False
            elif first:
                
                #Si le satellite va vers le haut
                if (vit > 0):
                    #Point en bas à gauche
                    tab.append([latitude - self.orientationMax, longitude - self.orientationMax])
                    #Point en bas à droite
                    tab.append([latitude - self.orientationMax, longitude + self.orientationMax])
                    #Point en haut à droite
                    tab.append([latitude + self.orientationMax, longitude + self.orientationMax])
                else:
                    #Point en haut à gauche
                    tab.append([latitude + self.orientationMax, longitude - self.orientationMax])
                    #Point en haut à droite
                    tab.append([latitude + self.orientationMax, longitude + self.orientationMax])
                    #Point en bas à droite
                    tab.append([latitude - self.orientationMax, longitude + self.orientationMax])
                first = False
            else:
                if (vit > 0):
                    #Point à gauche du bas
                    tab.append([latitude, longitude - self.orientationMax])
                    #Point à droite du bas
                    tab.append([latitude, longitude + self.orientationMax])
                    #Point en haut à droite du bas
                    tab.append([latitude + self.orientationMax, longitude + self.orientationMax])
                else:
                    #Point à gauche du haut
                    tab.append([latitude, longitude - self.orientationMax])
                    #Point à droite du haut
                    tab.append([latitude, longitude + self.orientationMax])
                    #Point en bas à droite du haut
                    tab.append([latitude - self.orientationMax, longitude - self.orientationMax])
                    
            #Si le satellite va vers le haut (trajectoire nord ouest)   
            if (vit > 0):
                distanceLatitude = 324000 - latitude
                #Si on peut faire 1 tour
                if (totalDistance > distanceLatitude):
                    temps = (distanceLatitude / vit)
                    temps = int(temps)
                    distanceLatitude = (vit * temps)
                    pointLatitude = latitude + distanceLatitude
                    pointLongitude = longitude - (15 * temps)
                    
                    if (pointLongitude < -648000):
                        distLongLim = (-648000) - longitude
                        tempsLong = -distLongLim / 15
                        tempsLong = int(tempsLong)
                        distanceLatitude = (tempsLong * vit)
                        pointLatitude = latitude + distanceLatitude
                        pointLongitude = longitude - (15 * tempsLong)

                        tab.append([pointLatitude + self.orientationMax, pointLongitude + self.orientationMax])
                        tab.append([pointLatitude + self.orientationMax, pointLongitude])
                        tab.append([pointLatitude - self.orientationMax, pointLongitude])

                        tempsBis2 = 0
                        while (longitude > -648000):
                            longitude = longitude - 15
                            tempsBis2 += 1
                        totalDistance = totalDistance - distanceLatitude - (tempsBis2 * vit)
                        latitude = latitude + (tempsBis2 * vit)

                        longitude = 647999 + (longitude + 648000)
                        longiTour = True
                        
                    else:
                        tab.append([pointLatitude, pointLongitude + self.orientationMax])
                        tab.append([pointLatitude, pointLongitude - self.orientationMax])
                        tab.append([pointLatitude - self.orientationMax, pointLongitude - self.orientationMax])
                        
                        tempsBis = 0
                        while (latitude < 324000):
                            latitude += vit
                            tempsBis += 1
                        totalDistance = totalDistance - distanceLatitude - (tempsBis * vit)
                        latitude = 648000 - latitude
                        vit = -vit
                        longitude = -648000 + (longitude - (15 * tempsBis))

                        if (longitude < -648000):
                            longitude = 647999 + (longitude + 648000)
                #Si on peut pas faire un tour
                else:
                    temps = distanceLatitude // vit
                    pointLatitude = latitude + distanceLatitude
                    pointLongitude = longitude - (15 * temps)

                    if (pointLongitude < -648000):
                        pointLongitude = 647999 + (pointLongitude + 648000)

                    tab.append([latitude + self.orientationMax, pointLongitude + self.orientationMax])
                    tab.append([latitude + self.orientationMax, pointLongitude - self.orientationMax])
                    tab.append([latitude - self.orientationMax, pointLongitude< - self.orientationMax])

                    totalDistance = 0
            #Si le satellite va vers le bas (trajectoire sud ouest)
            else:
                distanceLatitude = 324000 + latitude
                if (totalDistance > distanceLatitude):
                    temps = (distanceLatitude / vit)
                    temps = int(temps)
                    distanceLatitude = (vit * temps)
                    pointLatitude = latitude - distanceLatitude
                    pointLongitude = longitude + (15 * temps)

                    if (pointLongitude < -648000):
                        distLongLim = (-648000) - longitude
                        tempsLong = -distLongLim / 15
                        tempsLong = int(tempsLong)
                        distanceLatitude = (tempsLong * vit)
                        pointLatitude = latitude + distanceLatitude
                        pointLongitude = longitude - (15 * tempsLong)

                        tab.append([pointLatitude + self.orientationMax, pointLongitude + self.orientationMax])
                        tab.append([pointLatitude + self.orientationMax, pointLongitude])
                        tab.append([pointLatitude - self.orientationMax, pointLongitude])

                        tempsBis2 = 0
                        while (longitude > -648000):
                            longitude = longitude - 15
                            tempsBis2 += 1
                        totalDistance = totalDistance - distanceLatitude - (tempsBis2 * vit)
                        latitude = latitude + (tempsBis2 * vit)

                        longitude = 647999 + (longitude + 648000)
                        longiTour = False
                    else:

                        tab.append([pointLatitude, pointLongitude + self.orientationMax])
                        tab.append([pointLatitude, pointLongitude - self.orientationMax])       
                        tab.append([pointLatitude + self.orientationMax, pointLongitude - self.orientationMax])
                        
                        tempsBis = 0
                        while (latitude > -324000):
                            latitude += vit
                            tempsBis += 1
                        totalDistance = totalDistance - distanceLatitude - (tempsBis * vit)
                        latitude = -648000 - latitude
                        vit = -vit
                        longitude = -648000 + (longitude - (15 * tempsBis))
                        if (longitude < -648000):
                            longitude = 647999 + (longitude + 648000)
                else:
                    temps = distanceLatitude / vit
                    pointLatitude = latitude + distanceLatitude
                    pointLongitude = longitude - (15 * temps)

                    if (pointLongitude < -648000):
                        pointLongitude = 647999 + (pointLongitude + 648000)

                    tab.append([latitude - self.orientationMax, pointLongitude + self.orientationMax])
                    tab.append([latitude - self.orientationMax, pointLongitude - self.orientationMax])
                    tab.append([latitude + self.orientationMax, pointLongitude - self.orientationMax])

                    totalDistance = 0
            #Ajoute un polygone au tableau résultat qui peut en contenir plusieurs
            res.append(tab)
        return res

    def changerOrientationLatitude(self):
        """
        Change la valeur de l'orientation du satellite pour la latitude (deltaLatitude)

        :param valeur: la valeur du changement de l'orientation
        :type valeur: int
        """

        # |valeur| ne doit pas etre superieur changementOrientationMax
        # et ne doit pas depasser les limites de l'orientation maximum
        if abs(self.deltaLatitude) > self.orientationMax:
            raise ValueError("Changement trop important")
        elif self.rotMaxLat-self.deltaLatitude >= 0:
            if self.deltaLatitude + self.changementOrientationMax < self.rotMaxLat:
                self.deltaLatitude += self.changementOrientationMax
            else:
                self.deltaLatitude += self.changementOrientationMax - ((self.deltaLatitude + self.changementOrientationMax) - self.rotMaxLat)
        else:
            if self.deltaLatitude - self.changementOrientationMax > self.rotMaxLat:
                self.deltaLatitude = self.deltaLatitude - self.changementOrientationMax
            else:
                self.deltaLatitude = self.deltaLatitude - (self.changementOrientationMax - (-(self.deltaLatitude - self.changementOrientationMax) + self.rotMaxLat))
        self.calculPointageCamera()

    def changerOrientationLongitude(self):
        """
        Change la valeur de l'orientation du satellite pour la longitude (deltaLongitude)

        :param valeur: La valeur du changement de l'orientation
        :type valeur: int
        """

        # |valeur| ne doit pas etre superieur changementOrientationMax
        # et ne doit pas depasser les limites de l'orientation maximum
        if abs(self.deltaLongitude) > self.orientationMax:
            raise ValueError("Changement trop important")
        #Aller vers la droite
        elif self.rotMaxLong-self.deltaLongitude >= 0:
            if self.deltaLongitude + self.changementOrientationMax < self.rotMaxLong:
                self.deltaLongitude += self.changementOrientationMax
            else:
                self.deltaLongitude += self.changementOrientationMax - ((self.deltaLongitude + self.changementOrientationMax) - self.rotMaxLong)
        #Aller vers la gauche
        else:
            if self.deltaLongitude - self.changementOrientationMax > self.rotMaxLong:
                self.deltaLongitude = self.deltaLongitude - self.changementOrientationMax
            else:
                self.deltaLongitude = self.deltaLongitude - (self.changementOrientationMax - (self.rotMaxLong - (self.deltaLongitude - self.changementOrientationMax)))
        self.calculPointageCamera()
                                                             
    def calculePosition(self):
        """
        Calcul la position du satellite au tour t+1
        """
        #Si latitude + vitesse se trouve entre -90 degre et 90 degre
        if self.latitude + self.vitesse <= 324000 and self.latitude + self.vitesse >= -324000:
            self.latitude = self.latitude + self.vitesse
            self.longitude = self.longitude - 15
        #Si latitude + vitesse se trouve superieur a 90 degre (il vient de depasser le Pole Nord)
        elif self.latitude + self.vitesse > 324000:
            self.latitude = (648000) - (self.latitude + self.vitesse)
            self.longitude = -(648000) + (self.longitude - 15)
            self.vitesse = -self.vitesse
        #Si latitude + vitesse se trouve infenieur a 90 degre (il vient de depasser le Pole Sud)
        else:
            self.latitude = -(648000) - (self.latitude + self.vitesse)
            self.longitude = -(648000) + (self.longitude - 15)
            self.vitesse = -self.vitesse
        #Si longitude depasse -648000" alors longitude repasse à 647999"
        if self.longitude < -648000:
            self.longitude = 648000 - (-self.longitude - 648000)
        self.calculPointageCamera()

    def getOrientationSatellite(self):
        """
        Accesseur - Renvoie l'orientation du satellite

        :return: la valeur de l'orientation pour la latitude (deltaLatitude) et la longitude (deltaLongitude)
        :rtype: int, int
        """

        return self.deltaLatitude, self.deltaLongitude

    def getPosition(self):
        """
        Accesseur - Renvoie la position du satellite

        :return: la latitude et la longitude du satellite
        :rtype:
        """

        return self.latitude, self.longitude

    def calculPointageCamera(self):
        """
        Met a jour le pointage de la camera en prenant en compte l'orientation du satellite (deltaLatitude et deltaLongitude)
        """

        self.pointageLatitude = self.latitude + self.deltaLatitude
        self.pointageLongitude = self.longitude + self.deltaLongitude

    def prendrePhoto(self, tour):
        """
        Prend une photo du point vise par le satellite
        et renvoie les caracteristiques de l'environnement au moment de cette prise

        :param tour: le tour courant
        :type tour: int
        :return: [latitude pointee par le satellite,
                longitude pointee par le satellite,
                numero du satellite,
                tour courant]
        :rtype: [int, int, int, int]
        """

        ret = [0]*4
        ret[0] = self.latitude + self.deltaLatitude
        ret[1] = self.longitude + self.deltaLongitude
        ret[2] = self.numero
        ret[3] = tour
        return ret

    def nombrePhotoPossible(self, listePhoto):
        """
        Renvoie le nombre de photos qui peuvent etre prises par le satellite

        :param listePhoto: la liste des coordonnees des points d'interet d'une collection
        :type listePhoto: [[int, int]]
        :return: le nombre de photos possibles
        :rtype: int
        """

        ret = 0
        for coord in listePhoto:
            if int(int(coord[1]) < self.longitude+self.orientationMax and int(coord[1]) > self.longitude-self.orientationMax) and (int(coord[0]) > self.latitude - self.orientationMax and int(coord[0]) < self.latitude + self.orientationMax):
                ret += 1
        return ret

    def prendrePhotoPossible(self, coord):
        if (coord[1] == self.pointageLongitude) and (coord[0] == self.pointageLatitude):
            return True
        return False

    def photoPossible(self, coord):
        """
        Verifie si la photo peut être prise par le satellite

        :param coord: les coordonnees d'un point d'interet
        :type coord: [int, int]
        :return: True si la photo peut etre prise
                False sinon
        :rtype: boolean
        """

        if (coord[1] < self.longitude+self.orientationMax and coord[1] > self.longitude-self.orientationMax) and (coord[0] > self.latitude - self.orientationMax and coord[0] < self.latitude + self.orientationMax):
            return True
        return False

    def getPointageCamera(self):
        """
        Accesseur -  Renvoie le pointage de la camera (qui prend en compte l'orientation du satellite (deltaLatitude et deltaLongitude))

        :return: la latitude et la longitude du pointage de la camera
        :rtype: int, int
        """

        return self.pointageLatitude, self.pointageLongitude

    def peutPrendrePoint(self, coordSat, coordPoint, tempsActu, tempsPoint):
        ret = True
        deltaT = tempsPoint - tempsActu
        rotMax = deltaT * self.changementOrientationMax
        if rotMax < abs(coordSat[0] - self.deltaLatitude) or rotMax < abs(coordSat[1] - self.deltaLongitude):
            ret = False
        else:
            self.rotMaxLat = coordSat[0]
            self.rotMaxLong = coordSat[1]
        return ret

    def getNumero(self):
        """
        Retourne le numero du satellite

        :return: le numero du satellite
        :rtype: int
        """

        return self.numero

    def getVitesse(self):
        return self.vitesse

    def resetVitesse(self):
        self.vitesse = self.vitesseDefaut

    def resetPos(self):
        self.longitude = self.longitudeDefaut
        self.latitude = self.latitudeDefaut

    def string(self):
        """
        Simple methode d'impression qui renvoie les informations de l'objet de type Satellite

        :return: la latitude, la longitude, la vitesse, le changement d'orientation maximum de la camera, l'orientation maximum de la camera et le numero du satellite
        :rtype: string
        """
        return "Latitude: ",self.latitude," Longitude: ",self.longitude," Vitesse: ",self.vitesse," Changement Orientation Max: ",self.changementOrientationMax," Orientation Max: ",self.orientationMax," Numero: ",self.numero
