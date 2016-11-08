from Temps import Temps
from Collection import Collection
from Satellite import Satellite

class Lanceur:
    """
    Cette classe s'occupe de gerer les entrees sorties et de lancer la simulation
    """

    def __init__(self,fichier):
        """
        Constructeur de Lanceur

        :param fichier: Le chemin du fichier contenant les donnees d'entree en caracteres ASCII
        :type fichier: string
        """

        self.listeSatellite = []
        self.listeCollection = []
        self.listePhotosPossibles = []
        # la liste de toutes les coordonnees de toutes les collections triees (par latitude croissante, si meme latitude par longitude decroissante)
        self.listeCoordonneesTriees = []
        self.score = 0
        self.temps = None
        self.nomFichier = fichier
        self.lectureFichier()
        self.lancerSimulation()

    def lectureFichier(self):
        """
        Lit le fichier et en extrait:
        le temps de la simulation
        le nombre de satellites
        les parametres initiaux des satellites:
            latitude de depart
            longitude de depart
            vitesse de depart
            changement d'orientation max d'un tour a l'autre
            orientation max
        le nombre d'images dans la collection
        les points d'interet:
            score rapporte pour la prise d'un point d'interet
            latitude
            longitude
            intervals de prise de vue requis
        """

        with open(self.nomFichier,'r') as f:
            #Premiere ligne pour le temps
            self.temps = Temps(int(f.readline()))
            #On creer les satellites
            for i in range(0, int(f.readline())):
                coord = f.readline().split(" ")
                self.listeSatellite.append(Satellite(int(coord[0]),int(coord[1]),float(coord[2]),int(coord[3]),int(coord[4]),i))
            #Ajout des collections d images
            for i in range(0, int(f.readline())):
                #line contient 1) Points 2) Nombre d images 3) Nombre d intervalles de temps
                line = f.readline().split(" ")
                images = []
                temps = []
                #Ajoute les coordonnees des images
                for p in range(0, int(line[1])):
                    images.append(f.readline().strip('\n').split(" "))
                    #Parcours de images pour initialiser listeCoordonneesTriees
                    for coord in images:
                        #Si la coordonnees n'est pas deja dans listeCoordonneesTriees, alors on l'ajoute
                        if(coord not in self.listeCoordonneesTriees):
                            self.listeCoordonneesTriees.append(coord)
                #Ajoute les intervalles de temps
                for p in range(0, int(line[2])):
                    temps.append(f.readline().strip('\n').split(" "))
                #Ajoute la collection
                self.listeCollection.append(Collection(line[0], images, temps))
            #Tri par latitude croissante et, si meme latitude par longitude decroissante
            self.trierListeCoordonneesTriees()
            #Initialise la liste des photos sur la trajectoire des satellites
            """self.initialiserListePhotosPossibles()"""



        """
        compteur = 0
        boucle = 0
        collection = None
        boucle2 = 0
        boucle3 = 0
        with open(self.nomFichier,'r') as f:
            for ligne in f:
                #Initialisation du temps de la simulation
                if(compteur == 0):
                    self.temps = Temps(int(ligne))
                    print(str(ligne) + ": temps de la simulation")
                    compteur += 1
                #Nombre de satellites
                elif(compteur == 1):
                    boucle = int(ligne)
                    print(str(ligne) + ": nombre de satellites")
                    compteur += 1
                #Decoupage des satellites
                elif(compteur == 2):
                    coord = ligne.split(" ")
                    print(str(coord[0])+ "," + str(coord[1]) + "," + str(coord[2]) + "," + str(coord[3]) + "," + str(coord[4]) + ": nouveau satelitte")
                    self.listeSatellite.append(Satellite(float(coord[0]),float(coord[1]),int(coord[2]),float(coord[3]),float(coord[4]),boucle))
                    boucle -= 1
                    if(boucle == 0):
                        compteur += 1
                #Nombre de collections
                elif(compteur == 3):
                    boucle = int(ligne)
                    print(str(ligne) + ": nombre de collections")
                    compteur += 1
                #Decoupage de collections
                elif(compteur == 4):
                    value = ligne.split(" ")
                    print(value[0] + ": Score de la collection, " + value[1] + ": Nombre d'images, " + value[2] + ": Nombre de conditions")
                    boucle2 = int(value[1])
                    boucle3 = int(value[2])
                    collection = Collection(int(value[0]))
                    self.getListeCollection().append(collection)
                    compteur += 1
                #Repartition des coordonnees
                elif(compteur == 5):
                    liste = ligne.split(" ")
                    liste[0] = float(liste[0])
                    liste[1] = float(liste[1])
                    print(liste)
                    collection.getCoordonnees().append(liste)
                    bouclteste2 -= 1
                    if(boucle2 == 0):
                        compteur += 1
                    #Delais de temps
                elif(compteur == 6):
                    liste = ligne.split(" ")
                    liste[0] = float(liste[0])
                    liste[1] = float(liste[1])
                    print(liste)
                    collection.getTemps().append(liste)
                    boucle3 -= 1
                    boucle -= 1
                    if(boucle3 == 0):
                        if(boucle == 0):
                            f.close()
                            break
                        else:
                            #On rollback pour faire une autre collection
                            compteur = 4
            """
        print()
        print("Les collections : ")
        for i in self.listeCollection:
            print(i.string())
        print()
        print("Les satellites : ")
        for i in self.listeSatellite:
            print(i.string())

    def fichierSortie(self):
        """
        Ecrit le fichier de sortie contenant:
            le nombre de photos prises
            pour chaque photo prise:
                latitude du point d'interet
                longitude du point d'interet
                tour de la prise de vue
                numero du satellite ayant pris la prise de vue

        .. todo: A faire
        """
        fichier = open("fichierSortie.txt", "w")
        for collect in self.listeCollection:
            if(collect.estVide()):
                fichier.write("Collection terminee")
            else:
                fichier.write("Collection non terminee")
            for  donnees in collect.listeCoordonneesReussies:
                fichier.write("Latitude : " + donnes[0] + ", Longitude : "+ donnes[1] + ", Tour : " + donnes[2] + ", Satelitte : " + donnes[3] + "\n")
        fichier.close()

    """
    Tri de listeCoordonneesTriees
    Les coordonnees sont triees par latitude croissante et, par longitude decroissante pour les coordonnees ayant la meme latitude
    """
    def trierListeCoordonneesTriees(self):
        #Tri par longitude decroissante
        self.listeCoordonneesTriees.sort(key=lambda x: x[1], reverse = True)
        #Puis tri par latitude croissante
        self.listeCoordonneesTriees.sort(key=lambda x: x[0])
        print("listeCoordonneesTriees", self.listeCoordonneesTriees)

    """
    def initialiserListePhotosPossibles(self):
        for satellite in self.listeSatellite:
            print(satellite.getPosition())
    """

	


    def validationCollection(self):
        """
        Validation de la collection

        :return: True si tous les points d'interet ont ete photographies
                False sinon
        :rtype: boolean

        .. todo: A faire
	utilite de la methode?
        """
        if len(self.listeCoordonneesTriees)==0:
            return True
        else:
            return False
    def lancerSimulation(self) :
        """
        Lancement de la simulation
        """

        print()
        print("Lancement de la simulation :")
        while self.temps.getTempsActuel() < self.temps.getTempsTotal():
            for s in self.listeSatellite:
                for c in self.listeCoordonneesTriees:
                    #Si la photo est sur la trajectoire du satellite
                    if s.photoPossible(c) == True:
                        print("Tour : ", self.temps.getTempsActuel()," Satellite : ",s.getNumero(), " Coordonnees pt d'interet: ",c)
                        '''
                            TODO: supprimer les coordonnees pouvant etre prise ne photo de listeCoordonnees
                                et les rajouter dans listeCoordonneesReussies
                        '''
                s.calculePosition()
            self.temps.incrementer()
        self.fichierSortie()

    def getListeSatellite(self):
        """
        Accesseur - Renvoie la liste des satellites

        :return: la liste des satellites (listeSatellite)
        :rtype: [Satellite]
        """

        return self.listeSatellite

    def getListeCollection(self):
        """
        Accesseur - Renvoie la liste des collections

        :return: la liste des collections (listeCollection)
        :rtype: [Collection]
        """

        return self.listeCollection

# initialisation d'un objet de type Lanceur
l1 = Lanceur("test.txt")
