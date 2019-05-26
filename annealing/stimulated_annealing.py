import random
import math
import numpy
from annealing import distances, random_generator

temperature = 100


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


def set_starting_temperature(whole_distances):
    global temperature
    differences_arr = get_differences_arr(whole_distances)
    temperature = get_average(differences_arr)


def swap_arr_values(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr


def get_changed_route(array):
    rand_idx = random_generator.get_random_index(array)
    rand_idx2 = random_generator.get_random_index(array)
    while rand_idx2 == rand_idx:
        rand_idx2 = random_generator.get_random_index(array)
    return swap_arr_values(array, rand_idx, rand_idx2)


def acceptance_probability(energy):
    power_value = energy / temperature
    return math.exp(power_value)


def annealing(init_solution):
    defender_energy = -distances.calculate_route(init_solution)
    swap_solution = get_changed_route(init_solution.copy())
    challenger_energy = -distances.calculate_route(swap_solution)
    energy_difference = challenger_energy - defender_energy
    if energy_difference > 0:
        return swap_solution
    elif acceptance_probability(energy_difference) > random.random():
        return swap_solution
    else:
        return init_solution


def clean_annealing(data):
    global temperature
    random_solutions = random_generator.random_solution_generator(data, solutions_no=100)
    whole_distances = distances.calculate_array_of_routes(random_solutions)
    set_starting_temperature(whole_distances)
    starting_solution = random_solutions[0]
    while temperature > 0.5:
        starting_solution = annealing(starting_solution)
        temperature *= 0.95
    return starting_solution
