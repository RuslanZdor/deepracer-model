import unittest

import aws_deepracer_reward_function as rf


class TestStringMethods(unittest.TestCase):

    def test_zero_steering(self):
        params = {
            "steering_angle": 0,
            "closest_waypoints": [0, 1]
        }
        self.assertEqual(1, rf.steering_reward(params), 'small steering should return max value')

    def test_threshold_steering_green(self):
        params = {
            "steering_angle": rf.GREEN_STEERING_THRESHOLD,
            "closest_waypoints": [0, 1],
        }
        self.assertEqual(1, rf.steering_reward(params), 'small steering should return max value')

    def test_over_steering_threshold_green(self):
        params = {
            "steering_angle": 45,
            "closest_waypoints": [0, 1],
        }
        self.assertEqual(0.8, rf.steering_reward(params), 'punish over reach steering threshold')


if __name__ == '__main__':
    unittest.main()
