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

  def avancerRobot(self, distance, tab):
            # Si angle = 0, il avance vers la droite ( vue du dessus )
        if self.angle==0:
            tab[self.x][self.y]=0
            self.x=self.x+1
            tab[self.x][self.y]=1
        # Si angle = 90, il avance vers le haut
        elif self.angle==90:
            tab[self.x][self.y]=0
            self.y=self.y+1
            tab[self.x][self.y]=1
        # Si angle = 180, il avance vers la gauche
        elif self.angle==180:
            tab[self.x][self.y]=0
            self.x=self.x-1
            tab[self.x][self.y]=1
        # Si angle = 270, il avance vers le bas
        elif self.angle==270:
            tab[self.x][self.y]=0
            self.y=self.y-1
            tab[self.x][self.y]=1
            
#Test


