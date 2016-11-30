import copy

class Collection:
    """
    Cette classe gere les collections d images
    """

    def __init__(self,valeurPoints,listeCoordonnees,tempsRequis):
        """
        Constructeur de Collection

        :param valeurPoints: le score offert pour la prise de vue de chaque point d'interet de la collection
        :param listeCoordonnees: la liste des coordonnees des points d'interet de la collection
        :param tempsRequis: le temps imposé pour la prise des points de la collection
        :type valeurPoints: int
        :type listeCoordonnees: [[int, int]]
        :type tempsRequis: int
        """

        self.listeCoordonneesReussies = []
        self.valeurPoints = valeurPoints
        if(tempsRequis != None or listeCoordonnees != None):
            self.listeCoordonnees = listeCoordonnees
            self.tempsRequis = tempsRequis
        else:
            self.listeCoordonnees = []
            self.tempsRequis = []

    def getvaleur(self):
        """
        Accesseur - Renvoie le score offert pour la prise de vue de chaque point d'interet de la collection

        :return: les valeur des points (valeurPoints)
        :rtype: int
        """

        return self.valeurPoints

    def getCoordonnees(self):
        """
        Accesseur - Renvoie la liste des coordonnees des points d'interet de la collection

        :return: la liste des coordonnees (listeCoordonnees)
        :rtype: [[int, int]]
        """

        return self.listeCoordonnees

    def getTemps(self):
        """
        Accesseur - Renvoie le temps imposé pour la prise des points de la collection

        :return: le temps requis (tempsRequis)
        :rtype: int
        """

        return self.tempsRequis

    def getCoordonneesReussies(self):
        """
        Accesseur - Renvoie la liste des coordonnees photographiees parmi la liste des coordonnees des points d'interet de la collection (listeCoordonnees)

        :return: la liste des coordonnees photographiees (listeCoordonneesReussies)
        :rtype: [[int, int, int, int]]
        """

        return self.listeCoordonneesReussies

    def ajouteElementCoordonneesReussies(self,donnees):
        """
        Methode permettant d ajouter la liste des coordonnees reussies et des donnees dans la listeCoordonneesReussies

        :param donnees: les coordonnees du point photographiees, le tour et le numero du satelitte
        :type donnees: [int, int, int, int]
        """
        self.listeCoordonneesReussies.append(donnees)

    def fusionDonnees(self,coord,tour,numSatellite):
        """
        Methode permettant, lorsqu'un point est photographie, d'y associer le tour courant et le numero du satellite l'ayant pris en photo

        :param coord: les coordonnees du point photographiees
        :type coord: [int, int]
        :param tour: tour durant lequel la photographie est prise
        :type tour: int
        :param numSatellite: numero du satellite ayant pris la photographie
        :type numSatellite: int
        :return: la liste contenant toutes les donnes
        :rtype: [[int, int, int, int]]
        """
        tabClone = copy.deepcopy(coord)
        tabClone.append(tour)
        tabClone.append(numSatellite)
        return tabClone

    def prisePhoto(self,coord,tour,numSatellite):
        """
        Methode permettant de gerer la prise d une photo au sein de la classe Collection

        :param coord: les coordonnees du point photographiees
        :type coord: [int, int]
        :param tour: tour durant lequel la photographie est prise
        :type tour: int
        :param numSatellite: numero du satellite ayant pris la photographie
        :type numSatellite: int
        :return: True si la liste des coordonnees des points d'interet restant a photographies est vide
                False sinon
        :rtype: boolean
        """

        # si le point n'est pas dans listeCoordonnees, cela declenchera une exception
        try:
            # essai de suppression des coordonnees du point de listeCoordonnees
            self.listeCoordonnees.remove(coord)
            # L'exception ValueError n'est pas declenchee, on peut donc rajouter ce point dans la liste des coordonnees reussies (listeCoordonneesReussies)
            self.ajouteElementCoordonneesReussies(self.fusionDonnees(coord,tour,numSatellite))
        except ValueError:
            pass


    def estVide(self):
        """
        Verifie si la liste des coordonnees a photographiees est vide (listeCoordonnees)

        :return: True si la liste des coordonnees des points d'interet restant a photographies est vide
                False sinon

        :rtype: boolean
        """

        if not self.listeCoordonnees:
            return True
        else:
            return False

    def string(self):
        """
        Simple methode d'impression qui renvoie les informations de l'objet de type Collection

        :return: le score, la liste des coordonnees a photographier, et le temps requis pour photographier les differents points de cette collection
        :rtype: string
        """

        return "Valeur points: ",self.valeurPoints," Liste coordonnees: ",self.listeCoordonnees," Temps requis: ",self.tempsRequis
