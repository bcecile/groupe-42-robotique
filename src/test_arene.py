import unittest
from robot import *
from arene import *
from obstacle import *

class TestArene(unittest.TestCase) :
	def setUp(self) :
		self.a = Arene(5,5)
		self.r = Robot(0,0,0)
		self.o = Obstacle(3,3,1)

	def test_arene(self) :
		self.assertEqual(self.a.largeur,5)
		self.assertEqual(self.a.longueur,5)
		self.assertEqual(len(self.a.matrice),5)
		for i in range(self.a.largeur) :
			self.assertEqual(len(self.a.matrice[i]),5)

	def test_placerRobot(self) :
		self.a.placerRobot(self.r)
		self.assertEqual(self.a.matrice[self.r.x][self.r.y],1)
		self.assertEqual(self.a.robot,self.r)

	def test_placerObstacle(self) :
		self.a.placerObstacle(self.o)
		self.assertEqual(self.a.matrice[self.o.x][self.o.y],2)
		self.assertEqual(self.o,self.a.obstacle[0])


if __name__ == '__main__' :
	unittest.main()