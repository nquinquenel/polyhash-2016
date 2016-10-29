from Temps import Temps
from Collection import Collection
from Satellite import Satellite

class Lanceur:

    # Constructeur de Lanceur
    #
    # @param fichier Le fichier contenant les données d'entrée en caractères ASCII
    #
    def __init__(self,fichier):
        self.listeSatellite = []
        self.listeCollection = []
        self.score = 0
        self.temps = None
        self.nomFichier = fichier
        self.lectureFichier()

    # Lit le fichier et en extrait:
    #   le temps de la simulation
    #   le nombre de satellites
    #   les paramètres initiaux des satellites:
    #       latitude de départ
    #       longitude de départ
    #       vitesse de départ
    #       changement d'orientation max d'un tour à l'autre
    #       orientation max
    #   le nombre d'images dans la collection
    #   les points d'intérêt:
    #       score rapporté pour la prise d'un point d'intérêt
    #       latitude
    #       longitude
    #       intervals de prise de vue requis
    #
    def lectureFichier(self):
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
                #Découpage des satellites
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
                #Découpage de collections
                elif(compteur == 4):
                    value = ligne.split(" ")
                    print(value[0] + ": Score de la collection, " + value[1] + ": Nombre d'images, " + value[2] + ": Nombre de conditions")
                    boucle2 = int(value[1])
                    boucle3 = int(value[2])
                    collection = Collection(int(value[0]))
                    self.getListeCollection().append(collection)
                    compteur += 1
                #Répartition des coordonnées
                elif(compteur == 5):
                    liste = ligne.split(" ")
                    liste[0] = float(liste[0])
                    liste[1] = float(liste[1])
                    print(liste)
                    collection.getCoordonnees().append(liste)
                    boucle2 -= 1
                    if(boucle2 == 0):
                        compteur += 1
                    #Délais de temps
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

    # Ecrit le fichier de sortie contenant;
    #   le nombre de photos prises
    #   pour chaque photo prise:
    #       latitude du point d'intérêt
    #       longitude du point d'intérêt
    #       tour de la prise de vue
    #       numéro du satellite ayant pris la prise de vue
    #
    def fichierSortie(self):
        return 0

    # Validation de la collection
    #
    # @return True si tous les points d'intérêt ont été photographiés
    #         False sinon
    #
    def validationCollection(self):
        return True

    # Lancement de la simulation
    #
    def lancerSimulation(self) :
        return 0 #Pourquoi un return ?!

    # Accesseur - Renvoie la liste des satellites
    #
    # @return la liste des satellites (listeSatellite)
    #
    def getListeSatellite(self):
        return self.listeSatellite

    # Accesseur - Renvoie la liste des collections
    #
    # @return la liste des collections (listeCollection)
    #
    def getListeCollection(self):
        return self.listeCollection

# initialisation d'un objet de type Lanceur
l1 = Lanceur("test.txt")
