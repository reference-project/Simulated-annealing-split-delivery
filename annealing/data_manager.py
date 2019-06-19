def read_data_set(input_file, delimiter):
    retrieved_data = []
    data_in = open(input_file, "r")
    for f in data_in:
        spl = f.rstrip('\n').split(delimiter)
        retrieved_data.extend([[int(x) for x in spl]])
    return retrieved_data

def write_data(name, input_data):
    print(name)
    f = open(str(name) + ".csv", "w")
    for i in range(len(input_data)):
        space = ";"
        for j in range(0, len(input_data[i])):
            if j == len(input_data[i]) - 1:
                space = "\n"
            else:
                input_data[i][j] = input_data[i][j]
            if i == 0:
                input_data[i][j] = input_data[i][j]
            f.write(str(input_data[i][j]) + space)
    f.close()


def last_value_split(arr_list):
    new_arr_list = []
    for arr in arr_list:
        arr_len = len(arr) - 1
        arr = [arr[:arr_len], arr[arr_len]]
        new_arr_list.append(arr)
    return new_arr_list


def last_values_sum(array_list, arr):
    cap_idx = len(arr[0]) - 1
    capacities_sum = arr[cap_idx]
    for element in array_list:
        capacities_sum += element[cap_idx]
    return capacities_sum


def get_column_from_2d(array2D, column):
    arr = []
    for element in array2D:
        arr.append(element[column])
    return arr


def get_column_from_3d(array3D, column):
    arr = []
    for array2D in array3D:
        arr.append(get_column_from_2d(array2D, column))
    return arr


def get_column_from_4d(array4D, column):
    columns_list_arr = []
    for array3D in array4D:
        column_arr = get_column_from_3d(array3D, column)
        columns_list_arr.append(column_arr)
    return columns_list_arr
