#!/usr/bin/python
# -*- coding: utf-8 -*-

class Arene:
    
    def __init__(self,longueur,largeur):
        self.longueur=longueur
        self.largeur=largeur
        self.matrice=[[]]
        
        
    def construction(self,longueur,largeur):
        tab=[]
        for i in range(longueur):
            tab.append([0] * largeur)
        return tab

#Test
#instanciation de la classe
Arene = Arene(5,5)
#Utilisation de la methode
bob = Arene.construction(Arene.longueur,Arene.largeur)
#Presentation du tableau 
print(bob)

