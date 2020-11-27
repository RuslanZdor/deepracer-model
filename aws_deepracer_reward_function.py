# define constants for function
import math

# in case of negative reward - use thin min value
MIN_REWARD = 1e-3

# max speed for racer
MAX_SPEED = 3

# max possible reward for aws function
MAX_REWARD = 1

# angle for not punishing for line correction
ALLOWED_CORRECTION_ANGLE = 15

# angle for not punishing for line correction
STEERING_THRESHOLD = 20

SPEED_TRACK = {}
RED = "red"
ORANGE = "orange"
GREEN = "green"
ORANGE_SPEED = 0.70
RED_SPEED = 0.40
for i in range(0, 10):
    SPEED_TRACK[i] = GREEN
for i in range(20, 45):
    SPEED_TRACK[i] = ORANGE
for i in range(53, 70):
    SPEED_TRACK[i] = ORANGE
for i in range(70, 85):
    SPEED_TRACK[i] = GREEN
for i in range(85, 91):
    SPEED_TRACK[i] = ORANGE
for i in range(91, 120):
    SPEED_TRACK[i] = GREEN
for i in range(175, 195):
    SPEED_TRACK[i] = ORANGE
for i in range(195, 205):
    SPEED_TRACK[i] = ORANGE
for i in range(205, 224):
    SPEED_TRACK[i] = GREEN


def reward_function(params):
    """
    Example of rewarding the agent to follow center line
    """

    # Give higher reward if the car is closer to center line and vice versa and moving faster
    reward = max(MIN_REWARD, MAX_REWARD
                 * speed_reward(params)
                 * distance_from_center_reward(params)
                 * angle_with_closest_waypoint_reward(params)
                 * steering_reward(params)
                 * of_track_reward(params))
    print("result_row {} {} {} {} {}".format(speed_reward(params),
                                             distance_from_center_reward(params),
                                             angle_with_closest_waypoint_reward(params),
                                             steering_reward(params),
                                             of_track_reward(params)))
    progress = params["progress"]
    if progress == 100.0:
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
    if steering_angle > STEERING_THRESHOLD:
        return 0.5 + (90 - steering_angle) / 180
    return 1


# give more points if racer has faster current speed
def speed_reward(params):
    current_speed = params['speed']
    s_color = speed_color(params)
    if s_color == GREEN:
        return current_speed / MAX_SPEED
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
        return 0.5
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
    return (track_width - distance_from_center) / track_width


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


# get speed color (green is max speed, orange is middle, red for slow parts
def speed_color(params):
    closest_waypoints = params['closest_waypoints']
    if closest_waypoints[1] in SPEED_TRACK:
        return SPEED_TRACK[closest_waypoints[1]]
    return RED
