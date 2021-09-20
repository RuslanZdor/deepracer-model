# define constants for function
import math

# in case of negative reward - use thin min value
MIN_REWARD = 1e-3

# max speed for racer
MAX_SPEED = 2

# max possible reward for aws function
MAX_REWARD = 1

# angle for not punishing for line correction
ALLOWED_CORRECTION_ANGLE = 10

# angle for not punishing for line correction
STEERING_THRESHOLD = 20
GREEN_STEERING_THRESHOLD = 10

# speed color (green is max speed, orange is middle, red for slow parts
SPEED_TRACK = {0: 'green', 1: 'green', 2: 'green', 3: 'green', 4: 'green', 5: 'green', 6: 'green', 7: 'green', 8: 'green', 9: 'green', 10: 'green', 11: 'green', 12: 'green', 13: 'green', 14: 'green', 15: 'green', 16: 'green', 17: 'green', 18: 'green', 19: 'green', 20: 'green', 21: 'green', 22: 'green', 23: 'green', 24: 'green', 25: 'green', 26: 'green', 27: 'green', 28: 'red', 29: 'red', 30: 'red', 31: 'red', 32: 'red', 33: 'red', 34: 'red', 35: 'green', 36: 'green', 37: 'green', 38: 'green', 39: 'green', 40: 'red', 41: 'red', 42: 'red', 43: 'green', 44: 'green', 45: 'green', 46: 'green', 47: 'green', 48: 'green', 49: 'green', 50: 'green', 51: 'green', 52: 'green', 53: 'green', 54: 'green', 55: 'green', 56: 'green', 57: 'green', 58: 'green', 59: 'red', 60: 'red', 61: 'red', 62: 'red', 63: 'red', 64: 'red', 65: 'green', 66: 'green', 67: 'green', 68: 'green', 69: 'green', 70: 'green', 71: 'green', 72: 'green', 73: 'green', 74: 'green', 75: 'green', 76: 'green', 77: 'green', 78: 'green', 79: 'green', 80: 'green', 81: 'green', 82: 'green', 83: 'green', 84: 'green', 85: 'green', 86: 'green', 87: 'green', 88: 'green', 89: 'green', 90: 'green', 91: 'green', 92: 'green', 93: 'green', 94: 'green', 95: 'green', 96: 'green', 97: 'green', 98: 'green', 99: 'red', 100: 'red', 101: 'red', 102: 'red', 103: 'red', 104: 'red', 105: 'red', 106: 'red', 107: 'red', 108: 'red', 109: 'red', 110: 'red', 111: 'red', 112: 'red', 113: 'red', 114: 'red', 115: 'red', 116: 'green', 117: 'green', 118: 'green', 119: 'green', 120: 'green', 121: 'green', 122: 'green', 123: 'green', 124: 'green', 125: 'green', 126: 'green', 127: 'green', 128: 'green', 129: 'green', 130: 'green', 131: 'green', 132: 'green', 133: 'green', 134: 'green', 135: 'green', 136: 'green', 137: 'red', 138: 'red', 139: 'red', 140: 'red', 141: 'red', 142: 'red', 143: 'red', 144: 'red', 145: 'red', 146: 'red', 147: 'red', 148: 'red', 149: 'red', 150: 'red', 151: 'red', 152: 'red', 153: 'red', 154: 'green', 155: 'green', 156: 'green', 157: 'green', 158: 'green', 159: 'red', 160: 'red', 161: 'red', 162: 'green', 163: 'green', 164: 'green', 165: 'green', 166: 'red', 167: 'red', 168: 'red', 169: 'red', 170: 'red', 171: 'green', 172: 'green', 173: 'green', 174: 'green', 175: 'green', 176: 'green', 177: 'green', 178: 'green', 179: 'green', 180: 'green', 181: 'green'}
# turn color (green is both possible, blue is left, red right
TURN_TRACK = {0: 'blue', 1: 'blue', 2: 'blue', 3: 'blue', 4: 'blue', 5: 'blue', 6: 'blue', 7: 'blue', 8: 'blue', 9: 'blue', 10: 'blue', 11: 'blue', 12: 'blue', 13: 'blue', 14: 'blue', 15: 'blue', 16: 'blue', 17: 'blue', 18: 'blue', 19: 'blue', 20: 'blue', 21: 'blue', 22: 'blue', 23: 'blue', 24: 'blue', 25: 'green', 26: 'green', 27: 'green', 28: 'green', 29: 'green', 30: 'green', 31: 'green', 32: 'red', 33: 'red', 34: 'red', 35: 'red', 36: 'red', 37: 'red', 38: 'red', 39: 'red', 40: 'blue', 41: 'blue', 42: 'blue', 43: 'blue', 44: 'blue', 45: 'blue', 46: 'blue', 47: 'blue', 48: 'blue', 49: 'blue', 50: 'blue', 51: 'blue', 52: 'blue', 53: 'blue', 54: 'blue', 55: 'blue', 56: 'blue', 57: 'blue', 58: 'blue', 59: 'blue', 60: 'blue', 61: 'blue', 62: 'blue', 63: 'blue', 64: 'blue', 65: 'blue', 66: 'blue', 67: 'blue', 68: 'blue', 69: 'blue', 70: 'blue', 71: 'blue', 72: 'blue', 73: 'blue', 74: 'blue', 75: 'blue', 76: 'blue', 77: 'blue', 78: 'blue', 79: 'blue', 80: 'blue', 81: 'blue', 82: 'blue', 83: 'blue', 84: 'blue', 85: 'blue', 86: 'blue', 87: 'blue', 88: 'blue', 89: 'blue', 90: 'blue', 91: 'blue', 92: 'blue', 93: 'blue', 94: 'blue', 95: 'blue', 96: 'blue', 97: 'blue', 98: 'blue', 99: 'blue', 100: 'blue', 101: 'blue', 102: 'blue', 103: 'blue', 104: 'blue', 105: 'red', 106: 'red', 107: 'red', 108: 'red', 109: 'red', 110: 'red', 111: 'red', 112: 'red', 113: 'red', 114: 'red', 115: 'blue', 116: 'blue', 117: 'blue', 118: 'blue', 119: 'blue', 120: 'blue', 121: 'blue', 122: 'blue', 123: 'blue', 124: 'blue', 125: 'blue', 126: 'blue', 127: 'blue', 128: 'blue', 129: 'blue', 130: 'blue', 131: 'blue', 132: 'blue', 133: 'blue', 134: 'blue', 135: 'blue', 136: 'blue', 137: 'blue', 138: 'blue', 139: 'blue', 140: 'red', 141: 'red', 142: 'red', 143: 'red', 144: 'red', 145: 'red', 146: 'red', 147: 'red', 148: 'red', 149: 'red', 150: 'blue', 151: 'blue', 152: 'blue', 153: 'blue', 154: 'blue', 155: 'blue', 156: 'blue', 157: 'blue', 158: 'blue', 159: 'blue', 160: 'blue', 161: 'blue', 162: 'blue', 163: 'blue', 164: 'blue', 165: 'blue', 166: 'blue', 167: 'blue', 168: 'blue', 169: 'blue', 170: 'blue', 171: 'blue', 172: 'blue', 173: 'blue', 174: 'blue', 175: 'blue', 176: 'blue', 177: 'blue', 178: 'blue', 179: 'blue', 180: 'blue', 181: 'blue'}

RED = "red"
BLUE = "blue"
ORANGE = "orange"
GREEN = "green"
ORANGE_SPEED = 0.75
RED_SPEED = 0.50


def reward_function(params):
    # Give higher reward if the car is closer to center line and vice versa and moving faster
    reward = max(MIN_REWARD, MAX_REWARD
                 * speed_reward(params)
                 * distance_from_center_reward(params)
                 * angle_with_closest_waypoint_reward(params)
                 * steering_reward(params)
                 * of_track_reward(params)
                 * specific_turn_direction(params))
    print("result_row {} {} {} {} {}".format(speed_reward(params),
                                             distance_from_center_reward(params),
                                             angle_with_closest_waypoint_reward(params),
                                             steering_reward(params),
                                             of_track_reward(params)))
    progress = params["progress"]
    if progress >= 100:
        reward += 100

    return float(reward)


# prevent leaving of track
def of_track_reward(params):
    all_wheels_on_track = params["all_wheels_on_track"]
    if all_wheels_on_track:
        return 1
    else:
        return 0


# prevent steering to match to avoid sliding
def steering_reward(params):
    steering_angle = params['steering_angle']
    s_color = get_color(params, SPEED_TRACK)
    steering_threshold_angle = STEERING_THRESHOLD
    if s_color == GREEN:
        steering_threshold_angle = GREEN_STEERING_THRESHOLD
    if steering_angle > steering_threshold_angle:
        return 0.5 + (90 - steering_angle) / 180
    return 1


# give more points if racer has faster current speed
def speed_reward(params):
    current_speed = params['speed']
    s_color = get_color(params, SPEED_TRACK)
    if s_color == GREEN:
        # square function is because to punish more for low speed
        return (current_speed / MAX_SPEED) * (current_speed / MAX_SPEED)
    elif s_color == ORANGE:
        return 1 - max(0, ORANGE_SPEED - current_speed / MAX_SPEED) - max(0, current_speed / MAX_SPEED - ORANGE_SPEED)
    elif s_color == RED:
        return 1 - max(0, RED_SPEED - current_speed / MAX_SPEED) - max(0, current_speed / MAX_SPEED - RED_SPEED)


# compare current degree and closest waypoint degree, reward of values is pointing to the same direction
def angle_with_closest_waypoint_reward(params):
    heading = params['heading']
    is_left_of_center = params['is_left_of_center']
    difference = heading - closest_waypoint_angle(params)
    if difference > 90:
        return 0
    else:
        if is_left_of_center and -ALLOWED_CORRECTION_ANGLE <= difference < 0:
            return 1
        if not is_left_of_center and 0 < difference <= ALLOWED_CORRECTION_ANGLE:
            return 1
        return 1 - (abs(difference) / 180)


# give more points if racer is following center line
def distance_from_center_reward(params):
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    return min(1, (track_width - distance_from_center) / track_width + 0.2)


# use "closest_waypoint" params to find current angle for road
def closest_waypoint_angle(params):
    closest_waypoints = params['closest_waypoints']
    waypoints = params['waypoints']
    prev_point = waypoints[closest_waypoints[0]]
    next_point = waypoints[closest_waypoints[1]]
    angle = math.degrees(math.atan2(prev_point[1] - next_point[1], prev_point[0] - next_point[0])) - 180.0
    if angle <= -180:
        angle += 360
    return angle


# return 0 reward for any turn that is not expected in this part of track,
# this make sense for places where we what to do only left\right turn
def specific_turn_direction(params):
    steering_angle = params['steering_angle']
    color = get_color(params, TURN_TRACK)
    if GREEN == color:
        return 1
    if RED == color and steering_angle <= 0:
        return 1
    if BLUE == color and steering_angle >= 0:
        return 1
    return 0


# get speed color (green is max speed, orange is middle, red for slow parts
def get_color(params, track):
    closest_waypoints = params['closest_waypoints']
    if closest_waypoints[1] in track:
        return track[closest_waypoints[1]]
    return GREEN
