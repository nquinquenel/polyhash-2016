class Temps:
    """
    Cette classe s occupe de gerer le temps (les tours) lors de la simulation
    """

    def __init__(self, tempsTotal):
        """
        Constructeur de Temps
        :param tempsTotal: Le temps total
        """

        # initialisation du temps a 0
        self.temps = 0
        self.tempsTotal = tempsTotal

    def incrementer(self):
        """
        Incrementation du temps
        """

        self.temps += 1

    def tempsEcoule(self):
        """
        Verifie si le temps est superieur (ou egal) au temps temps total
        :return: True si temps >= tempsTotal
                False sinon
        """

        ret = False
        if (self.temps >= self.tempsTotal):
            ret = True
        return ret
