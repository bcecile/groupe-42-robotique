#!/usr/bin/python
# -*- coding: utf-8 -*-
from Obstacle import *
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

    # Une case 1 représente un robot
    def placerRobot(self):
        x=self.robot.getx()
        y=self.robot.gety()
        self.matrice[x][y]=1
        
    # Une case 2 représente un obstacle
    def placerObstacle(self,x,y,taille):
        j=0 #int
        i=0 # int
        for i in range(taille):
            for j in range(taille):
                if ((self.matrice[x+i][y+j]==1)or(self.matrice[x+i][y+j]==2)):
                    print("Erreur, la case est occupee \n")
                    return 
                else:
                    self.matrice[x+i][y+j]=2

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

#Placer Obstacle

obstacle = Obstacle(2,3,2)
Arene.placerObstacle(obstacle.getx(),obstacle.gety(),obstacle.gettaille())
print(bob)

obstacle2 = Obstacle(1,1,1)
Arene.placerObstacle(obstacle2.getx(),obstacle2.gety(),obstacle2.gettaille())

#On fait avancer le Robot

#robot.avancerRobot(2,bob)

#Resultat du deplacement

#print(bob)

