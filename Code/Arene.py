#!/usr/bin/python
# -*- coding: utf-8 -*-
from Robot import *
class Arene:

    def __init__(self,longueur,largeur):
        self.longueur=longueur
        self.largeur=largeur
        self.matrice=[]
        

    def construction(self,longueur,largeur):
        for i in range(self.longueur-1):
            self.matrice.append([0] * (self.largeur+1))
    
    def getLongueur(self):
        return self.longueur
        
    def getLargeur(self):
        return self.largeur

    def addRobot(self,robot) :
        self.matrice[robot.getx()][robot.gety()]="r"
        self.robot=robot

#Test
#instanciation de la classe
#Arene = Arene(5,5)
#Utilisation de la methode
#bob = Arene.construction(Arene.longueur,Arene.largeur)
#Presentation du tableau 
#print(bob)

