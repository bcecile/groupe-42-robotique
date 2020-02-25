#!/usr/bin/python
# -*- coding: utf-8 -*-
from Robot import *
class Arene:
    
    def __init__(self,longueur,largeur,robot):
        self.longueur=longueur
        self.largeur=largeur
        self.matrice=[[]]
        self.robot=robot
        
        
    def construction(self,longueur,largeur):
        tab=[]
        for i in range(longueur):
            tab.append([0] * largeur)
        self.matrice=tab
        return self.matrice
    
    def getLongueur(self):
        return self.longueur
        
    def getLargeur(self):
        return self.largeur

    def placerRobot(self):
        x=self.robot.getx()
        y=self.robot.gety()
        self.matrice[x][y]=1
        

#Test
#instanciation de la classe
robot = Robot(1,1,0)
Arene = Arene(5,5,robot)
#Utilisation de la methode
bob = Arene.construction(Arene.longueur,Arene.largeur)
#Presentation du tableau 
print(bob)
#On place le Robot dans l'Arene
Arene.placerRobot()
#Nouvelle representation du tableau
print(bob)
#On fait avancer le Robot
robot.avancerRobot(2,bob)
#Resultat du deplacement
print(bob)

