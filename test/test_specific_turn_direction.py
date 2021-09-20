import unittest

import aws_deepracer_reward_function as rf


class TestStringMethods(unittest.TestCase):

    def test_let_turn(self):
        params = {
            "steering_angle": 1,
            "closest_waypoints": [0, 1]
        }
        self.assertEqual(1, rf.specific_turn_direction(params), 'left turn is ok')

    def test_right_turn(self):
        params = {
            "steering_angle": -1,
            "closest_waypoints": [0, 1]
        }
        self.assertEqual(0, rf.specific_turn_direction(params), 'right turn has to be punished')


if __name__ == '__main__':
    unittest.main()
