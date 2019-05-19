class DataManager(object):
    @staticmethod
    def read_data_set(input_file, delimiter):
        retrieved_data = []
        data_in = open(input_file, "r")
        for f in data_in:
            spl = f.rstrip('\n').split(delimiter)
            retrieved_data.extend([[int(x) for x in spl]])
        return retrieved_data

    @staticmethod
    def last_value_split(arr_list):
        new_arr_list = []
        for arr in arr_list:
            arr_len = len(arr) - 1
            arr = [arr[:arr_len], arr[arr_len]]
            new_arr_list.append(arr)
        return new_arr_list

    @staticmethod
    def last_values_sum(array_list, arr):
        cap_idx = len(arr[0]) - 1
        capacities_sum = arr[cap_idx]
        for element in array_list:
            capacities_sum += element[cap_idx]
        return capacities_sum

    @staticmethod
    def get_column_from_2d(array2D, column):
        arr = []
        for element in array2D:
            arr.append(element[column])
        return arr

    def get_column_from_3d(self, array3D, column):
        arr = []
        for array2D in array3D:
            arr.append(self.get_column_from_2d(array2D, column))
        return arr

    def get_column_from_4d(self, array4D, column):
        columns_list_arr = []
        for array3D in array4D:
            column_arr = self.get_column_from_3d(array3D, column)
            columns_list_arr.append(column_arr)
        return columns_list_arr
