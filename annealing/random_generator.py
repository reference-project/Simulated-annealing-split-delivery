from random import randint
from annealing import data_manager


class RandomGenerator:
    manager = data_manager.DataManager()

    @staticmethod
    def get_random_index(arr):
        try:
            randint(0, len(arr) - 1)
        except ValueError:
            print("out of range", arr)
        return randint(0, len(arr) - 1)

    def random_solution(self, list_arr):
        solution = []
        for i in range(0, len(list_arr)):
            random_idx = self.get_random_index(list_arr)
            solution.append(list_arr[random_idx])
            del list_arr[random_idx]
        return solution

    def random_solution_generator(self, list_arr, solutions_no):
        solutions = []
        for i in range(0, solutions_no):
            rand_solution = self.random_solution(list_arr.copy())
            solutions.append(rand_solution)
        return solutions

    def sd_random_capacity_generator(self, list_arr, capacity):
        capacity_solution = []
        tries = 0
        for i in range(0, len(list_arr)):
            random_idx = self.get_random_index(list_arr)
            if self.manager.last_values_sum(capacity_solution, list_arr[random_idx]) <= capacity:
                capacity_solution.append(list_arr[random_idx])
                del list_arr[random_idx]
            else:
                tries += 1
            if tries == 3:
                break
        return capacity_solution

    @staticmethod
    def remove_elements_from_arr(array, elements_to_remove):
        for element in elements_to_remove:
            array.remove(element)
        return array

    def sd_random_solution(self, list_arr, capacity):
        solution = []
        while len(list_arr) != 0:
            solution_part = self.sd_random_capacity_generator(list_arr.copy(), capacity)
            list_arr = self.remove_elements_from_arr(list_arr, solution_part)
            solution.append(solution_part)
        return solution

    def sd_random_solutions(self, list_arr, capacity, solutions_no):
        solutions = []
        for i in range(0, solutions_no):
            solution = self.sd_random_solution(list_arr.copy(), capacity)
            if solution:
                solutions.append(solution)
        # solutions = [[[[[2, 3], 8], [[2, 14], 1]], [[[7, 7], 7], [[1, 2], 3]], [[[3, 9], 2], [[7, 6], 8]]], [[[[1, 2], 3], [[3, 9], 2], [[2, 14], 1]], [[[2, 3], 8]], [[[7, 6], 8]], [[[7, 7], 7]]]]
        return solutions
