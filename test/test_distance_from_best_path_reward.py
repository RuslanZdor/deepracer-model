import unittest

import aws_deepracer_reward_function as rf


class TestDistanceFromBestPathReward(unittest.TestCase):

    rf.BEST_PATH = {0: [1, 1], 1: [2, 2]}

    def test_on_track(self):
        print("test_on_track")
        params = {
            "all_wheels_on_track": True,
            "closest_waypoints": [0, 1],
            "track_width": 1,
            "waypoints": [[0, 0], [1, 0]],
            "distance_from_center": 0.2,
            "x": 0.5,
            "y": 2,
        }
        self.assertEqual(1, rf.distance_from_best_path_reward(params), 'if car is on track then return max value')

    def test_of_track(self):
        print("test_of_track")
        params = {
            "all_wheels_on_track": True,
            "closest_waypoints": [0, 1],
            "track_width": 1,
            "waypoints": [[0, 0], [1, 0]],
            "distance_from_center": 0.2,
            "x": 0,
            "y": 0,
        }
        self.assertAlmostEqual(0.3, rf.distance_from_best_path_reward(params), msg='of car is out of track return less rewards', delta=0.1)


if __name__ == '__main__':
    unittest.main()
