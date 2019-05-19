import random
import math
import numpy
from annealing import random_generator, distances, data_manager, split_delivery
import copy

temperature = 100
capacity = 10
generator = random_generator.RandomGenerator()
distance = distances.Distances()
delivery = split_delivery.SplitDelivery()
manager = data_manager.DataManager()


def get_data():
    file = data_manager.DataManager()
    return file.read_data_set("../coordinates.csv", ";")


def calculate_energy(defender, challenger):
    return defender - challenger


def get_absolute_difference(x0, x1):
    return abs(x0 - x1)


def get_differences_arr(whole_distances):
    differences_arr = []
    for i in range(0, len(whole_distances) - 1):
        absolute_difference = get_absolute_difference(whole_distances[i], whole_distances[i + 1])
        differences_arr.append(absolute_difference)
    return differences_arr


def get_average(arr):
    return numpy.average(arr)


def set_starting_temperature(random_solutions):
    global temperature
    whole_distances = distance.sd_calculate_array_of_routes_no_cap(random_solutions)
    differences_arr = get_differences_arr(whole_distances)
    average_difference = get_average(differences_arr)
    temperature = average_difference


def swap_arr_values(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr


def get_changed_route(array):
    rand_idx = generator.get_random_index(array)
    rand_idx2 = generator.get_random_index(array)
    while rand_idx2 == rand_idx:
        rand_idx2 = generator.get_random_index(array)
    return swap_arr_values(array, rand_idx, rand_idx2)


def acceptance_probability(energy):
    power_value = -abs(energy / temperature)
    return math.exp(power_value)


def annealing(init_solution):
    defender_energy = -distance.sd_calculate_route(init_solution)
    swap_solution_cp = copy.deepcopy(init_solution)
    swap_solution = delivery.get_changed_route(swap_solution_cp, capacity)
    challenger_energy = -distance.sd_calculate_route(swap_solution)
    energy_difference = challenger_energy - defender_energy
    random_val = random.random()
    if energy_difference > 0:
        return swap_solution
    elif acceptance_probability(energy_difference) > random_val:
        return swap_solution
    else:
        return init_solution


def annealing_init(capacity_split):
    global temperature
    random_solutions = generator.sd_random_solutions(list_arr=capacity_split, capacity=capacity, solutions_no=100)
    random_solutions_no_cap = manager.get_column_from_4d(random_solutions.copy(), 0)
    set_starting_temperature(random_solutions_no_cap)
    starting_solution = random_solutions[0]
    print(starting_solution)
    while temperature > 0.5:
        starting_solution = annealing(starting_solution)
        temperature *= 0.99
    print(starting_solution)
    print(distance.sd_calculate_route(starting_solution))


def main():
    coordinates_pack = get_data()
    capacity_split = data_manager.DataManager().last_value_split(coordinates_pack)
    annealing_init(capacity_split)


if __name__ == '__main__':
    main()
