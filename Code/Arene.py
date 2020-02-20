#!/usr/bin/python
# -*- coding: utf-8 -*-
from Robot import *
class Arene:

    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.matrice = []
        

    def construction(self):
        """Initialise la matrice de l'arene"""
        for i in range(self.longueur):
            self.matrice.append([0] * (self.largeur))
    
    def getLongueur(self):
        return self.longueur
        
    def getLargeur(self):
        return self.largeur

    def addRobot(self,robot) :
        """ Place dans la matrice de l'arene le robot et le passe en attribut
            :param robot: le robot à placer
        """
        self.matrice[robot.getx()][robot.gety()]="r"
        self.robot=robot


