import copy
from annealing import random_generator, data_manager
import math

cap1 = 0
cap2 = 0


def calculate_capacity_sum(arr):
    last_val_idx = len(arr[0]) - 1
    return sum(data_manager.get_column_from_2d(arr, last_val_idx))


def can_be_swapped(array1, array2, capacity):
    global cap1, cap2
    cap1 = calculate_capacity_sum(array1)
    cap2 = calculate_capacity_sum(array2)
    if cap1 < capacity or cap2 < capacity:
        return True
    return False


def change_index(idx1, idx2):
    if idx1 < idx2:
        return idx2 - 1
    return idx2


def shift_value(array_list, idx1, idx2, idx_of_idx1):
    item = array_list[idx1][idx_of_idx1]
    array_list[idx1].remove(item)
    array_list[idx2].append(item)
    if len(array_list[idx1]) == 0:
        del array_list[idx1]
    return array_list


def change_or_false(array_list, idx1, idx2, idx_of_idx1, capacity):
    array = copy.deepcopy(array_list)
    move_arr = shift_value(array, idx1, idx2, idx_of_idx1)
    if len(array_list) != len(move_arr):
        idx2 = change_index(idx1, idx2)
    if calculate_capacity_sum(move_arr[idx2]) <= capacity:
        return move_arr
    return False


def move_part(array_list, idx1, idx2, idx_of_idx, capacity, cap_of_arr_no_2):
    array = copy.deepcopy(array_list)
    total_amount_to_add = capacity - cap_of_arr_no_2
    last_idx = len(array[idx1][idx_of_idx]) - 1
    if array[idx1][idx_of_idx][last_idx] > total_amount_to_add != 0:
        amount_left = array[idx1][idx_of_idx][last_idx] - total_amount_to_add
        if amount_left == 0:
            return False
        array[idx1][idx_of_idx][last_idx] = amount_left
        array[idx2].append([array[idx1][idx_of_idx][0], total_amount_to_add])
        return array
    return change_or_false(array_list, idx1, idx2, idx_of_idx, capacity)


def new_single_path(array_list, capacity):
    tries = 0
    while tries <= 2:
        idx1_idx_2 = get_random_arr_indexes(array_list)
        if can_be_swapped(array_list[idx1_idx_2[0]], array_list[idx1_idx_2[1]], capacity):
            if cap1 < capacity:
                idx_of_idx1 = random_generator.get_random_index(array_list[idx1_idx_2[0]])
                change_arr_or_false = move_part(array_list, idx1_idx_2[0], idx1_idx_2[1], idx_of_idx1,
                                                capacity, cap2)
            elif cap2 < capacity:
                idx_of_idx2 = random_generator.get_random_index(array_list[idx1_idx_2[1]])
                change_arr_or_false = move_part(array_list, idx1_idx_2[1], idx1_idx_2[0], idx_of_idx2, capacity, cap1)
            else:
                change_arr_or_false = False
            if change_arr_or_false:
                return change_arr_or_false
        tries += 1
    return array_list


def swap_arr_values(arr, idx1, idx2, idx_lst_1, idx_lst_2):
    arr[idx1][idx_lst_1], arr[idx2][idx_lst_2] = arr[idx2][idx_lst_2], arr[idx1][idx_lst_1]
    return arr


def switch_or_false(arr, idx1, idx2, idx_lst_1, idx_lst_2, capacity):
    arr_cp = copy.deepcopy(arr)
    swap_arr = swap_arr_values(arr_cp, idx1, idx2, idx_lst_1, idx_lst_2)
    if calculate_capacity_sum(swap_arr[idx1]) <= capacity:
        if calculate_capacity_sum(swap_arr[idx2]) <= capacity:
            return swap_arr
    return False


def get_random_arr_indexes(array_list):
    rand_idx = random_generator.get_random_index(array_list)
    rand_idx2 = random_generator.get_random_index(array_list)
    while rand_idx2 == rand_idx:
        rand_idx2 = random_generator.get_random_index(array_list)
    return rand_idx, rand_idx2


def change_values(array_list, capacity):
    tries = 0
    while tries <= 2:
        idx1_idx_2 = get_random_arr_indexes(array_list)
        idx_of_idx1 = random_generator.get_random_index(array_list[idx1_idx_2[0]])
        idx_of_idx2 = random_generator.get_random_index(array_list[idx1_idx_2[1]])
        switch_arr_or_false = switch_or_false(array_list, idx1_idx_2[0], idx1_idx_2[1], idx_of_idx1, idx_of_idx2,
                                              capacity)
        if switch_arr_or_false:
            return switch_arr_or_false
        tries += 1
    return array_list


def how_many_changes(array):
    arr_len = 0
    for elements in array:
        arr_len += len(elements)
    return math.ceil(0.1 * arr_len)


def get_changed_route(array_list, capacity):
    changes_value = how_many_changes(array_list)
    for i in range(0, changes_value):
        array_list = new_single_path(array_list, capacity)
    return array_list
