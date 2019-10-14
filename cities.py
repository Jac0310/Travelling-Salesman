from math import *
from copy import *
from earth_distance import *
import random
def read_cities(file_name):
    '''
    Reads State, City, Lattitude longitude data from specified location and returns
    a list of tuples representing a circular roadmap - the salesman's route.
    '''

    infile = open(file_name, 'r')
    read = False
    road_map = []
    while not read:
        line = infile.readline()
        line.rstrip()
        if line != '':
            word = line.split('\t')
            word = tuple(word)
            state, city, lat, lon = word
            lat = float(lat)
            lon = float(lon)
            road_map.append((state, city, lat, lon))
        else:
            read = True
    first = road_map[0]
    road_map.append(first)
    return road_map
    
  
def print_cities(road_map):
    '''
    Prints simplified road map data, with city name and lattitude/longitude to 2 sf.
    '''
    city_list = []
    sf = 2
    for i in road_map:
        state, city, lat, lon = i
        city_list.append((city, round(lat, sf), round(lon, sf)))
    print(city_list)


def compute_total_distance(road_map):
    '''
    Uses total distance function from earth_distance.py to return the total
    distance incurred by travelling the entire route of the current road_map.
    '''
    total_distance = 0
    trips = len(road_map)-1
    for i in range(trips):
        nxt = i+1
        state, city, lat_1, lon_1 = road_map[i]
        state, city, lat_2, lon_2 = road_map[nxt]
        total_distance += distance(lat_1, lon_1, lat_2, lon_2)
    return float(total_distance)
        

def swap_adjacent_cities(road_map, index):
    '''
    Takes the city at location `index` in the `road_map`, and the city at 
    location `index+1` (or at `0`, if `index` refers to the last element 
    in the list), swaps their positions in the `road_map`, computes the 
    new total distance, and returns the tuple 

        (new_road_map, new_total_distance)
        
    '''
    if index == len(road_map)-1:
        index = 0
    new_road_map = copy(road_map[:-1])
    nxt = new_road_map[(index + 1) % len(new_road_map)]
    new_road_map[(index + 1) % len(new_road_map)] = new_road_map[index]
    new_road_map[index] = nxt
    first = new_road_map[0]
    new_road_map.append(first)
    return (new_road_map, compute_total_distance(new_road_map))

def swap_cities(road_map, index1, index2): #test
    '''
    Takes the city at location `index` in the `road_map`, and the 
    city at location `index2`, swaps their positions in the `road_map`, 
    computes the new total distance, and returns the tuple 

        (new_road_map, new_total_distance)
        
    '''
    if index1 == len(road_map)-1:
        index1 = 0
    if index2 == len(road_map)-1:
        index2 = 0
    new_road_map = copy(road_map[:-1])
    new_road_map[index1] = road_map[index2]
    new_road_map[index2] = road_map[index1]
    first = new_road_map[0]
    new_road_map.append(first)
    return (new_road_map, compute_total_distance(new_road_map))
    
   

def find_best_cycle(road_map): #test
    '''
    Using a combination of `swap_cities` and `swap_adjacent_cities`, 
    finds the 'best' cycle.
    '''
    best_map = copy(road_map)
    best_distance = compute_total_distance(road_map)
    new_map = copy(road_map)
    swaps = 0
    swapLimit = 10000
    increment = 2
    while swaps <= swapLimit:
        new_map, new_distance = swap_cities(new_map, random.randint(0, len(road_map)-1), random.randint(0, len(road_map)-1))
        new_map, new_distance = swap_adjacent_cities(new_map, random.randint(0, len(road_map)-1))
        if new_distance < best_distance:
            best_map = new_map
            best_distance = new_distance
        swaps +=increment
    return best_map
        
        
        
    


def print_map(road_map):
    '''
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    '''
    cityIndex = 1
    sf = 2
    for i in range(len(road_map)-1):
        nxt = i+1
        state, city, lat_1, lon_1 = road_map[i]
        state, city, lat_2, lon_2 = road_map[nxt]
        print(str(road_map[i][cityIndex]) + " --> " + str(road_map[i+1][cityIndex]))
        print("Distance: " + str(round(distance(lat_1, lon_1, lat_2, lon_2), sf)) + " miles.")
    print()
    print("Total distance: " + str(round(compute_total_distance(road_map))))
            
        


def main():
    '''
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    '''
    print('Please enter file name containing city data: ', end = '')
    file_name = str(input())
    road_map = read_cities(file_name)
    print("Pre sorting: ")
    print_map(road_map)
    print()
    best_map = find_best_cycle(road_map)
    print("After sorting: ")
    print_map(best_map)
          
    
    

if __name__ == "__main__":
    main()


    
