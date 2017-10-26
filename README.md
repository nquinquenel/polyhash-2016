Projet Poly
===========

Le projet Polyhash consiste à programmer la planification du travail d'un ensemble de satellites à l'aide d'une liste
de points d'intérêt à photographier, de sorte à maximiser le nombre d'images satellite réalisées dans un temps donné.

Equipe et répartition des tâches(non exhaustive) :


-QUINQUENEL Nicolas:

    -Gestion de la classe Satellite
        -Changement d'orientation
        -Calcul de la trajectoire
        -Gestion des attributs du satellite (orientation, delta, pointage etc.)
        -Prendre une photo
        -Déterminer les photos possibles à prendre actuellement sous le satellite
    -Création de la première version du programme principal
    -Aide au développement de la lecture du fichier
    -Aide à la documentation


-SOYER Mathieu:

    -Documentation DocString
    -Gestion des intervalles de temps pour la prise d'une photo
    -Gestion apres prise photo d'un point d'interet
        -Mettre a jour les collections contenant ce point
        -Mettre a jour les chemins des satellites contenant un point valide pour toutes les collections en prenant en compte leur(s) intervalle(s) requis


-EHRESMANN Nicolas:

    -Interface Graphique
    -Aide à la documentation

-OUTHIER Arthur:

    -Entrées/Sorties
    -Conception et analyse du projet (diagramme de classe)
    -Gestion de la classe Temps
