#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        return tab
    
    def getLongueur(self):
        return self.longueur
        
    def getLargeur(self):
        return self.largeur
        

#Test
#instanciation de la classe
Arene = Arene(5,5)
#Utilisation de la methode
bob = Arene.construction(Arene.longueur,Arene.largeur)
#Presentation du tableau 
print(bob)

