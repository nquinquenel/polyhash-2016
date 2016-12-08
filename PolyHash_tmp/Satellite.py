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
        self.vitesseDefaut = vitesse

    def prochainPoint(self, coord):
        if (self.vitesse > 0 and (self.latitude - self.orientationMax) < coord[0]):
            temps = ((coord[0] - (self.latitude + self.orientationMax)) // self.vitesse) + 1
            self.latitude += self.vitesse * temps
            self.longitude = self.longitude - (15 * temps)
        elif (self.vitesse > 0 and (self.latitude - self.orientationMax) > coord[0]):
            distance = 324000 - (self.latitude + self.orientationMax)
            distance = distance + (coord[0] + 324000)
            temps = (distance // self.vitesse) + 1
            self.latitude = coord[0] - self.orientationMax
        elif (self.vitesse < 0 and (self.latitude + self.orientationMax) > coord[0]):
            temps = (-(coord[0] - (self.latitude - self.orientationMax)) // -self.vitesse) + 1
            self.latitude = coord[0] + self.orientationMax
            self.longitude = self.longitude - (15 * temps)
        elif (self.vitesse < 0 and (self.latitude + self.orientationMax) < coord[0]):
            distance = -(-324000 - (self.latitude - self.orientationMax))
            distance = distance + (324000 + coord[0])
            temps = (distance // self.vitesse) + 1
            self.latitude = coord[0] + self.orientationMax
        
        self.longitude = self.longitude - (15 * temps)
        if (self.longitude < -648000):
            self.longitude = 647999 - (-self.longitude - 648000)
        self.temps += temps
        res = []
        res.append(self.temps)
        res.append(self.numero)
        res.append(coord)
        return res

    def changerOrientation(self, coord):
        """
        Change l'orientation de la camera du satellite en fonction du prochain point a photographier

        :param coord: les coordonnees du prochain point a photographier
        :type coord: [int, int]
        """
        distanceLatitude = coord[0] - self.pointageLatitude
        distanceLongitude = coord[1] - self.pointageLongitude
        
        #Si coord latitude est au nord du pointage de la camera
        if coord[0] > self.pointageLatitude and self.deltaLatitude < self.orientationMax:
            #Si la distance est plus petite que le changement d'orientation max
            if distanceLatitude < self.changementOrientationMax:
                #Si la distance est plus petite que ce que peut encore bouger le satellite
                if distanceLatitude < (self.orientationMax - self.deltaLatitude):
                    self.changerOrientationLatitude(distanceLatitude)
                else:
                    self.changerOrientationLatitude(self.orientationMax - self.deltaLatitude)
            else:
                if self.changementOrientationMax < (self.orientationMax - self.deltaLatitude):
                    self.changerOrientationLatitude(self.changementOrientationMax)
                else:
                    self.changerOrientationLatitude(self.orientationMax - self.deltaLatitude)

        elif coord[0] < self.pointageLatitude and self.deltaLatitude > -self.orientationMax:
            if -distanceLatitude < (self.changementOrientationMax):
                if -distanceLatitude < (self.orientationMax + self.deltaLatitude):
                    self.changerOrientationLatitude(distanceLatitude)
                else:
                    self.changerOrientationLatitude(-self.orientationMax + self.deltaLatitude)
            else:
                if self.changementOrientationMax < (self.orientationMax + self.deltaLatitude):
                    coef = (coord[0] - self.pointageLatitude)%-self.vitesse
                    if coef > self.changementOrientationMax:
                        self.changerOrientationLatitude(-self.changementOrientationMax)
                    elif coef < self.changementOrientationMax:
                        self.changerOrientationLatitude(self.changementOrientationMax)
                    elif coef != 0:
                        print(coef)
                        self.changerOrientationLatitude(coef)
                else:
                    self.changerOrientationLatitude(-self.orientationMax - self.deltaLatitude)

        #Si coord longitude est à l'est du pointage de la camera
        if coord[1] > self.pointageLongitude and self.deltaLongitude < self.orientationMax:
            #Si la distance est plus petite que le chang
            if distanceLongitude < (self.changementOrientationMax):
                if distanceLongitude < (self.orientationMax - self.deltaLongitude):
                    self.changerOrientationLongitude(distanceLongitude)
                else:
                    self.changerOrientationLongitude(self.orientationMax - self.deltaLongitude)
            else:
                if self.changementOrientationMax < (self.orientationMax -self.deltaLongitude):
                    self.changerOrientationLongitude(self.changementOrientationMax)
                else:
                    self.changerOrientationLongitude(self.orientationMax - self.deltaLongitude)

        elif coord[1] < self.pointageLongitude and self.deltaLongitude > -self.orientationMax:
            if -distanceLongitude < (self.changementOrientationMax):
                if -distanceLongitude < (self.orientationMax + self.deltaLongitude):
                    self.changerOrientationLongitude(distanceLongitude)
                else:
                    self.changerOrientationLongitude(-self.orientationMax - self.deltaLongitude)
            else:
                if self.changementOrientationMax < (self.orientationMax + self.deltaLongitude):
                    self.changerOrientationLongitude(-self.changementOrientationMax)
                else:
                    self.changerOrientationLongitude(-self.orientationMax - self.deltaLongitude)

        """
        #Si coord latitude est au nord du pointage de la camera
        if coord[0] > self.pointageLatitude and self.deltaLatitude < self.orientationMax:
            if self.pointageLatitude + self.changementOrientationMax > coord[0]:
                if self.deltaLatitude + self.changementOrientationMax < self.orientationMax and self.deltaLatitude - self.changementOrientationMax > -self.orientationMax:
                    self.changerOrientationLongitude(coord[0] - self.pointageLatitude)
                else:
                    if self.deltaLatitude > 0:
                        self.changerOrientationLatitude(self.orientationMax - self.deltaLatitude)
                    else:
                        self.changerOrientationLatitude(self.orientationMax + self.deltaLatitude)
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
                if self.deltaLongitude + self.changementOrientationMax < self.orientationMax and self.deltaLongitude - self.changementOrientationMax > -self.orientationMax:
                    self.changerOrientationLongitude(coord[1] - self.pointageLongitude)
                else:
                    if self.deltaLongitude > 0:
                        self.changerOrientationLongitude(self.orientationMax - self.deltaLongitude)
                    else:
                        self.changerOrientationLongitude(self.orientationMax + self.deltaLongitude)
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
    """
            
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
        while (totalDistance != 0):
            tab = []
            #Permet de définir le début
            if first:
                
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
                    temps = distanceLatitude // vit
                    distanceLatitude = (vit * temps)
                    pointLatitude = latitude + distanceLatitude
                    pointLongitude = longitude - (15 * temps)
                    
                    if (pointLongitude < -648000):
                        pointLongitude = 647999 + (pointLongitude + 648000)
                    
                    tab.append([pointLatitude, pointLongitude + self.orientationMax])
                    tab.append([pointLatitude, pointLongitude - self.orientationMax])
                    tab.append([pointLatitude - self.orientationMax, pointLongitude - self.orientationMax])
                    
                    tempsBis = 0
                    while (latitude < 324000):
                        latitude += vit
                        tempsBis += 1
                    totalDistance = totalDistance - distanceLatitude - (latitude - 324000)
                    latitude = 648000 - latitude
                    vit = -vit
                    longitude = -648000 + (longitude - (15 * tempsBis))

                    if (longitude < -648000):
                        longitude = 647999 + (longitude + 648000)
                #Si on peut pas faire un tour
                else:
                    temps = distanceLatitude / vit
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
                    temps = distanceLatitude // vit
                    distanceLatitude = (vit * temps)
                    pointLatitude = latitude - distanceLatitude
                    pointLongitude = longitude + (15 * temps)

                    if (pointLongitude < -648000):
                        pointLongitude = 647999 + (pointLongitude + 648000)

                    tab.append([pointLatitude, pointLongitude + self.orientationMax])
                    tab.append([pointLatitude, pointLongitude - self.orientationMax])       
                    tab.append([pointLatitude + self.orientationMax, pointLongitude - self.orientationMax])
                    
                    tempsBis = 0
                    while (latitude > -324000):
                        latitude += vit
                        tempsBis += 1
                    totalDistance = totalDistance - distanceLatitude - (latitude + 324000)
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
        if self.latitude + self.vitesse <= 324000 and self.latitude + self.vitesse >= -324000:
            self.latitude = self.latitude + self.vitesse
            self.longitude = self.longitude - 15
        #Si latitude + vitesse se trouve superieur a 90 degre (il vient de depasser le Pole Nord)
        elif self.latitude + self.vitesse > 324000:
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

    def peutPrendrePoint(self, coord, tempsCoord, tempsActu):
        ret = True
        temps = (coord[0] - self.pointageLatitude) / self.vitesse
        if (temps) > (tempsCoord - tempsActu):
            ret = False
        if (coord[1] - self.pointageLongitude)/15 > (tempsCoord - tempsActu):
            ret = False
        return ret


    def setPointageCamera(self, latitude, longitude):
        self.pointageLatitude = latitude
        self.pointageLongitude = longitude

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

    def string(self):
        """
        Simple methode d'impression qui renvoie les informations de l'objet de type Satellite

        :return: la latitude, la longitude, la vitesse, le changement d'orientation maximum de la camera, l'orientation maximum de la camera et le numero du satellite
        :rtype: string
        """
        return "Latitude: ",self.latitude," Longitude: ",self.longitude," Vitesse: ",self.vitesse," Changement Orientation Max: ",self.changementOrientationMax," Orientation Max: ",self.orientationMax," Numero: ",self.numero
