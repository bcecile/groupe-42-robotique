import unittest
from obstacle import *

class TestObstacle(unittest.TestCase) :
	def setUp(self) :
		self.r = Obstacle(0,0,0)

	def test_obstacle(self) :
		self.assertEqual(self.r.x,0)
		self.assertEqual(self.r.y,0)
		self.assertEqual(self.r.taille,0)


if __name__ == '__main__' :
	unittest.main()
