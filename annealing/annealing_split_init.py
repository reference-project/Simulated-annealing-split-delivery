import random
from annealing import random_generator, distances, data_manager, split_delivery, stimulated_annealing
import copy
from greedy import greedy

temperature = 0
capacity = 12
route_distance = 0

sol_dist_arr = []
init_arr = []


def get_data():
    return data_manager.read_data_set("../random_coordinates.csv", ";")


def set_starting_temperature(random_solutions):
    global temperature
    whole_distances = distances.sd_calculate_array_of_routes_no_cap(random_solutions)
    differences_arr = stimulated_annealing.get_differences_arr(whole_distances)
    temperature = stimulated_annealing.get_average(differences_arr)


def annealing(init_solution):
    defender_energy = -greedy.get_greedy_distance_whole(init_solution)
    swap_solution_cp = copy.deepcopy(init_solution)
    swap_solution = split_delivery.get_changed_route(swap_solution_cp, capacity)
    challenger_energy = -greedy.get_greedy_distance_whole(swap_solution)
    energy_difference = challenger_energy - defender_energy
    if energy_difference > 0:
        return swap_solution
    elif stimulated_annealing.acceptance_probability(energy_difference) > random.random():
        return swap_solution
    else:
        return init_solution


def annealing_init(capacity_split):
    best_of_random = -1
    random_solutions = random_generator.sd_random_solutions(list_arr=capacity_split, capacity=capacity,
                                                            solutions_no=100)
    random_solutions_no_cap = data_manager.get_column_from_4d(random_solutions.copy(), 0)
    set_starting_temperature(random_solutions_no_cap)
    best_solution = copy.deepcopy(random_solutions[0])
    for i in range(0, len(random_solutions[0]) * 7 - 1):
        init_temp = temperature
        starting_solution = random_solutions[i]
        while init_temp > 0.5:
            starting_solution = annealing(starting_solution)
            init_temp *= 0.99
        if greedy.get_greedy_distance_whole(starting_solution) < greedy.get_greedy_distance_whole(best_solution):
            best_solution = starting_solution[:]
            best_of_random = i
    output(random_solutions[best_of_random], "initial distance")
    return best_solution


def output(solution, message):
    global init_arr
    annealing_result = get_annealing_route(solution)
    print(annealing_result)
    print(message, route_distance)
    init_arr.append(route_distance)
    from plot import draw_plot
    draw_plot.draw_plot(annealing_result)


def single_annealing_route(data_with_cap):
    get_only_coordinates = data_manager.get_column_from_2d(data_with_cap, 0)
    return stimulated_annealing.clean_annealing(get_only_coordinates)


def get_annealing_route(data_with_cap):
    global route_distance
    route_distance = 0
    route = []
    for element in data_with_cap:
        route_arr = single_annealing_route(element)
        route_distance += distances.calculate_route(route_arr)
        route_arr = [[0, 0]] + route_arr + [[0, 0]]
        route.append(route_arr)
    return route


def random_solutions():
    global init_arr, sol_dist_arr
    import random
    for i in range(0, 10):
        points_no = random.randint(2, 75)
        arr = []
        for i in range(0, points_no):
            x = random.randint(1, 70)
            y = random.randint(1, 70)
            capacity_init = random.randint(1, 12)
            arr.append([x, y, capacity_init])
        data_manager.write_data("../random_coordinates", arr)
        main()
        sol_dist_arr.append(init_arr)
        init_arr = []

    for element in sol_dist_arr:
        print(element[0], element[1])


def main():
    coordinates_pack = get_data()
    capacity_split = data_manager.last_value_split(coordinates_pack)
    solution = annealing_init(capacity_split)
    output(solution, "solution distance")



if __name__ == '__main__':
    random_solutions()
