import unittest
from robot import *

class TestRobot(unittest.TestCase) :
	def setUp(self) :
		self.r = Robot(0,0,0)

	def test_robot(self) :
		self.assertEqual(self.r.x,0)
		self.assertEqual(self.r.y,0)
		self.assertEqual(self.r.angle,0)

if __name__ == '__main__' :
	unittest.main()