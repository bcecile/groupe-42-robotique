import unittest
from robot import *

class TestRobot(unittest.TestCase) :
	def setUp(self) :
		self.r1 = Robot(0,0,0,0)
		self.r2 = Robot(2,0,90,0)
		self.r3 = Robot(3,0,180,0)
		self.r4 = Robot(4,2,270,0)
		self.tab = [[0 for i in range(5)] for j in range(5)]

	def test_robot(self) :
		self.assertEqual(self.r1.x,0)
		self.assertEqual(self.r1.y,0)
		self.assertEqual(self.r1.angle,0)
		self.assertEqual(self.r1.xreel,0)
		self.assertEqual(self.r1.yreel,0) 

	def test_direction(self) :
		self.assertEqual(self.r1.direction(),'bas')
		self.assertEqual(self.r2.direction(),'gauche')
		self.assertEqual(self.r3.direction(),'droite')
		self.assertEqual(self.r4.direction(),'haut')

	def test_avancerRobot(self) :
		self.r1.avancerRobot(1,self.tab)
		self.assertEqual(self.tab[1][0],1)
		self.r2.avancerRobot(1,self.tab)
		self.assertEqual(self.tab[0][1],1)
		self.r3.avancerRobot(1,self.tab)
		self.assertEqual(self.tab[0][4],1)
		self.r4.avancerRobot(1,self.tab)
		self.assertEqual(self.tab[1][4],1)

	def test_collision(self) :
		self.assertFalse(self.r3.collision(1,self.tab))



if __name__ == '__main__' :
	unittest.main()
