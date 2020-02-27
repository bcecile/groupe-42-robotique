class Robot:
	"""Le robot est definit par des coordonnees x, y et un angle en degres
	"""
	def __init__(self,x,y,angle):
		self.x = x
		self.y = y
		# angle dans le sens trigonometrique
		self.angle = angle

	def getx(self):
		return self.x
	
	def gety(self):
		return self.y

	def getangle(self):
		return self.angle