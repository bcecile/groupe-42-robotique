from vue import *
from arene import *
from robot import *

robot = Robot(4,4,45)
print'Je suis un robot en' , robot.x, robot.y, 'avec un angle de', robot.angle

arene = Arene(5,5)
print 'Je suis une matrice de largeur :', arene.largeur, 'et de longueur :', arene.longueur
print arene.matrice
arene.placerRobot(robot)
print arene.matrice


fenetre = Tk()
vue = Vue(fenetre, arene)
vue.afficherArene()
fenetre.mainloop()