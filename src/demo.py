from vue import *
from arene import *
from robot import *

robot = Robot(4,4,45)
print'Je suis un robot en' , robot.getx(), robot.gety(), 'avec un angle de', robot.getangle()

arene = Arene(5,5)
arene.construction()
print 'Je suis une matrice de largeur :', arene.getLargeur(), 'et de longueur :', arene.getLongueur() 
print arene.matrice
arene.addRobot(robot)
print arene.matrice


fenetre = Tk()
vue = Vue(fenetre, arene)
vue.afficherArene()
fenetre.mainloop()