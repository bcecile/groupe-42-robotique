from Arene import *
from Robot import *
from Tkinter import *
class Vue:

    def __init__(self, master, arene) :
        self.master = master
        master.title("fenetre")
        master.resizable(0,0)
        self.arene=arene
        self.canvas=Canvas(master,width=100*self.arene.getLongueur(),height=100*self.arene.getLargeur())
        self.canvas.pack()
        self.img=[]
    
    def afficherArene(self) :
        self.afficherObjet(self.arene.robot)

    def afficherObjet(self,rob) :
    	print rob.getx()
        self.canvas.create_rectangle(100*(rob.getx()+1),100*(rob.gety()+1),100*rob.getx(),100*rob.gety(), fill="yellow")
