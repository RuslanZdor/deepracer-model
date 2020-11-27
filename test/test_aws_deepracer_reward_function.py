import unittest

import aws_deepracer_reward_function as rf

params = {
    "track_width": 10,
    "distance_from_center": 0,
    "speed": rf.MAX_SPEED,
    "heading": 0,
    "closest_waypoints": [0, 1],
    "waypoints": [[0, 0], [1, 0]],
    "steering_angle": 0,
    "all_wheels_on_track": True,
    "is_left_of_center": True,
    "progress": 0
}


class TestStringMethods(unittest.TestCase):

    def test_speed_dependency(self):
        slower_params = params.copy()
        faster_params = params.copy()
        faster_params["speed"] = 8

        self.assertTrue(rf.reward_function(slower_params)
                        < rf.reward_function(faster_params), 'Faster speed has to give more rewards')

    def test_negative_scenario(self):
        temp_params = params.copy()
        temp_params["distance_from_center"] = 11
        self.assertEqual(rf.MIN_REWARD, rf.reward_function(temp_params))

    def test_max_reward(self):
        temp_params = params.copy()
        self.assertEqual(1, rf.reward_function(temp_params))


if __name__ == '__main__':
    unittest.main()
