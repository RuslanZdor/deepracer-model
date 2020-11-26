import unittest

import aws_deepracer_reward_function as rf


class TestStringMethods(unittest.TestCase):

    def test_zero_steering(self):
        params = {
            "steering_angle": 0,
        }
        self.assertEqual(1, rf.steering_reward(params), 'small steering should return max value')

    def test_threshold_steering(self):
        params = {
            "steering_angle": rf.STEERING_THRESHOLD,
        }
        self.assertEqual(1, rf.steering_reward(params), 'small steering should return max value')

    def test_over_steering_threshold(self):
        params = {
            "steering_angle": 45,
        }
        self.assertEqual(0.75, rf.steering_reward(params), 'punish over reach steering threshold')


if __name__ == '__main__':
    unittest.main()
