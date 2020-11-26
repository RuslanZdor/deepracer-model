import unittest

import aws_deepracer_reward_function as rf


class TestStringMethods(unittest.TestCase):

    def test_right(self):
        params = {
            "closest_waypoints": [0, 1],
            "waypoints": [[0, 0], [1, 0]]
        }
        self.assertEqual(0, rf.closest_waypoint_angle(params), 'only X movements to right has to return 0 degree')

    def test_top(self):
        params = {
            "closest_waypoints": [0, 1],
            "waypoints": [[0, 0], [0, 1]]
        }
        self.assertEqual(90, rf.closest_waypoint_angle(params), 'only Y movements to top has to return 90 degree')

    def test_left(self):
        params = {
            "closest_waypoints": [0, 1],
            "waypoints": [[0, 0], [-1, 0]]
        }
        self.assertEqual(180, rf.closest_waypoint_angle(params), 'only X movements to left has to return 180 degree')

    def test_bottom(self):
        params = {
            "closest_waypoints": [0, 1],
            "waypoints": [[0, 0], [0, -1]]
        }
        self.assertEqual(-90, rf.closest_waypoint_angle(params), 'only X movements to left has to return -90 degree')

    def test_middle(self):
        params = {
            "closest_waypoints": [0, 1],
            "waypoints": [[0, 0], [1, 1]]
        }
        self.assertEqual(45, rf.closest_waypoint_angle(params), 'only X movements to right and top has to return 45 '
                                                                'degree')


if __name__ == '__main__':
    unittest.main()
