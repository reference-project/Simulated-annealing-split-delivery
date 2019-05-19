import annealing.distances as distance


class Greedy(object):
    distance = distance.Distances()

    def get_smallest_idx(self, arr):
        arr = []
        return arr.index(min(arr))

    def greedy_algorithm(self, coordinates_pack):
        route_arr = [[0, 0]]
        for i in range(0, len(coordinates_pack)):
            last_route_arr_idx = len(route_arr) - 1
            coordinates_distances = distance.get_distance_arr(coordinates_pack, route_arr[last_route_arr_idx])
            smallest_idx = self.get_smallest_idx(coordinates_distances)
            route_arr.append(coordinates_pack[smallest_idx])
            del coordinates_pack[smallest_idx]
        route_arr.append([0, 0])
        return route_arr
