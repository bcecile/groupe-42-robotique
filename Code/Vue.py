from tkinter import * 
class Vue:

    def __init__(self, master,arene){
        self.master = master
        master.title("fenetre")
        self.arene=arene
        self.canvas=Canvas(master,width=100*arene.getLongueur(),height=100*arene.getLargeur)
        canvas.pack
    }
    
    def afficherArene(self){
        for e in arene.robot{
            afficherRobot(e)
        }
        
    }
    def afficherRobot(self,robot){
        robot=canvas.create_rectangle(100*getPosx(),100*getPosy(),100*(getPosx()-1),100*(getPosy()-1))
        self.robot=robot
    }
    
