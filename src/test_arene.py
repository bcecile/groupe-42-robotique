import unittest
from robot import *
from arene import *

class TestArene(unittest.TestCase) :
	def setUp(self) :
		self.a = Arene(5,5)
		self.r = Robot(0,0,0)

	def test_robot(self) :
		self.assertEqual(self.a.largeur,5)
		self.assertEqual(self.a.longueur,5)

	def test_construction(self) :
		self.a.construction()
		self.assertEqual(len(self.a.matrice),5)
		for i in range(self.a.largeur) :
			self.assertEqual(len(self.a.matrice[i]),5)

	def test_addRobot(self) :
		self.a.construction()
		self.a.addRobot(self.r)
		self.assertEqual(self.a.matrice[self.r.x][self.r.y],'r')

if __name__ == '__main__' :
	unittest.main()