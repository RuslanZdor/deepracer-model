import unittest

import aws_deepracer_reward_function as rf


class TestSSpeedColor(unittest.TestCase):

    def test_green(self):
        params = {
            "closest_waypoints": [0, 1],
        }
        self.assertEqual("green", rf.speed_color(params), 'expect green color')

    def test_orange(self):
        params = {
            "closest_waypoints": [20, 21],
        }
        self.assertEqual("orange", rf.speed_color(params), 'expect orange color')

    def test_red(self):
        params = {
            "closest_waypoints": [224, 225],
        }
        self.assertEqual("red", rf.speed_color(params), 'if index is our of SPEED_TRACK - return red color')


if __name__ == '__main__':
    unittest.main()
