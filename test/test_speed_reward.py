import unittest

import aws_deepracer_reward_function as rf


class TestStringMethods(unittest.TestCase):

    def test_max_speed_green(self):
        params = {
            "speed": rf.MAX_SPEED,
            "closest_waypoints": [0, 1],
        }
        self.assertEqual(1, rf.speed_reward(params), 'max speed should return max value')

    def test_max_speed_orange(self):
        params = {
            "speed": rf.MAX_SPEED,
            "closest_waypoints": [21, 22],
        }
        self.assertEqual(0.7, rf.speed_reward(params), 'max speed should return max value')

    def test_max_speed_red(self):
        params = {
            "speed": rf.MAX_SPEED,
            "closest_waypoints": [255, 256],
        }
        self.assertEqual(0.4, rf.speed_reward(params), 'max speed should return max value')

    def test_zero_speed_green(self):
        params = {
            "speed": 0,
            "closest_waypoints": [0, 1],
        }
        self.assertEqual(0, rf.speed_reward(params), 'zero speed should return zero value')

    def test_zero_speed_orange(self):
        params = {
            "speed": 0,
            "closest_waypoints": [21, 22],
        }
        self.assertAlmostEqual(0.3, rf.speed_reward(params), delta=0.01, msg='zero speed should return zero value')

    def test_zero_speed_red(self):
        params = {
            "speed": 0,
            "closest_waypoints": [255, 256],
        }
        self.assertEqual(0.6, rf.speed_reward(params), 'zero speed should return zero value')

if __name__ == '__main__':
    unittest.main()
