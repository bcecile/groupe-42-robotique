#!/usr/bin/python
# -*- coding: utf-8 -*-

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

P=Point(0,1)
print(P.getX())
print(P.getY())

#Test : Affichage
#0
#1
