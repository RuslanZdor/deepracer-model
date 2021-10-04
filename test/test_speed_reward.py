import unittest

import aws_deepracer_reward_function as rf


class TestStringMethods(unittest.TestCase):

    def test_max_speed_green(self):
        self.set_speed_track()
        params = {
            "speed": rf.MAX_SPEED,
            "closest_waypoints": [0, 1],
        }
        self.assertEqual(1, rf.speed_reward(params), 'max speed should return max value')

    # def test_max_speed_orange(self):
    #     self.set_speed_track()
    #     params = {
    #         "speed": rf.MAX_SPEED,
    #         "closest_waypoints": [21, 22],
    #     }
    #     self.assertEqual(rf.ORANGE_SPEED, rf.speed_reward(params), 'max speed should return max value')

    # def test_max_speed_red(self):
    #     self.set_speed_track()
    #     rf.SPEED_TRACK[1] = "red"
    #     rf.SPEED_TRACK[2] = "red"
    #     params = {
    #         "speed": rf.MAX_SPEED,
    #         "closest_waypoints": [1, 2],
    #     }
    #     self.assertEqual(rf.RED_SPEED, rf.speed_reward(params), 'max speed should return max value')

    def test_zero_speed_green(self):
        self.set_speed_track()
        params = {
            "speed": 0,
            "closest_waypoints": [0, 1],
        }
        self.assertEqual(0, rf.speed_reward(params), 'zero speed should return zero value')

    def test_zero_speed_orange(self):
        self.set_speed_track()
        params = {
            "speed": 0,
            "closest_waypoints": [21, 22],
        }
        self.assertAlmostEqual(0.0, rf.speed_reward(params), delta=0.01, msg='zero speed should return zero value')

    def test_zero_speed_red(self):
        self.set_speed_track()
        params = {
            "speed": 0,
            "closest_waypoints": [255, 256],
        }
        self.assertEqual(0.0, rf.speed_reward(params), 'zero speed should return zero value')

    @staticmethod
    def set_speed_track():
        rf.SPEED_TRACK = {}
        for i in range(0, 10):
            rf.SPEED_TRACK[i] = rf.GREEN
        for i in range(20, 45):
            rf.SPEED_TRACK[i] = rf.ORANGE
        for i in range(53, 70):
            rf.SPEED_TRACK[i] = rf.ORANGE
        for i in range(70, 85):
            rf.SPEED_TRACK[i] = rf.GREEN
        for i in range(85, 91):
            rf.SPEED_TRACK[i] = rf.ORANGE
        for i in range(91, 120):
            rf.SPEED_TRACK[i] = rf.GREEN
        for i in range(175, 195):
            rf.SPEED_TRACK[i] = rf.ORANGE
        for i in range(195, 205):
            rf.SPEED_TRACK[i] = rf.ORANGE
        for i in range(205, 224):
            rf.SPEED_TRACK[i] = rf.GREEN


if __name__ == '__main__':
    unittest.main()
