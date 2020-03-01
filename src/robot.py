#!/usr/bin/python
# -*- coding: utf-8 -*-

class Robot:
  """Le robot est definit par des coordonnees x, y et un angle en degres
  """
  def __init__(self,x,y,angle):
      self.x=x
      self.y=y
      self.angle=angle

  def direction(self):
    """Retourne la direction du robot selon son angle
    """
    if self.angle==0:
      return "bas"
    elif self.angle==90:
      return "gauche"
    elif self.angle==180:
      return "droite"
    elif self.angle==270:
      return "haut"


  def avancerRobot(self, distance, tab):
    """Fait avancer le robot selon sa direction
       Si angle = 0 , il avance vers le bas
       Si angle = 90, il avance vers la gauche
       Si angle = 180, il avance vers la droite
       Si angle = 270 , il avance vers le haut
       :param distance : le nombre de case que le robot doit parcourir
       :param tab : la matrice où le robot se deplace
    """
    if (self.direction() == "droite"):
      tab[self.y][self.x] = 0
      self.x = self.x+distance
      tab[self.y][self.x] = 1

    elif (self.direction() == "haut"):
      tab[self.y][self.x] = 0
      self.y = self.y-distance
      tab[self.y][self.x] = 1

    elif (self.direction() == "gauche"):
      tab[self.y][self.x] = 0
      self.x = self.x-distance
      tab[self.y][self.x] = 1

    elif (self.direction() == "bas"):
      tab[self.y][self.x] = 0
      self.y = self.y+distance
      tab[self.y][self.x] = 1

  def collision(self, distance, tab):
    """Retourne s'il y a une collision, si une des cases devant le robot est occupée
       :param distance : la distance que le robot doit parcourir
       :param tab : la matrice où le robot se deplace
    """
    if (self.direction() == "droite"):
      for j in range(distance+1):
        if (tab[self.y][self.x+j] == 2):
          return True
        
    elif (self.direction() == "haut"):
      for i in range(distance+1):
        if (tab[self.y+i][self.x] == 2):
          return True
        
    elif (self.direction() == "gauche"):
      for j in range(distance+1):
        if (tab[self.y][self.x-i] == 2):
          return True
        
    elif (self.direction() == "bas"):     
      for i in range(distance+1):
        if (tab[self.y-j][self.x] == 2):
          return True
    return False
  