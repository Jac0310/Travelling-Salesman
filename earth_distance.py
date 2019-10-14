from math import *

def distance(lat1degrees, long1degrees, lat2degrees, long2degrees):
    earth_radius = 3956  # miles
    lat1 = radians(lat1degrees)
    long1 = radians(long1degrees)
    lat2 = radians(lat2degrees)
    long2 = radians(long2degrees)
    lat_difference = lat2 - lat1
    long_difference = long2 - long1
    sin_half_lat = sin(lat_difference / 2)
    sin_half_long = sin(long_difference / 2)
    a = sin_half_lat ** 2 + cos(lat1) * cos(lat2) * sin_half_long ** 2
    c = 2 * atan2(sqrt(a), sqrt(1.0 - a))
    return earth_radius * c

def tot_distance(road_map):
    total_distance = 0
    for i in range(len(road_map)-1):
        lat_1 = road_map[i][2] 
        lat_2 = road_map[i+1][2]
        lon_1 = road_map[i][3]
        lon_2 = road_map[i+1][3]
        total_distance += distance(lat_1, lon_1, lat_2, lon_2)
    return total_distance
