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
        """

        self.listeCoordonneesReussies= []
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
        """

        return self.valeurPoints

    def getCoordonnees(self):
        """
        Accesseur - Renvoie la liste des coordonnees des points d'interet de la collection
        :return: la liste des coordonnees (listeCoordonnees)
        """

        return self.listeCoordonnees

    def getTemps(self):
        """
        Accesseur - Renvoie le temps imposé pour la prise des points de la collection
        :return: le temps requis (tempsRequis)
        """

        return self.tempsRequis

    def getCoordonneesReussies(self):
        """
        Accesseur - Renvoie la liste des coordonnees photographiees parmi la liste des coordonnees des points d'interet de la collection (listeCoordonnees)
        :return: la liste des coordonnees photographiees (listeCoordonneesReussies)
        """

        return self.listeCoordonneesReussies

    def suppressionElement(self,liste):
        """
        Supprime les coordonnees du point potographie de listeCoordonnees et les rajoute dans listeCoordonneesReussies
        :param liste: les coordonnees du point photographiees à supprimer de listeCoordonnees
        :return: True si la liste des coordonnees des points d'interet restant a photographies est vide
                False sinon
        """

        self.listeCoordonnees.remove(liste)
        return estVide()

    def estVide(self):
        """
        Verifie si la liste des coordonnees a photographiees est vide (listeCoordonnees)
        :return: True si la liste des coordonnees des points d'interet restant a photographies est vide
                False sinon
        """

        if not self.listeCoordonnees:
            return True
        else:
            return False

    def string(self):
        """
        Simple methode d'impression qui renvoie les informations de l'objet de type Collection
        :return: le score, la liste des coordonnees a photographier, et le temps requis pour photographier les differents points de cette collection
        """

        return "Valeur points: ",self.valeurPoints," Liste coordonnees: ",self.listeCoordonnees," Temps requis: ",self.tempsRequis
