#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Module de prise en charge des entrées/sorties, notamment pour
    la production et la consommation de fichiers ASCII.
    Usage:

    >>> from polyhash import say_hello
    >>> say_hello("World")
"""

__all__ = ['say_hello']  # ajouter dans cette liste tous les symboles 'importables'


def say_hello(entity):
    """
        Fonction de politesse.

        :param entity: Le truc à qui on dit bonjour
        :type entity: string
        :return: Rien, parce que c'est uniquement pour l'exemple
        :rtype: None
    """
    print("Hello {}!".format(entity))


if __name__ == "__main__":
    say_hello("World")
