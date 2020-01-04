"""
Jason is stranded in a desert.His phone's battery is going to die out and all he has left is a compass.
Parse the JaSON.json(in src/res) file and get the latitude and longitude values of the current and destination location.
Also find the distance between those two locations (refer resources for the link)
Return a Directions json file with your personalized message, distance and some direction.

"""

import json
import math


def parse_json(file_path):
    """
    Reads a json file and returns a python dictionary
    :param file_path: path and file name of json file
    :return: a python dictionary equivalent to the json data
    """
    j_data = open(file_path, 'r')
    s_data = ""
    for line in j_data:
        s_data += line
    j_data.close()
    s_data.strip()
    p_data = json.loads(s_data)
    return p_data


def degrees_to_radians(degrees):
    """
    Converts degrees to radians
    :param degrees: a number of degrees
    :return: a float value of radians
    """
    return degrees * math.pi / 180


def distance_in_km_between_earth_coordinates(b, e):
    """
    Calculates the distance in km between two points on earth
    :param b: a tuple containing the latitude and longitude (both floats) of the starting point
    :param e: a tuple containing the latitude and longitude (both floats) of the ending point
    :return: the number of km between the two points (a float)
    """
    earth_radius_km = 6371

    d_lat = degrees_to_radians(e[0] - b[0])
    d_lon = degrees_to_radians(e[1] - b[1])

    lat1 = degrees_to_radians(b[0])
    lat2 = degrees_to_radians(e[0])

    a = math.sin(d_lat / 2) * math.sin(d_lat / 2) + math.sin(d_lon / 2) * math.sin(d_lon / 2) * math.cos(lat1) \
        * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return earth_radius_km * c


def calculate_compass_bearing(point_a, point_b):
    """
    Calculates the bearing between two points.
    The formulae used is the following:
        θ = atan2(sin(Δlong).cos(lat2),
                  cos(lat1).sin(lat2) − sin(lat1).cos(lat2).cos(Δlong))
    :Parameters:
      - `pointA: The tuple representing the latitude/longitude for the
        first point. Latitude and longitude must be in decimal degrees
      - `pointB: The tuple representing the latitude/longitude for the
        second point. Latitude and longitude must be in decimal degrees
    :Returns:
      The bearing in degrees
    :Returns Type:
      float
    """
    # LICENSE: public domain from https://gist.github.com/jeromer/2005586

    if (type(point_a) != tuple) or (type(point_b) != tuple):
        raise TypeError("Only tuples are supported as arguments")

    lat1 = math.radians(point_a[0])
    lat2 = math.radians(point_b[0])

    diff_long = math.radians(point_b[1] - point_a[1])

    x = math.sin(diff_long) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
                                           * math.cos(lat2) * math.cos(diff_long))

    initial_bearing = math.atan2(x, y)

    # Now we have the initial bearing but math.atan2 return values
    # from -180° to + 180° which is not what we want for a compass bearing
    # The solution is to normalize the initial bearing as shown below
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing


def get_direction_letters(d):
    """
    Calculates the 16 point abbreviated representation of a numerical bearing
    :param d: a float representing a compass bearing
    :return: a string containing the 16 point bearing in letters
    """
    d_letters = ('N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW')
    x = int((d + 11.25) / 22.5) % 16
    return d_letters[x]


two_points = parse_json('txt/JaSON2.json')

st_lat_long = two_points['markers'][0]['location'][0], two_points['markers'][0]['location'][1]
dest_lat_long = two_points['markers'][1]['location'][0], two_points['markers'][1]['location'][1]

print('Start: {}, End: {}'.format(st_lat_long, dest_lat_long))

dist = distance_in_km_between_earth_coordinates(st_lat_long, dest_lat_long)
direction = calculate_compass_bearing(st_lat_long, dest_lat_long)
direction_letters = get_direction_letters(direction)
message = "Follow the direction for the distance listed to get to the destination."

data_to_convert = {"directions": [{"message": message, "distance": dist, "direction": direction_letters}]}

print(data_to_convert)

j_directions = json.dumps(data_to_convert)

f = open('txt/directions.json', 'w')
for l in j_directions:
    f.write(l)
f.close()
