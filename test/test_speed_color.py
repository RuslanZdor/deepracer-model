import unittest

import aws_deepracer_reward_function as rf


class TestSSpeedColor(unittest.TestCase):

    def test_green(self):
        self.set_speed_track()
        params = {
            "closest_waypoints": [0, 1],
        }
        self.assertEqual("green", rf.speed_color(params), 'expect green color')

    def test_orange(self):
        self.set_speed_track()
        params = {
            "closest_waypoints": [20, 21],
        }
        self.assertEqual("orange", rf.speed_color(params), 'expect orange color')

    def test_red(self):
        self.set_speed_track()
        params = {
            "closest_waypoints": [224, 225],
        }
        self.assertEqual("red", rf.speed_color(params), 'if index is our of SPEED_TRACK - return red color')

    def set_speed_track(self):
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
