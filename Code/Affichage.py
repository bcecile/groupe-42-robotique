from Arene import *
from Robot import *
from Tkinter import *
class Vue:

    def __init__(self, master, arene) :
        self.master = master
        master.title("fenetre")
        master.resizable(0,0)
        self.arene=arene
        self.canvas=Canvas(master,width=100*arene.getLongueur(),height=100*arene.getLargeur())
        self.canvas.pack()
        self.img=[]
    
    def afficherArene(self) :
    	for e in range(arene.getLargeur()):
    		self.canvas
        self.afficherObjet(arene.robot)

    def afficherObjet(self,rob) :
    	print rob.getx()
        self.canvas.create_rectangle(100*(rob.getx()+1),100*(rob.gety()+1),100*rob.getx(),100*rob.gety(), fill="yellow")

robot = Robot(0,0,45)

arene = Arene(10,10)

arene.construction(arene.getLongueur(),arene.getLargeur())
arene.addRobot(robot)

fenetre = Tk()
vue = Vue(fenetre, arene)
vue.afficherArene()
fenetre.mainloop()