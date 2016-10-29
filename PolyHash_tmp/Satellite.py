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
        :param changementOrientationMax: le changement d'orientation max du satellite d'un tour a l'autre en arcsec (0 < changementOrientationMax < 200)
        :param orientationMax: l'orientation max du satellite en arcsec (0 < orientationMax < 10000)
        :param numero: le numero donne a l'objet de type Satellite
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

    def changerOrientationLatitude(self, valeur):
        """
        Change la valeur de l'orientation du satellite pour la latitude (deltaLatitude)
        :param valeur: la valeur du changement de l'orientation
        """
        
        # |valeur| ne doit pas etre superieur changementOrientationMax
        # et ne doit pas depasser les limites de l'orientation maximum
        if valeur > self.changementOrientationMax or valeur < -self.changementOrientationMax:
            raise ValueError("Changement trop important")
        elif (self.deltaLatitude + valeur) < -self.orientationMax or (self.deltaLatitude + valeur) > self.orientationMax:
            raise ValueError("Hors des limites de l'orientation maximum")
        else:
            self.deltaLatitude += valeur

    def changerOrientationLongitude(self, valeur):
        """
        Change la valeur de l'orientation du satellite pour la longitude (deltaLongitude)
        :param valeur: La valeur du changement de l'orientation
        """
        
        # |valeur| ne doit pas etre superieur changementOrientationMax
        # et ne doit pas depasser les limites de l'orientation maximum
        if valeur > self.changementOrientationMax or valeur < -self.changementOrientationMax:
            raise ValueError("Changement trop important")
        elif (self.deltaLongitude + valeur) < -self.orientationMax or (self.deltaLongitude + valeur) > self.orientationMax:
            raise ValueError("Hors des limites de l'orientation maximum")
        else:
            self.deltaLongitude += valeur

    def calculePosition(self):
        """
        Calcul la position du satellite au tour t+1
        """
        
        #Si latitude + vitesse se trouve entre -90° et 90°
        if self.latitude <= 324000 and self.latitude >= -324000:
            self.latitude = self.latitude + self.vitesse
            self.longitude = self.longitude - 15
        #Si latitude + vitesse se trouve superieur a 90° (il vient de depasser le Pole Nord)
        elif self.latitude > 324000:
            self.latitude = (324000*2) - (self.latitude + self.vitesse)
            self.longitude = -(324000*2) + (self.longitude - 15)
            self.vitesse = -self.vitesse
        #Si latitude + vitesse se trouve infenieur a 90° (il vient de depasser le Pole Sud)
        else:
            self.latitude = -(324000*2) - (self.latitude + self.vitesse)
            self.longitude = -(324000*2) + (self.longitude - 15)
            self.vitesse = -self.vitesse
        #Si longitude depasse -648000" alors longitude repasse Ã  647999"
        if self.longitude < -648000:
            self.longitude = 648000 - (-self.longitude - 648000)
        print("Latitude : " , self.latitude , "; Longitude : " , self.longitude , "; Vitesse : " , self.vitesse)

    def getOrientationSatellite(self):
        """
        Accesseur - Renvoie l'orientation du satellite
        :return: la valeur de l'orientation pour la latitude (deltaLatitude) et la longitude (deltaLongitude)
        """
        
        return self.deltaLatitude, self.deltaLongitude

    def getPosition(self):
        """
        Accesseur - Renvoie la position du satellite
        :return: la latitude et la longitude du satellite
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
        :return: [latitude pointee par le satellite,
                longitude pointee par le satellite,
                numero du satellite, tour courant]
        """
        
        ret = [4]
        ret[0] = self.latitude + self.deltaLatitude
        ret[1] = self.longitude + self.deltaLongitude
        ret[2] = self.numero
        ret[3] = tour
        return ret

    def nombrePhotoPossible(liste):
        """
        Renvoie le nombre de photos qui peuvent etre prises par le satellite
        :return: le nombre de photos possibles
        """
        
        return 0

    def getPointageCamera():
        """
        Accesseur -  Renvoie le pointage de la camera (qui prend en compte l'orientation du satellite (deltaLatitude et deltaLongitude))
        :return: la latitude et la longitude du pointage de la camera
        """
        
        return self.pointageLatitude, self.pointageLongitude
