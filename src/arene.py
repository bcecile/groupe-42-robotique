#!/usr/bin/python
# -*- coding: utf-8 -*-
from obstacle import *
from robot import *
class Arene:
    """L'arene est definit par sa longueur et sa largeur
    """
    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.matrice = [[0 for i in range(longueur)] for j in range(largeur)]
        self.obstacle = []

    def placerRobot(self,robot) :
        """ Place dans la matrice de l'arene le robot, représenté par un 1, et le passe en attribut
            :param robot: le robot à placer
        """
        self.matrice[robot.x][robot.y] = 1
        self.robot = robot

    def placerObstacle(self,obstacle):
        """ Place dans la matrice de l'arene un obstacle, représenté par un 2, et le rajoute dans la liste attribut.
            :param obstacle: l'obstacle à placer
        """
        self.obstacle.append(obstacle)
        for i in range(obstacle.taille) :
            for j in range(obstacle.taille) :
                if (self.matrice[obstacle.x+i][obstacle.y+j] != 0):
                    print("Erreur, la case est occupee \n")
                    return 
                else:
                    self.matrice[obstacle.x+i][obstacle.y+j] = 2