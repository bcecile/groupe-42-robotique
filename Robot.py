#!/usr/bin/python
# -*- coding: utf-8 -*-

class Robot:
  # Constructeur
  def __init__(self,x,y,angle):
      self.x=x
      self.y=y
      # angle dans le sens trigonometrique
      self.angle=angle

  #Methode get()
  def getx(self):
      return self.x

  def gety(self):
      return self.y

  def getangle(self):
      return self.angle

  def direction(self):
    if self.angle==0:
      return "bas"
    elif self.angle==180:
      return "droite"
    elif self.angle==270:
      return "haut"
    elif self.angle==90:
      return "gauche"

  def avancerRobot(self, distance, tab):
    # Si angle = 180, il avance vers la droite ( vue du dessus )
    if (self.direction()=="droite"):
      tab[self.y][self.x]=0
      self.x=self.x+distance
      tab[self.y][self.x]=1
    # Si angle =270 , il avance vers le haut
    elif (self.direction()=="haut"):
      tab[self.y][self.x]=0
      self.y=self.y+distance
      tab[self.y][self.x]=1
    # Si angle = 90, il avance vers la gauche
    elif (self.direction()=="gauche"):
      tab[self.y][self.x]=0
      self.x=self.x-distance
      tab[self.y][self.x]=1
    # Si angle =0 , il avance vers le bas
    elif (self.direction()=="bas"):
      tab[self.y][self.x]=0
      self.y=self.y-distance
      tab[self.y][self.x]=1

  def collision(self, distance, tab):
    i=1
    j=1
    if (self.direction()=="droite"):
      for j in range(distance+1):
        if (tab[self.y][self.x+j]==2):
          return True
        
    elif (self.direction()=="haut"):
      for i in range(distance+1):
        if (tab[self.y+i][self.x]==2):
          return True
        
    elif (self.direction()=="gauche"):
      for j in range(distance+1):
        if (tab[self.y][self.x-i]==2):
          return True
        
    elif (self.direction()=="bas"):     
      for i in range(distance+1):
        if (tab[self.y-j][self.x]==2):
          return True
    return False
  
#Test

robot = Robot(0,0,0)
