from Temps import Temps
from Collection import Collection
from Satellite import Satellite
import copy
import math

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
                    images.append([int(j) for j in f.readline().strip('\n').split(" ")])
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
        print()
        print("Les collections : ")
        for i in self.listeCollection:
            print(i.string())
        print()
        print("Les satellites : ")
        for i in self.listeSatellite:
            print(i.string())
    """
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
                print("dans fichierSortie()")
                #fichier.write("Latitude : " + str(donnees[0]) + ", Longitude : "+ str(donnees[1]) + ", Tour : " + str(donnees[2]) + ", Satelitte : " + str(donnees[3]) + "\n")
        fichier.close()

    """
    Tri de listeCoordonneesTriees
    Les coordonnees sont triees par latitude croissante et, par longitude decroissante pour les coordonnees ayant la meme latitude
    """
    def trierListeCoordonneesTriees(self):
        #Tri par longitude decroissante
        self.listeCoordonneesTriees.sort(key=lambda x: x[1], reverse = True)
        #Puis tri par latitude croissante
        self.listeCoordonneesTriees.sort(key=lambda x:x[0])
        #print("listeCoordonneesTriees", self.listeCoordonneesTriees)

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

        tabPointsSat = []

        for sat in self.listeSatellite:
            polygone = sat.getPolygone(self.temps.getTempsTotal())
            p = 0
            aires = []
            while (p < len(polygone)):
                aire = (1/2)*abs(((polygone[p+0][0]*polygone[p+1][1])+(polygone[p+3][0]*polygone[p+0][1])-(polygone[p+1][0]*polygone[p+0][1])-(polygone[p+2][0]*polygone[p+1][1])-(polygone[p+3][0]*polygone[p+2][1])-(polygone[p+1][0]*polygone[p+2][1])+(polygone[p+2][0]*polygone[p+3][1])+(polygone[p+0][0]*polygone[p+3][1])))
                aires.append(aire)
                p = p + 4
            print(aires)
            for coord in self.listeCoordonneesTriees:
                i = 0
                aireCoord = 0
                while (i < len(polygone)):
                    v = 0
                    while (v < 3):
                        distA = math.sqrt((coord[0]-polygone[i+v][0])**2+(coord[1]-polygone[i+v][1])**2)
                        distB = math.sqrt((coord[0]-polygone[i+v+1][0])**2+(coord[1]-polygone[i+v+1][1])**2)
                        dist2Points = math.sqrt((polygone[i+v+1][0]-polygone[i+v][0])**2+(polygone[i+v][1]-polygone[i+v+1][1])**2)
                        aireCoord += (1/4)*math.sqrt((distA+dist2Points+distB)*(-distA+dist2Points+distB)*(distA-dist2Points+distB)*(distA+dist2Points-distB))
                        v = v + 1
                    distA = math.sqrt((coord[0]-polygone[i][0])**2+(coord[1]-polygone[i][1])**2)
                    distB = math.sqrt((coord[0]-polygone[i+3][0])**2+(coord[1]-polygone[i+3][1])**2)
                    aireCoord += math.sqrt((polygone[i+3][0]-polygone[i][0])**2+(polygone[i+3][1]-polygone[i][1])**2)
                    
                    for ai in aires:
                        print(ai)
                        print(aireCoord)
                        print()
                    i = i + 4

        """
        tabPointsSat = [[]]*len(self.listeSatellite)
        tabPointsSatFinal = [[]]*len(self.listeSatellite)
        satClone = copy.deepcopy(self.listeSatellite)

        #Rempli un tableau avec toutes les coordonnees que les satellites peuvent avoir
        while self.temps.getTempsActuel() < self.temps.getTempsTotal():
            for coord in self.listeCoordonneesTriees:
                for cmpt in range(0, len(self.listeSatellite)):
                    if satClone[cmpt].photoPossible(coord) and coord not in tabPointsSat[cmpt]:
                        tabPointsSat[satClone[cmpt].getNumero()].append(coord)
            for s in satClone:
                s.calculePosition()
            self.temps.incrementer()

        print("Part 1 done")

        #Clone les tableaux
        for it in range(0, len(tabPointsSat)):
            tabPointsSat[0] = copy.copy(tabPointsSat[0])
            tabPointsSatFinal[0] = copy.copy(tabPointsSatFinal[0])

        print("Part 2 done")

        #Donne des chemins uniques aux satellites
        if len(tabPointsSat) > 1:
            for a in range(0, len(tabPointsSat)):
                if tabPointsSat[a]:
                    for b in range(0, len(tabPointsSat)):
                        if a != b:
                            if tabPointsSat[a][0] in tabPointsSat[b]:
                                tabPointsSat[b].remove(tabPointsSat[a][0])
                    tabPointsSatFinal[a].append(tabPointsSat[a][0])
                    del tabPointsSat[a][0]
        else:
            tabPointsSatFinal = tabPointsSat

        print("Part 3 done")
        """
        """
        for sat in self.listeSatellite:
            lati, longi = sat.getPosition()
            trier = False
            while not trier:
                if len(tabPointsSatFinal[sat.getNumero()]) > 1:
                    if tabPointsSatFinal[sat.getNumero()][len(tabPointsSatFinal)][1] >= lati:
                        if tabPointsSatFinal[sat.getNumero()][0][0] < lati:
                            tabPointsSatFinal[sat.getNumero()].append(tabPointsSatFinal[sat.getNumero()][0])
                            del tabPointsSatFinal[sat.getNumero()][0]
                        else:
                            trier = True
                    else:
                        trier = True
                else:
                    trier = True
        """
        """
        self.temps.resetTemps()

        print("Part 4 done")

        print(tabPointsSatFinal)

        print("Total avant : ", len(tabPointsSatFinal[0]))

        while self.temps.getTempsActuel() < self.temps.getTempsTotal() and tabPointsSatFinal:
            for s in self.listeSatellite:
                if tabPointsSatFinal[s.getNumero()]:
                    s.changerOrientation(tabPointsSatFinal[s.getNumero()][0])
                    if s.photoPossible(tabPointsSatFinal[s.getNumero()][0]) == True:
                        print("Tour : ", self.temps.getTempsActuel()," Satellite : ",s.getNumero(), " Coordonnees pt d'interet: ",tabPointsSatFinal[s.getNumero()][0])
                        del tabPointsSatFinal[s.getNumero()][0]                    
                s.calculePosition()
            self.temps.incrementer()

        print("Total : ", len(tabPointsSatFinal[0]))
        """  
        """
            #Test si les photos peuvent etre prises
            #Pour chaque collection
            for c in self.listeCollection:
                #Pour chaque coordonnees non prises en photo
                for coord in c.getCoordonnees():
                    #Pour chaque satellite
                    for s in self.listeSatellite:
                        #Si la photo est sur la trajectoire du satellite
                        :
                            #On supprime les coordonnees de la photo prise de toutes les collections
                            for c2 in self.listeCollection:
                                c2.suppressionElement(coord)
                            print("Tour : ", self.temps.getTempsActuel()," Satellite : ",s.getNumero(), " Coordonnees pt d'interet: ",coord)
                            c.suppressionElement(coord)
            #MAJ de la position des satellites
            for s in self.listeSatellite:
                s.calculePosition()
            #Passage au tour suivant
            self.temps.incrementer()
        self.fichierSortie()
        """
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
