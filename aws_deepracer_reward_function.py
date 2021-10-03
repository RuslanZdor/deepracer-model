# define constants for function
import math

# in case of negative reward - use thin min value
MIN_REWARD = 1e-3

# max speed for racer
MAX_SPEED = 3

# max possible reward for aws function
MAX_REWARD = 1

# angle for not punishing for line correction
ALLOWED_CORRECTION_ANGLE = 10

# angle for not punishing for line correction
STEERING_THRESHOLD = 20
GREEN_STEERING_THRESHOLD = 10

# speed color (green is max speed, orange is middle, red for slow parts
SPEED_TRACK = {0: 'orange', 1: 'orange', 2: 'orange', 3: 'orange', 4: 'orange', 5: 'orange', 6: 'orange', 7: 'orange', 8: 'orange', 9: 'orange', 10: 'orange', 11: 'orange', 12: 'green', 13: 'green', 14: 'green', 15: 'green', 16: 'green', 17: 'green', 18: 'green', 19: 'green', 20: 'green', 21: 'green', 22: 'green', 23: 'green', 24: 'green', 25: 'green', 26: 'green', 27: 'green', 28: 'green', 29: 'green', 30: 'green', 31: 'green', 32: 'green', 33: 'green', 34: 'green', 35: 'green', 36: 'green', 37: 'green', 38: 'orange', 39: 'orange', 40: 'orange', 41: 'orange', 42: 'orange', 43: 'orange', 44: 'green', 45: 'green', 46: 'green', 47: 'green', 48: 'green', 49: 'green', 50: 'green', 51: 'green', 52: 'green', 53: 'green', 54: 'green', 55: 'green', 56: 'green', 57: 'green', 58: 'green', 59: 'green', 60: 'green', 61: 'green', 62: 'green', 63: 'green', 64: 'green', 65: 'green', 66: 'green', 67: 'green', 68: 'green', 69: 'green', 70: 'green', 71: 'green', 72: 'green', 73: 'green', 74: 'green', 75: 'green', 76: 'green', 77: 'green', 78: 'orange', 79: 'orange', 80: 'orange', 81: 'orange', 82: 'orange', 83: 'orange', 84: 'orange', 85: 'orange', 86: 'orange', 87: 'orange', 88: 'orange', 89: 'orange', 90: 'orange', 91: 'orange', 92: 'orange', 93: 'orange', 94: 'orange', 95: 'orange', 96: 'orange', 97: 'orange', 98: 'orange', 99: 'orange', 100: 'green', 101: 'green', 102: 'green', 103: 'green', 104: 'green', 105: 'green', 106: 'green', 107: 'green', 108: 'green', 109: 'green', 110: 'green', 111: 'green', 112: 'green', 113: 'green', 114: 'green', 115: 'green', 116: 'green', 117: 'green', 118: 'green', 119: 'green', 120: 'orange', 121: 'orange', 122: 'orange', 123: 'orange', 124: 'orange', 125: 'orange', 126: 'orange', 127: 'orange', 128: 'orange', 129: 'orange', 130: 'green', 131: 'green', 132: 'green', 133: 'green', 134: 'green', 135: 'green', 136: 'green', 137: 'green', 138: 'green', 139: 'orange', 140: 'orange', 141: 'orange', 142: 'orange', 143: 'orange', 144: 'orange', 145: 'orange', 146: 'orange', 147: 'orange', 148: 'orange', 149: 'orange', 150: 'orange', 151: 'orange', 152: 'orange', 153: 'orange', 154: 'orange'}
# turn color (green is both possible, blue is left, red right
TURN_TRACK = {0: 'blue', 1: 'blue', 2: 'blue', 3: 'blue', 4: 'blue', 5: 'blue', 6: 'blue', 7: 'blue', 8: 'blue', 9: 'blue', 10: 'blue', 11: 'blue', 12: 'blue', 13: 'blue', 14: 'blue', 15: 'blue', 16: 'blue', 17: 'blue', 18: 'blue', 19: 'blue', 20: 'blue', 21: 'blue', 22: 'blue', 23: 'blue', 24: 'blue', 25: 'blue', 26: 'blue', 27: 'blue', 28: 'blue', 29: 'blue', 30: 'blue', 31: 'blue', 32: 'blue', 33: 'blue', 34: 'blue', 35: 'blue', 36: 'blue', 37: 'blue', 38: 'blue', 39: 'blue', 40: 'blue', 41: 'blue', 42: 'blue', 43: 'blue', 44: 'blue', 45: 'blue', 46: 'blue', 47: 'blue', 48: 'blue', 49: 'blue', 50: 'blue', 51: 'blue', 52: 'blue', 53: 'blue', 54: 'blue', 55: 'blue', 56: 'blue', 57: 'blue', 58: 'blue', 59: 'blue', 60: 'blue', 61: 'blue', 62: 'blue', 63: 'blue', 64: 'blue', 65: 'blue', 66: 'blue', 67: 'blue', 68: 'blue', 69: 'blue', 70: 'blue', 71: 'blue', 72: 'blue', 73: 'blue', 74: 'blue', 75: 'blue', 76: 'blue', 77: 'blue', 78: 'blue', 79: 'blue', 80: 'blue', 81: 'blue', 82: 'blue', 83: 'blue', 84: 'blue', 85: 'blue', 86: 'blue', 87: 'blue', 88: 'blue', 89: 'blue', 90: 'blue', 91: 'blue', 92: 'blue', 93: 'blue', 94: 'blue', 95: 'blue', 96: 'blue', 97: 'blue', 98: 'blue', 99: 'blue', 100: 'blue', 101: 'blue', 102: 'blue', 103: 'blue', 104: 'blue', 105: 'blue', 106: 'blue', 107: 'blue', 108: 'blue', 109: 'blue', 110: 'blue', 111: 'blue', 112: 'blue', 113: 'blue', 114: 'blue', 115: 'blue', 116: 'blue', 117: 'blue', 118: 'blue', 119: 'blue', 120: 'red', 121: 'red', 122: 'red', 123: 'red', 124: 'red', 125: 'red', 126: 'red', 127: 'red', 128: 'red', 129: 'red', 130: 'blue', 131: 'blue', 132: 'blue', 133: 'blue', 134: 'blue', 135: 'blue', 136: 'blue', 137: 'blue', 138: 'blue', 139: 'blue', 140: 'blue', 141: 'blue', 142: 'blue', 143: 'blue', 144: 'blue', 145: 'blue', 146: 'blue', 147: 'blue', 148: 'blue', 149: 'blue', 150: 'blue', 151: 'blue', 152: 'blue', 153: 'blue', 154: 'blue'}
# turn color (green is both possible, blue is left, red right
BEST_PATH = {0: [0.6306910855808379, 2.8061193187598317], 1: [0.6336712502600561, 2.6907962084913333], 2: [0.64671879844676, 2.5756929069468697], 3: [0.6697223050606538, 2.4618398778926056], 4: [0.7025150580147865, 2.350225687933456], 5: [0.7448758872516801, 2.241775135380155], 6: [0.7965292269381135, 2.137327702073386], 7: [0.8571445889604701, 2.0376165897940752], 8: [0.9263357102737471, 1.9432487198980812], 9: [1.0036597543535617, 1.8546862524469439], 10: [1.0886172129266198, 1.772230506831474], 11: [1.1806536995778907, 1.696009722064841], 12: [1.27916562451252, 1.6259727993301363], 13: [1.3835122734099072, 1.5618915638414308], 14: [1.4930357972437118, 1.5033733456028702], 15: [1.6070863658096604, 1.4498832214458561], 16: [1.7250419173566693, 1.4007717547047782], 17: [1.8463044315529822, 1.3553016080057492], 18: [1.9702560300742156, 1.3126661163655196], 19: [2.09617545495538, 1.271992203465992], 20: [2.2231516963031606, 1.2323237433044643], 21: [2.355769763848039, 1.190680995904921], 22: [2.488141560880269, 1.1483605933912393], 23: [2.620103720427086, 1.1049142988426883], 24: [2.7515551494884045, 1.060066677008878], 25: [2.882456931209304, 1.013714110373173], 26: [3.012839289948518, 0.9659425244006475], 27: [3.1427840323592005, 0.9169779495926159], 28: [3.272395377041519, 0.8671061591514733], 29: [3.4017887089897707, 0.8166419369705296], 30: [3.525342917396783, 0.7679858244272988], 31: [3.64882806345605, 0.720987171881005], 32: [3.772250536689716, 0.6765777939272573], 33: [3.8956574404119717, 0.63576533247025], 34: [4.019126284507557, 0.5993530181742783], 35: [4.142731944487423, 0.5680280672308169], 36: [4.266522653410114, 0.5424025411418923], 37: [4.3905079951724115, 0.5230312892694833], 38: [4.514656201929046, 0.5104131135298673], 39: [4.6388964110707045, 0.5049812580303754], 40: [4.763122708959208, 0.5070893294535697], 41: [4.887198566945313, 0.5169978797966641], 42: [5.010961461768899, 0.534865307431222], 43: [5.134227886556341, 0.5607448881873455], 44: [5.256798894774465, 0.5945880421957306], 45: [5.378466104203227, 0.6362527456138463], 46: [5.499017908693244, 0.6855154688591929], 47: [5.618245558333863, 0.742085046996655], 48: [5.735948761788441, 0.8056172033729188], 49: [5.851940508679295, 0.8757288230719185], 50: [5.966050880918649, 0.952011384173886], 51: [6.078129704479884, 1.034043172514096], 52: [6.188047977606734, 1.1214000482485447], 53: [6.295698090655126, 1.2136646292964919], 54: [6.400992920613838, 1.31043382985293], 55: [6.503863935081087, 1.411324753333731], 56: [6.604258473138035, 1.5159789921070206], 57: [6.702136383470799, 1.6240654306967688], 58: [6.797466194882073, 1.7352816828754838], 59: [6.890220974638877, 1.849354314453712], 60: [6.980374000991022, 1.9660380119143537], 61: [7.067894343462419, 2.085113852939266], 62: [7.15274241399219, 2.2063868202399286], 63: [7.234865528921659, 2.329682677928094], 64: [7.314193510337665, 2.454844303721176], 65: [7.390634358086674, 2.581727544764477], 66: [7.464070041854949, 2.7101966439988354], 67: [7.534352495193162, 2.84011927168856], 68: [7.601299937458228, 2.971361196096969], 69: [7.664693700697912, 3.10378064039297], 70: [7.72427579019867, 3.237222400270733], 71: [7.779747452160063, 3.3715118372928403], 72: [7.830769051478319, 3.5064489135115737], 73: [7.876961568793016, 3.641802488407529], 74: [7.917910001805209, 3.777305152780304], 75: [7.953168896701898, 3.9126489178386086], 76: [7.982270139922662, 4.047482102788967], 77: [8.004733011227984, 4.181407762688826], 78: [8.020076343394738, 4.313983963934398], 79: [8.027832463624136, 4.444726144164974], 80: [8.027562422288899, 4.573111687205757], 81: [8.018871863543648, 4.698586707129901], 82: [8.001426777353679, 4.820574878402188], 83: [7.974968309354319, 4.938487985172062], 84: [7.939325804964658, 5.05173770861867], 85: [7.894427332398623, 5.1597480441847665], 86: [7.840307063210617, 5.261967656632944], 87: [7.777109078607449, 5.357881452681926], 88: [7.705087397848873, 5.4470206857217525], 89: [7.624602269446095, 5.528971005317617], 90: [7.536113001889473, 5.603378019387619], 91: [7.4401678142499055, 5.669950136019715], 92: [7.337391337865675, 5.72845867663389], 93: [7.228470484463541, 5.778735481212128], 94: [7.114139407664787, 5.820668437499423], 95: [6.995164227011861, 5.854195539029028], 96: [6.872328068022163, 5.879298195009649], 97: [6.746416816872122, 5.895994567443778], 98: [6.618205817165343, 5.904333692572592], 99: [6.48844757334331, 5.9043910566086275], 100: [6.357860393423449, 5.896266147481461], 101: [6.227117820955166, 5.880082307761797], 102: [6.096838683332358, 5.8559889855123615], 103: [5.9675776232465605, 5.824166238229436], 104: [5.839816075363149, 5.784831109821287], 105: [5.713953786027748, 5.738245290891735], 106: [5.590301128198999, 5.684723305926886], 107: [5.469072612509523, 5.624640360313229], 108: [5.350382118821539, 5.558438927015279], 109: [5.234240457688271, 5.486633151866064], 110: [5.120555941712524, 5.409810146475074], 111: [5.0091399384955135, 5.328625034520874], 112: [4.899726663769728, 5.243773819450962], 113: [4.792013439209298, 5.155933749255134], 114: [4.6857631032989016, 5.065605453024112], 115: [4.580792695253142, 4.973159174012796], 116: [4.480818783513936, 4.882433566317696], 117: [4.379597479350928, 4.794203275522037], 118: [4.2768435419456345, 4.709068377012267], 119: [4.172249406683978, 4.627695662962578], 120: [4.065537670885524, 4.550718210850859], 121: [3.9564417441231754, 4.478778538106517], 122: [3.8447481655301816, 4.412441040406261], 123: [3.7303111830280584, 4.352156343601486], 124: [3.6130605911709854, 4.298234929044067], 125: [3.493004087571274, 4.250828279140158], 126: [3.3702246819806065, 4.209917859767956], 127: [3.244875114810131, 4.1753097086648605], 128: [3.1171707046380055, 4.146633610700183], 129: [2.9873824736476857, 4.123344222322313], 130: [2.8558513922746442, 4.104669581178079], 131: [2.7228205236536547, 4.090057965450789], 132: [2.58852157791807, 4.078960262504751], 133: [2.453152883048898, 4.070891041745671], 134: [2.316756010055542, 4.065796494483948], 135: [2.1842507909083038, 4.057872394955421], 136: [2.0535654582720935, 4.046523765366982], 137: [1.9251617047886112, 4.031055745613201], 138: [1.79950824831001, 4.010841840448683], 139: [1.6772191072224656, 3.9851132711205137], 140: [1.5587352679576263, 3.9534865034022597], 141: [1.4446663785956435, 3.9154135169441124], 142: [1.3356467086330939, 3.870432395038873], 143: [1.23222980790194, 3.818300743675883], 144: [1.1351925060030505, 3.7586213016948116], 145: [1.0451995262323004, 3.6912827697412762], 146: [0.962855346058243, 3.6163720190513566], 147: [0.8887074841741225, 3.5341512028508957], 148: [0.8232400538850875, 3.445046114429557], 149: [0.7668686360501706, 3.3496316889545286], 150: [0.7199375587667798, 3.2486142141671337], 151: [0.6827192800087478, 3.1428113984019843], 152: [0.6554154295486796, 3.033131233951117], 153: [0.638159054778358, 2.9205502417869615], 154: [0.6306910855808379, 2.8061193187598317]}

RED = "red"
BLUE = "blue"
ORANGE = "orange"
GREEN = "green"
ORANGE_SPEED = 0.75
RED_SPEED = 0.5


def reward_function(params):
    # Give higher reward if the car is closer to center line and vice versa and moving faster
    reward = max(MIN_REWARD, MAX_REWARD
                 * speed_reward(params)
                 * distance_from_best_path_reward(params)
                 * steering_reward(params)
                 * of_track_reward(params))

    steps = params['steps']
    progress = params["progress"]
    if progress >= 100:
        reward += 100

    return float(reward * progress / steps)


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
    if abs(steering_angle) > STEERING_THRESHOLD:
        return 0.8
    return 1


# give more points if racer has faster current speed
def speed_reward(params):
    current_speed = params['speed']
    return (current_speed / MAX_SPEED) * (current_speed / MAX_SPEED)


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


# give more points if racer is following center line
def distance_from_best_path_reward(params):
    closest_waypoints = params['closest_waypoints']
    waypoints = params['waypoints']
    distance_from_center = params['distance_from_center']
    x_car = params['x']
    y_car = params['y']
    first_point = BEST_PATH[closest_waypoints[1]]
    second_point = waypoints[closest_waypoints[1]]

    x_dif = max(first_point[0] - second_point[0], second_point[0] - first_point[0])
    y_dif = max(first_point[1] - second_point[1], second_point[1] - first_point[1])

    line_to_center = math.sqrt(x_dif * x_dif + y_dif * y_dif)

    x_dif = max(first_point[0] - x_car, x_car - first_point[0])
    y_dif = max(first_point[1] - y_car, y_car - first_point[1])

    line_to_car = math.sqrt(x_dif * x_dif + y_dif * y_dif)

    print("line_to_center " + str(line_to_center))
    print("distance_from_center " + str(distance_from_center))
    print("line_to_car " + str(line_to_car))

    if line_to_center >= distance_from_center and line_to_center >= line_to_car:
        return 1
    return 0.3


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
