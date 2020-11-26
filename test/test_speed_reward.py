import unittest

import aws_deepracer_reward_function as rf


class TestStringMethods(unittest.TestCase):

    def test_max_speed(self):
        params = {
            "speed": rf.MAX_SPEED,
        }
        self.assertEqual(1, rf.speed_reward(params), 'max speed should return max value')

    def test_zero_speed(self):
        params = {
            "speed": 0,
        }
        self.assertEqual(0, rf.speed_reward(params), 'zero speed should return zero value')


if __name__ == '__main__':
    unittest.main()
