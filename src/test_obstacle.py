import unittest
from obstacle import *

class TestObstacle(unittest.TestCase) :
	def setUp(self) :
		self.o = Obstacle(0,0,0)

	def test_obstacle(self) :
		self.assertEqual(self.o.x,0)
		self.assertEqual(self.o.y,0)
		self.assertEqual(self.o.taille,0)


if __name__ == '__main__' :
	unittest.main()
