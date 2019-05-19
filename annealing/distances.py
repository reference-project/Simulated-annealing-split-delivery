import math
from annealing import data_manager


class Distances:
    manager = data_manager.DataManager()

    @staticmethod
    def two_points_distance(x0, x1, y0, y1):
        return math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)

    def calculate_route(self, route_arr):
        whole_distance = 0
        route_arr_cp = route_arr.copy()
        route_arr_cp = [[0, 0]] + route_arr_cp + [[0, 0]]
        for i in range(0, len(route_arr_cp) - 1):
            whole_distance += self.two_points_distance(route_arr_cp[i][0], route_arr_cp[i + 1][0], route_arr_cp[i][1],
                                                       route_arr_cp[i + 1][1])
        return whole_distance

    def calculate_array_of_routes(self, solutions):
        whole_distances = []
        for solution in solutions:
            whole_route = self.calculate_route(solution)
            whole_distances.append(whole_route)
        return whole_distances

    def sd_calculate_route_no_cap(self, route_arr):
        whole_distance = 0
        for single_route in route_arr:
            whole_distance += self.calculate_route(single_route)
        return whole_distance

    def sd_calculate_array_of_routes_no_cap(self, solutions):
        whole_distances = []
        for solution in solutions:
            whole_route = self.sd_calculate_route_no_cap(solution)
            whole_distances.append(whole_route)
        return whole_distances

    def sd_calculate_route(self, route_arr):
        whole_distance = 0
        for single_route in route_arr:
            distance_no_cap = self.manager.get_column_from_2d(single_route, 0)
            whole_distance += self.calculate_route(distance_no_cap)
        return whole_distance
