class Satellite:

    # Constructeur de Satellite
    #
    # @param latitude la latitude de départ en arcsec
    # @param longitude la longitude de départ en arcsec
    # @param vitesse la vitesse de départ en arcsec
    # @param changementOrientationMax le changement d'orientation max du satellite d'un tour à l'autre en arcsec (0 < changementOrientationMax < 200)
    # @param orientationMax l'orientation max du satellite en arcsec (0 < orientationMax < 10000)
    # @param numero le numéro donné à l'objet de type Satellite
    #
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
        self.delaiPhoto = 1
        self.numero = numero

    # Change la valeur de l'orientation pour la latitude (deltaLatitude)
    #
    # @param valeur la valeur du changement de l'orientation
    #
    def changerOrientationLatitude(self, valeur):
        # |valeur| ne doit pas etre superieur changementOrientationMax
        # et ne doit pas depasser les limites de l'orientation maximum
        if valeur > self.changementOrientationMax or valeur < -self.changementOrientationMax:
            raise ValueError("Changement trop important")
        elif (self.deltaLatitude + valeur) < -self.orientationMax or (self.deltaLatitude + valeur) > self.orientationMax:
            raise ValueError("Hors des limites de l'orientation maximum")
        else:
            self.deltaLatitude += valeur

    # Change la valeur de l'orientation pour la longitude (deltaLongitude)
    #
    # @param valeur La valeur du changement de l'orientation
    #
    def changerOrientationLongitude(self, valeur):
        # |valeur| ne doit pas etre superieur changementOrientationMax
        # et ne doit pas depasser les limites de l'orientation maximum
        if valeur > self.changementOrientationMax or valeur < -self.changementOrientationMax:
            raise ValueError("Changement trop important")
        elif (self.deltaLongitude + valeur) < -self.orientationMax or (self.deltaLongitude + valeur) > self.orientationMax:
            raise ValueError("Hors des limites de l'orientation maximum")
        else:
            self.deltaLongitude += valeur

    # Calcul la position du satellite au tour t+1
    #
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

    # Accesseur - Renvoie l'orientation du satellite
    #
    # @return la valeur de l'orientation pour la latitude (deltaLatitude)
    # @return la valeur de l'orientation pour la longitude (deltaLongitude)
    #
    def getOrientationSatellite(self):
        return self.deltaLatitude, self.deltaLongitude

    # Accesseur - Renvoie la position du satellite
    #
    # @return la latitude du satellite (latitude)
    # @return la longitude du satellite (longitude)
    #
    def getPosition(self):
        return self.latitude, self.longitude

    # Met à jour le pointage de la caméra en prenant en compte l'orientation du satellite (deltaLatitude et deltaLongitude)
    #
    def calculPointageCamera(self):
        self.pointageLatitude = self.latitude + self.deltaLatitude
        self.pointageLongitude = self.longitude + self.deltaLongitude

    # Prend une photo du point visé par le satellite
    #
    # et renvoie les caractéristiques de l'environnement au moment de cette prise
    # @param tour le tour courant
    # @return [latitude pointée par le satellite,
    #          longitude pointée par le satellite,
    #          numéro du satellite,
    #          tour courant]
    #
    def prendrePhoto(self, tour):
        ret = [4]
        ret[0] = self.latitude + self.deltaLatitude
        ret[1] = self.longitude + self.deltaLongitude
        ret[2] = self.numero
        ret[3] = tour
        return ret

    # Renvoie le nombre de photos qui peuvent être prises par le satellite
    #
    # @return le nombre de photos possibles
    #
    def nombrePhotoPossible(liste):
	    return 0

    # Accesseur -  Renvoie le pointage de la caméra (qui prend en compte l'orientation du satellite (deltaLatitude et deltaLongitude))
    #
    # @return la latitude du pointage de la caméra (pointageLatitude)
    # @return la longitude du pointage de la caméra (pointageLongitude)
    #
    def getPointageCamera():
	    return self.pointageLatitude, self.pointageLongitude
