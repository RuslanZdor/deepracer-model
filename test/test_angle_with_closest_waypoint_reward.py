import unittest
from unittest.mock import Mock, patch

import aws_deepracer_reward_function as rf


class TestStringMethods(unittest.TestCase):

    def test_same_direction(self):
        params = {
            "heading": 0,
            "is_left_of_center": True
        }
        with patch('aws_deepracer_reward_function.closest_waypoint_angle') as mock_closest_waypoint_angle:
            mock_closest_waypoint_angle.return_value = 0
            self.assertEqual(1, rf.angle_with_closest_waypoint_reward(params),
                             "When car heading track direction - give max reward")

    def test_wrong_direction(self):
        params = {
            "heading": 90,
            "is_left_of_center": True
        }
        with patch('aws_deepracer_reward_function.closest_waypoint_angle') as mock_closest_waypoint_angle:
            mock_closest_waypoint_angle.return_value = 0
            self.assertEqual(0.5, rf.angle_with_closest_waypoint_reward(params),
                             'When car heading track wrong direction - give zero reward')

    def test_middle_direction(self):
        params = {
            "heading": 45,
            "is_left_of_center": True
        }
        with patch('aws_deepracer_reward_function.closest_waypoint_angle') as mock_closest_waypoint_angle:
            mock_closest_waypoint_angle.return_value = 0
            self.assertEqual(0.75, rf.angle_with_closest_waypoint_reward(params),
                             'When car heading track wrong direction - give small reward')

    def test_left_side_correction(self):
        params = {
            "heading": -rf.ALLOWED_CORRECTION_ANGLE,
            "is_left_of_center": True
        }
        with patch('aws_deepracer_reward_function.closest_waypoint_angle') as mock_closest_waypoint_angle:
            mock_closest_waypoint_angle.return_value = 0
            self.assertEqual(1, rf.angle_with_closest_waypoint_reward(params),
                             'When car on left size heading track direction - give max reward')

    def test_right_side_correction(self):
        params = {
            "heading": rf.ALLOWED_CORRECTION_ANGLE,
            "is_left_of_center": False
        }
        with patch('aws_deepracer_reward_function.closest_waypoint_angle') as mock_closest_waypoint_angle:
            mock_closest_waypoint_angle.return_value = 0
            self.assertEqual(1, rf.angle_with_closest_waypoint_reward(params),
                             'When car on right size heading track direction - give max reward')


if __name__ == '__main__':
    unittest.main()
