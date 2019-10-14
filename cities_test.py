from cities import *
from earth_distance import *
import pytest

def testCompute_total_distance():
    ary = [('blackpool', 'england', 53.8175053, -3.035674800000038), ('Glasgow', 'Scotland', 55.864237, -4.251805999999988),
           ('blackpool', 'england', 53.8175053, -3.035674800000038)]
    assert compute_total_distance(ary) == pytest.approx(tot_distance(ary))

def testCompute_total_distance_1():
    ary = [('blackpool', 'england', 53.8175053, -3.035674800000038), ('Glasgow', 'Scotland', 55.864237, -4.251805999999988),
           ('Paris', 'France', 48.8566, 2.3522), ('blackpool', 'england', 53.8175053, -3.035674800000038)]
    assert compute_total_distance(ary) == pytest.approx(tot_distance(ary))

def testSwap_adjacent_cities():
     ary = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974),
            ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Arkansas', 'Little Rock', 34.736009, -92.331122),
            ('California', 'Sacramento', 38.555605, -121.468926), ('Colorado', 'Denver', 39.7391667, -104.984167),
            ('Alabama', 'Montgomery', 32.361538, -86.279118)]
     swapped = [('Alaska', 'Juneau', 58.301935, -134.41974), ('Alabama', 'Montgomery', 32.361538, -86.279118),
                ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Arkansas', 'Little Rock', 34.736009, -92.331122),
                ('California', 'Sacramento', 38.555605, -121.468926), ('Colorado', 'Denver', 39.7391667, -104.984167),
                ('Alaska', 'Juneau', 58.301935, -134.41974)]
     swap, distance = swap_adjacent_cities(ary, 0)
     assert swap == swapped
     assert distance == pytest.approx(tot_distance(swapped))
     
def testSwap_adjacent_cities_1():
     ary = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974),
            ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Arkansas', 'Little Rock', 34.736009, -92.331122),
            ('California', 'Sacramento', 38.555605, -121.468926), ('Colorado', 'Denver', 39.7391667, -104.984167),
            ('Alabama', 'Montgomery', 32.361538, -86.279118)]
     swapped = [('Alaska', 'Juneau', 58.301935, -134.41974), ('Alabama', 'Montgomery', 32.361538, -86.279118),
                ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Arkansas', 'Little Rock', 34.736009, -92.331122),
                ('California', 'Sacramento', 38.555605, -121.468926), ('Colorado', 'Denver', 39.7391667, -104.984167),
                ('Alaska', 'Juneau', 58.301935, -134.41974)]
     swap, distance = swap_adjacent_cities(ary, len(ary)-1)
     assert swap == swapped
     assert distance == pytest.approx(tot_distance(swapped)) 

def testSwap_adjacent_cities_2():
     ary = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974),
            ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Arkansas', 'Little Rock', 34.736009, -92.331122),
            ('California', 'Sacramento', 38.555605, -121.468926), ('Colorado', 'Denver', 39.7391667, -104.984167),
            ('Alabama', 'Montgomery', 32.361538, -86.279118)]
     swapped = [('Colorado', 'Denver', 39.7391667, -104.984167), ('Alaska', 'Juneau', 58.301935, -134.41974),
            ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Arkansas', 'Little Rock', 34.736009, -92.331122),
            ('California', 'Sacramento', 38.555605, -121.468926), ('Alabama', 'Montgomery', 32.361538, -86.279118),
                 ('Colorado', 'Denver', 39.7391667, -104.984167)]
     swap, distance = swap_adjacent_cities(ary, len(ary)-2)
     assert swap == swapped
     assert distance == pytest.approx(tot_distance(swapped))

def testSwap_adjacent_cities_3():
     ary = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974),
            ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Arkansas', 'Little Rock', 34.736009, -92.331122),
            ('California', 'Sacramento', 38.555605, -121.468926), ('Colorado', 'Denver', 39.7391667, -104.984167),
            ('Alabama', 'Montgomery', 32.361538, -86.279118)]
     swapped = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974),
            ('Arkansas', 'Little Rock', 34.736009, -92.331122), ('Arizona', 'Phoenix', 33.448457, -112.073844),
            ('California', 'Sacramento', 38.555605, -121.468926), ('Colorado', 'Denver', 39.7391667, -104.984167),
            ('Alabama', 'Montgomery', 32.361538, -86.279118)]
     swap, distance = swap_adjacent_cities(ary, 2)
     assert swap == swapped
     assert distance == pytest.approx(tot_distance(swapped)) 


def testSwap_cities():
    ary = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974),
           ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Arkansas', 'Little Rock', 34.736009, -92.331122),
           ('California', 'Sacramento', 38.555605, -121.468926), ('Colorado', 'Denver', 39.7391667, -104.984167),
           ('Alabama', 'Montgomery', 32.361538, -86.279118)]
    swapped = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974),
           ('California', 'Sacramento', 38.555605, -121.468926), ('Arkansas', 'Little Rock', 34.736009, -92.331122),
           ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Colorado', 'Denver', 39.7391667, -104.984167),
           ('Alabama', 'Montgomery', 32.361538, -86.279118)]
    swap, distance = swap_cities(ary, 2, 4)
    assert swap == swapped
    assert distance == pytest.approx(tot_distance(swapped))

def testSwap_cities_1():
    ary = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974),
           ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Arkansas', 'Little Rock', 34.736009, -92.331122),
           ('California', 'Sacramento', 38.555605, -121.468926), ('Colorado', 'Denver', 39.7391667, -104.984167),
           ('Alabama', 'Montgomery', 32.361538, -86.279118)]
    swap, distance = swap_cities(ary, 2, 2)
    assert swap == ary
    assert distance == pytest.approx(tot_distance(ary))
    
def testSwap_cities_2():
    ary = [('Colorado', 'Denver', 39.7391667, -104.984167), ('Alaska', 'Juneau', 58.301935, -134.41974),
           ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Arkansas', 'Little Rock', 34.736009, -92.331122),
           ('California', 'Sacramento', 38.555605, -121.468926), ('Colorado', 'Denver', 39.7391667, -104.984167)]
    swap, distance = swap_cities(ary, 0, len(ary)-1)
    assert swap == ary
    assert distance == pytest.approx(tot_distance(ary))

def testSwap_cities_3():
    ary = [('Colorado', 'Denver', 39.7391667, -104.984167), ('Alaska', 'Juneau', 58.301935, -134.41974),
           ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Arkansas', 'Little Rock', 34.736009, -92.331122),
           ('California', 'Sacramento', 38.555605, -121.468926), ('Colorado', 'Denver', 39.7391667, -104.984167)]
    swapped = [('Alaska', 'Juneau', 58.301935, -134.41974), ('Colorado', 'Denver', 39.7391667, -104.984167),
           ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Arkansas', 'Little Rock', 34.736009, -92.331122),
           ('California', 'Sacramento', 38.555605, -121.468926), ('Alaska', 'Juneau', 58.301935, -134.41974)]
    swap, distance = swap_cities(ary, 0, 1)
    assert swap == swapped
    assert distance == pytest.approx(tot_distance(swapped))
    
def testFind_best_cycle():
    ary = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974), ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Arkansas', 'Little Rock', 34.736009, -92.331122), ('California', 'Sacramento', 38.555605, -121.468926), ('Colorado', 'Denver', 39.7391667, -104.984167), ('Connecticut', 'Hartford', 41.767, -72.677), ('Delaware', 'Dover', 39.161921, -75.526755), ('Florida', 'Tallahassee', 30.4518, -84.27277), ('Georgia', 'Atlanta', 33.76, -84.39), ('Hawaii', 'Honolulu', 21.30895, -157.826182), ('Idaho', 'Boise', 43.613739, -116.237651), ('Illinois', 'Springfield', 39.78325, -89.650373), ('Indiana', 'Indianapolis', 39.790942, -86.147685), ('Iowa', 'Des Moines', 41.590939, -93.620866), ('Kansas', 'Topeka', 39.04, -95.69), ('Kentucky', 'Frankfort', 38.197274, -84.86311), ('Louisiana', 'Baton Rouge', 30.45809, -91.140229), ('Maine', 'Augusta', 44.323535, -69.765261), ('Maryland', 'Annapolis', 38.972945, -76.501157), ('Massachusetts', 'Boston', 42.2352, -71.0275), ('Michigan', 'Lansing', 42.7335, -84.5467), ('Minnesota', 'Saint Paul', 44.95, -93.094), ('Mississippi', 'Jackson', 32.32, -90.207), ('Missouri', 'Jefferson City', 38.572954, -92.189283), ('Montana', 'Helana', 46.595805, -112.027031), ('Nebraska', 'Lincoln', 40.809868, -96.675345), ('Nevada', 'Carson City', 39.160949, -119.753877), ('New Hampshire', 'Concord', 43.220093, -71.549127), ('New Jersey', 'Trenton', 40.221741, -74.756138), ('New Mexico', 'Santa Fe', 35.667231, -105.964575), ('New York', 'Albany', 42.659829, -73.781339), ('North Carolina', 'Raleigh', 35.771, -78.638), ('North Dakota', 'Bismarck', 48.813343, -100.779004), ('Ohio', 'Columbus', 39.962245, -83.000647), ('Oklahoma', 'Oklahoma City', 35.482309, -97.534994), ('Oregon', 'Salem', 44.931109, -123.029159), ('Pennsylvania', 'Harrisburg', 40.269789, -76.875613), ('Rhode Island', 'Providence', 41.82355, -71.422132), ('South Carolina', 'Columbia', 34.0, -81.035), ('South Dakota', 'Pierre', 44.367966, -100.336378), ('Tennessee', 'Nashville', 36.165, -86.784), ('Texas', 'Austin', 30.266667, -97.75), ('Utah', 'Salt Lake City', 40.7547, -111.892622), ('Vermont', 'Montpelier', 44.26639, -72.57194), ('Virginia', 'Richmond', 37.54, -77.46), ('Washington', 'Olympia', 47.042418, -122.893077), ('West Virginia', 'Charleston', 38.349497, -81.633294), ('Wisconsin', 'Madison', 43.074722, -89.384444), ('Wyoming', 'Cheyenne', 41.145548, -104.802042), ('Alabama', 'Montgomery', 32.361538, -86.279118)]
    assert compute_total_distance(find_best_cycle(ary)) < tot_distance(ary)

def testFind_best_cycle_1():
    ary = [('blackpool', 'england', 53.8175053, -3.035674800000038), ('Glasgow', 'Scotland', 55.864237, -4.251805999999988), ('Paris', 'France', 48.8566, 2.3522)]
    assert compute_total_distance(find_best_cycle(ary)) < tot_distance(ary)

def testFind_best_cycle_repeats():

    ary = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974),
            ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Arkansas', 'Little Rock', 34.736009, -92.331122),
            ('California', 'Sacramento', 38.555605, -121.468926), ('Colorado', 'Denver', 39.7391667, -104.984167),
            ('Alabama', 'Montgomery', 32.361538, -86.279118)]
    road_map = find_best_cycle(ary)
    repeat = 0
    for i in road_map:
        state, city, lat, lon = i
        if state == 'Alaska':
            repeat += 1
             
    assert repeat < 2
        
    
        



