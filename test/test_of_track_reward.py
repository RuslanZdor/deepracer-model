import unittest

import aws_deepracer_reward_function as rf


class TestStringMethods(unittest.TestCase):

    def test_on_track(self):
        params = {
            "all_wheels_on_track": True,
        }
        self.assertEqual(1, rf.of_track_reward(params), 'if car is on track then return max value')

    def test_of_track(self):
        params = {
            "all_wheels_on_track": False,
        }
        self.assertEqual(0, rf.of_track_reward(params), 'of car is out of track return zero')


if __name__ == '__main__':
    unittest.main()
