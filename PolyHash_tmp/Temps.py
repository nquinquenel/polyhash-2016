class Temps:

    # Constructeur de Temps
    #
    # @param tempsTotal Le temps total
    #
    def __init__(self, tempsTotal):
        # initialisation du temps à 0
        self.temps = 0
        self.tempsTotal = tempsTotal

    # Incrémentation du temps
    #
    def incrementer(self):
        self.temps += 1

    # Vérifie si le temps est supérieur (ou égal) au temps temps total
    #
    # @return True si temps >= tempsTotal
    #         False sinon
    #
    def tempsEcoule(self):
        ret = False
        if (self.temps >= self.tempsTotal):
            ret = True
        return ret
