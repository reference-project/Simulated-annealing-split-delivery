import math

import annealing.distances as distance
from annealing import data_manager


def get_smallest_idx(arr):
    return arr.index(min(arr))


def calculate_distance(x0, x1, y0, y1):
    return math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)


def get_distance_arr(array_list, array):
    distances = []
    for element in array_list:
        point_distance = calculate_distance(element[0], array[0], element[1], array[1])
        distances.append(point_distance)
    return distances


def greedy_algorithm(coordinates_pack):
    route_arr = [[0, 0]]
    for i in range(0, len(coordinates_pack)):
        last_route_arr_idx = len(route_arr) - 1
        coordinates_distances = get_distance_arr(coordinates_pack, route_arr[last_route_arr_idx])
        smallest_idx = get_smallest_idx(coordinates_distances)
        route_arr.append(coordinates_pack[smallest_idx])
        del coordinates_pack[smallest_idx]
    route_arr.append([0, 0])
    return route_arr


def get_data():
    return data_manager.read_data_set("../coordinates.csv", ";")


def get_greedy_distance(data_with_cap):
    get_only_coordinates = data_manager.get_column_from_2d(data_with_cap, 0)
    greedy = greedy_algorithm(get_only_coordinates)
    return distance.calculate_route(greedy)


def get_greedy_distance_whole(data_with_cap):
    whole_distance = 0
    for element in data_with_cap:
        whole_distance += get_greedy_distance(element)
    return whole_distance


def greedy_route(data_with_cap):
    get_only_coordinates = data_manager.get_column_from_2d(data_with_cap, 0)
    return greedy_algorithm(get_only_coordinates)


def get_greedy_route(data_with_cap):
    route = []
    for element in data_with_cap:
        route.append(greedy_route(element))
    return route


if __name__ == '__main__':
    data = get_data()
    capacity_split = data_manager.last_value_split(data)
    print(get_greedy_distance(capacity_split))

