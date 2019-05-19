import random
import copy
from annealing import random_generator
from annealing import data_manager
import math


class SplitDelivery:
    generator = random_generator.RandomGenerator()
    manager = data_manager.DataManager()

    @staticmethod
    def how_many_changes(array):
        arr_len = 0
        for elements in array:
            arr_len += len(elements)
        return math.ceil(0.1 * arr_len)

    @staticmethod
    def swap_arr_values(arr, idx1, idx2, idx_lst_1, idx_lst_2):
        arr[idx1][idx_lst_1], arr[idx2][idx_lst_2] = arr[idx2][idx_lst_2], arr[idx1][idx_lst_1]
        return arr

    def calculate_capacity_sum(self, arr):
        sum1 = 0
        cap_idx = len(arr[0]) - 1
        for element in arr:
            sum1 += element[cap_idx]
        # capacities_arr = self.manager.get_column_from_2d(arr, cap_idx)
        return sum1

    def is_switchable(self, arr, idx1, idx2, idx_lst_1, idx_lst_2, capacity):
        arr_cp = self.swap_arr_values(arr, idx1, idx2, idx_lst_1, idx_lst_2)
        if self.calculate_capacity_sum(arr_cp[idx1]) <= capacity:
            if self.calculate_capacity_sum(arr_cp[idx2]) <= capacity:
                return arr_cp
        return False

    def change_values(self, array_list, capacity):
        can_swap = False
        tries = 0
        array_list_cp = copy.deepcopy(array_list)
        while can_swap is False:
            rand_idx = self.generator.get_random_index(array_list_cp)
            random_list_idx = self.generator.get_random_index(array_list_cp[rand_idx])
            rand_idx2 = self.generator.get_random_index(array_list_cp)
            while rand_idx2 == rand_idx:
                rand_idx2 = self.generator.get_random_index(array_list_cp)
            random_list_idx2 = self.generator.get_random_index(array_list_cp[rand_idx2])
            can_swap = self.is_switchable(array_list_cp, rand_idx, rand_idx2, random_list_idx, random_list_idx2, capacity)
            if not can_swap:
                tries += 1
                can_swap = array_list
            if tries == 3:
                return array_list_cp
        return can_swap

    def shift_value(self, array_list, idx1, idx2, idx_of_idx1):
        item = array_list[idx1][idx_of_idx1]
        array_list[idx1].remove(item)
        array_list[idx2].append(item)
        if len(array_list[idx1]) == 0:
            del array_list[idx1]
        return array_list

    def is_addable(self, array_list, idx1, idx2, idx_of_idx1, capacity):
        array = copy.deepcopy(array_list)
        some_array = self.shift_value(array, idx1, idx2, idx_of_idx1)
        if len(array_list) != len(some_array):
            if idx1 < idx2:
                idx2 -= 1
        # print(self.calculate_capacity_sum(some_array[idx2]) <= capacity)
        if self.calculate_capacity_sum(some_array[idx2]) <= capacity:
            return True
        return False

    def move_value(self, array_list, capacity):
        can_swap = False
        tries = 0
        while can_swap is False:
            rand_idx = self.generator.get_random_index(array_list)
            random_list_idx = self.generator.get_random_index(array_list[rand_idx])
            rand_idx2 = self.generator.get_random_index(array_list)
            while rand_idx2 == rand_idx:
                rand_idx2 = self.generator.get_random_index(array_list)
            can_swap = self.is_addable(array_list, rand_idx, rand_idx2, random_list_idx, capacity)
            if can_swap:
                array_list = self.shift_value(array_list.copy(), rand_idx, rand_idx2, random_list_idx)
            if not can_swap:
                tries += 1
            if tries == 3:
                break
        return array_list

    def kind_of_change(self, array_list, capacity):
        if random.randint(0, 1) == 1:
            return self.change_values(array_list, capacity)
        else:
            return self.move_value(array_list, capacity)

    def get_changed_route(self, array_list, capacity):
        changes_value = self.how_many_changes(array_list)
        for i in range(0, changes_value):
            array_list = self.kind_of_change(array_list, capacity)
            # array_list = self.change_values(array_list, capacity)
        return array_list
