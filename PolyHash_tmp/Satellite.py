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

    def changerOrientation(self, coord):
        #Si coord latitude est au nord du pointage de la camera
        if coord[0] > self.pointageLatitude and self.deltaLatitude < self.orientationMax:
            if self.pointageLatitude + self.changementOrientationMax > coord[0]:
                self.changerOrientationLatitude((self.pointageLatitude+self.changementOrientationMax) - coord[0])
            else:
                if self.deltaLatitude + self.changementOrientationMax > self.orientationMax:
                    self.changerOrientationLatitude(self.orientationMax - self.deltaLatitude)
                else:
                    self.changerOrientationLatitude(self.changementOrientationMax)
        #Si coord lati est au sud du pointage de la camera
        elif coord[0] < self.pointageLatitude and self.deltaLatitude > -self.orientationMax:
            #Si en descendant la camera du changement Max on depasse (passe en dessous) de coord lati
            if self.pointageLatitude - self.changementOrientationMax <= coord[0]:
                if self.deltaLatitude > 0:
                    self.changerOrientationLatitude(self.pointageLatitude - self.changementOrientationMax - coord[0])
                else:
                    self.changerOrientationLatitude(coord[0] - (self.pointageLatitude - self.changementOrientationMax))
            #Si on reste au dessus
            else:
                #Si en bougeant on ne depasse pas l orientation max de la camera
                if self.deltaLatitude + self.changementOrientationMax < self.orientationMax and  self.deltaLatitude - self.changementOrientationMax  > -self.orientationMax:
                    self.changerOrientationLatitude(-self.changementOrientationMax)
                #Si on depasse l orientation max de la camera
                else:
                    if self.deltaLatitude > 0:
                        self.changerOrientationLatitude(-(self.orientationMax - self.deltaLatitude))
                    else:
                        self.changerOrientationLatitude(-(self.orientationMax + self.deltaLatitude))

        #Si coord longi est a l est du pointage de la camera
        if coord[1] > self.pointageLongitude and self.deltaLongitude < self.orientationMax:
            if self.pointageLongitude + self.changementOrientationMax > coord[1]:
                self.changerOrientationLongitude(coord[1] - self.pointageLongitude)
            else:
                if self.deltaLongitude + self.changementOrientationMax > self.orientationMax:
                    self.changerOrientationLongitude(self.orientationMax - self.deltaLongitude)
                else:
                    self.changerOrientationLongitude(self.changementOrientationMax)
        #Si coord longi est a l ouest du pointage de la camera
        elif coord[1] < self.pointageLongitude and self.deltaLongitude > -self.orientationMax:
            #Si en allant a gauche on depasse la coord longi
            if self.pointageLongitude - self.changementOrientationMax <= coord[1]:
                if self.deltaLongitude > 0:
                    self.changerOrientationLongitude((self.pointageLongitude - self.changementOrientationMax) - coord[1])
                else:
                    self.changerOrientationLongitude(-(self.pointageLongitude - self.changementOrientationMax) + coord[1])
            #Si on reste a l est
            else:
                #Si en bougeant on ne depasse pas l orientation max
                if self.deltaLongitude + self.changementOrientationMax < self.orientationMax and self.deltaLongitude - self.changementOrientationMax > -self.orientationMax:
                    self.changerOrientationLongitude(-self.changementOrientationMax)
                else:
                    if self.deltaLongitude > 0:
                        self.changerOrientationLongitude(-(self.orientationMax - self.deltaLongitude))
                    else:
                        self.changerOrientationLongitude(-(self.orientationMax + self.deltaLongitude))

    def getPolygone(self, tempsTotal):
        res = []
        latTmp = self.latitude
        longTmp = self.longitude
        totalDistance = self.vitesse * tempsTotal
        disLat = 0
        first = True
        tab = []
        while totalDistance != 0:
            if first:
                if (self.vitesse > 0):
                    p1 = [self.latitude-self.orientationMax, self.longitude-self.orientationMax]
                    p2 = [self.latitude-self.orientationMax, self.longitude+self.orientationMax]
                else:
                    p1 = [self.latitude+self.orientationMax, self.longitude-self.orientationMax]
                    p2 = [self.latitude+self.orientationMax, self.longitude+self.orientationMax]
                first = False
            else:
                if (self.vitesse > 0):
                    p1 = [-324000, longTmp-self.orientationMax]
                    p2 = [-324000, longTmp+self.orientationMax]
                else:
                    p1 = [324000, longTmp-self.orientationMax]
                    p2 = [324000, longTmp+self.orientationMax]
            tab.append(p1)
            tab.append(p2)
            #Si le satellite va vers le haut
            if (self.vitesse > 0):
                disLat = 324000 - latTmp
                #Si on peut faire 1 tour
                if (totalDistance > disLat):
                    posLong = self.longitude - (15 * disLat/self.vitesse)
                    if (posLong < -648000):
                        posLong = 647999 - (-648000 - posLong)
                    p3 = [324000, posLong-self.orientationMax]
                    p4 = [324000, posLong+self.orientationMax]
                    totalDistance = totalDistance - disLat
                    longTmp = posLong
                    latTmp = -324000
                else:
                    posLong = longTmp - (15 * (totalDistance/self.vitesse))
                    if (posLong < -648000):
                        posLong = 647999 - (-648000 - posLong)
                    p3 = [latTmp + totalDistance, posLong-self.orientationMax]
                    p4 = [latTmp + totalDistance, posLong+self.orientationMax]
                    totalDistance = 0
            #Si le satellite va vers le bas
            else:
                disLat = -324000 - latTmp
                #Si on peut faire 1 tour
                if (totalDistance < disLat):
                    posLong = self.longitude - (15 * abs(disLat)/-self.vitesse)
                    if (posLong < -648000):
                        posLong = 647999 - (-648000 - posLong)
                    p3 = [-324000, posLong-self.orientationMax]
                    p4 = [-324000, posLong+self.orientationMax]
                    totalDistance = totalDistance - disLat
                    longTmp = posLong
                    latTmp = 324000
                else:
                    posLong = longTmp - (15 * (abs(totalDistance)/-self.vitesse))
                    if (posLong < -648000):
                        posLong = 647999 - (-648000 - posLong)
                    p3 = [latTmp + totalDistance, posLong-self.orientationMax]
                    p4 = [latTmp + totalDistance, posLong+self.orientationMax]
                    totalDistance = 0
            tab.append(p3)
            tab.append(p4)
        return tab

    def changerOrientationLatitude(self, valeur):
        """
        Change la valeur de l'orientation du satellite pour la latitude (deltaLatitude)

        :param valeur: la valeur du changement de l'orientation
        :type valeur: int
        """

        # |valeur| ne doit pas etre superieur changementOrientationMax
        # et ne doit pas depasser les limites de l'orientation maximum
        if valeur > self.changementOrientationMax or valeur < -self.changementOrientationMax:
            raise ValueError("Changement trop important")
        elif (self.deltaLatitude + valeur) < -self.orientationMax or (self.deltaLatitude + valeur) > self.orientationMax:
            raise ValueError("Hors des limites de l'orientation maximum")
        else:
            self.deltaLatitude += valeur
        self.calculPointageCamera()

    def changerOrientationLongitude(self, valeur):
        """
        Change la valeur de l'orientation du satellite pour la longitude (deltaLongitude)

        :param valeur: La valeur du changement de l'orientation
        :type valeur: int
        """

        # |valeur| ne doit pas etre superieur changementOrientationMax
        # et ne doit pas depasser les limites de l'orientation maximum
        if valeur > self.changementOrientationMax or valeur < -self.changementOrientationMax:
            raise ValueError("Changement trop important")
        elif (self.deltaLongitude + valeur) < -self.orientationMax or (self.deltaLongitude + valeur) > self.orientationMax:
            raise ValueError("Hors des limites de l'orientation maximum")
        else:
            self.deltaLongitude += valeur
        self.calculPointageCamera()

    def calculePosition(self):
        """
        Calcul la position du satellite au tour t+1
        """

        #Si latitude + vitesse se trouve entre -90 degre et 90 degre
        if self.latitude <= 324000 and self.latitude >= -324000:
            self.latitude = self.latitude + self.vitesse
            self.longitude = self.longitude - 15
        #Si latitude + vitesse se trouve superieur a 90 degre (il vient de depasser le Pole Nord)
        elif self.latitude > 324000:
            self.latitude = (324000*2) - (self.latitude + self.vitesse)
            self.longitude = -(324000*2) + (self.longitude - 15)
            self.vitesse = -self.vitesse
        #Si latitude + vitesse se trouve infenieur a 90 degre (il vient de depasser le Pole Sud)
        else:
            self.latitude = -(324000*2) - (self.latitude + self.vitesse)
            self.longitude = -(324000*2) + (self.longitude - 15)
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

    def getNumero(self):
        """
        Retourne le numero du satellite

        :return: le numero du satellite
        :rtype: int
        """

        return self.numero

    def string(self):
        return "Latitude: ",self.latitude," Longitude: ",self.longitude," Vitesse: ",self.vitesse," Changement Orientation Max: ",self.changementOrientationMax," Orientation Max: ",self.orientationMax," Numero: ",self.numero
