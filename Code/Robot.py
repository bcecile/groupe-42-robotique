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

#Test
robot = Robot(0,3,45)
print'Je suis un robot en' , robot.getx(),robot.gety()
