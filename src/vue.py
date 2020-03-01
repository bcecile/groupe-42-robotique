# -*- coding: utf-8 -*-
from arene import *
from robot import *
from Tkinter import *
class Vue:
    """ Initialise un canvas pour dessiner le Robot selon ses coordonnes.
        :master : 
        :arene : arene contenant un robot
    """
    def __init__(self, master, arene) :
        self.master = master
        master.title("fenetre")
        master.resizable(0,0)
        self.arene = arene
        self.canvas = Canvas(master,width=100*self.arene.longueur,height=100*self.arene.largeur)
        self.canvas.pack()
    
    def afficherArene(self) :
        """Affiche un robot s'il est present dans arene
        """
        if hasattr(self.arene, 'robot') :
            self.afficherObjet(self.arene.robot)

    def afficherObjet(self,rob) :
        """ Dessine sur le canvas de vue une representation du robot
            param rob: le robot à dessiner
        """
        self.robot = self.canvas.create_rectangle(100*(rob.x+1),100*(rob.y+1),100*rob.x,100*rob.y, fill="yellow")
