from random import randint
from annealing import data_manager


def get_random_index(arr):
    return randint(0, len(arr) - 1)


def random_solution(list_arr):
    solution = []
    for i in range(0, len(list_arr)):
        random_idx = get_random_index(list_arr)
        solution.append(list_arr[random_idx])
        del list_arr[random_idx]
    return solution


def random_solution_generator(list_arr, solutions_no):
    solutions = []
    for i in range(0, solutions_no):
        rand_solution = random_solution(list_arr.copy())
        solutions.append(rand_solution)
    return solutions


def sd_random_capacity_generator(list_arr, capacity):
    capacity_solution = []
    tries = 0
    for i in range(0, len(list_arr)):
        random_idx = get_random_index(list_arr)
        if data_manager.last_values_sum(capacity_solution, list_arr[random_idx]) <= capacity:
            capacity_solution.append(list_arr[random_idx])
            del list_arr[random_idx]
        else:
            tries += 1
        if tries == 3:
            break
    return capacity_solution


def remove_elements_from_arr(array, elements_to_remove):
    for element in elements_to_remove:
        array.remove(element)
    return array


def sd_random_solution(list_arr, capacity):
    solution = []
    while len(list_arr) != 0:
        solution_part = sd_random_capacity_generator(list_arr.copy(), capacity)
        list_arr = remove_elements_from_arr(list_arr, solution_part)
        solution.append(solution_part)
    return solution


def sd_random_solutions(list_arr, capacity, solutions_no):
    solutions = []
    for i in range(0, solutions_no):
        solution = sd_random_solution(list_arr.copy(), capacity)
        if solution:
            solutions.append(solution)
    return solutions
