import matplotlib.pyplot as plt
from annealing import data_manager

x = []
y = []


def x_y_arrays(array_list):
    global x, y
    x_y_arr = []
    for i in range(0, len(array_list)):
        x_y_arr.append(data_manager.get_column_from_2d(array_list[i], 0))

    for i in range(0, len(array_list)):
        x_arr = []
        y_arr = []
        for element in array_list[i]:
            x_arr.append(element[0])
            y_arr.append(element[1])
        # x_arr.append(0)
        # y_arr.append(0)
        x.append(x_arr)
        y.append(y_arr)


def draw_plot(array_list):
    x_y_arrays(array_list)
    for i in range(0, len(x)):
        plt.plot(x[i],y[i],'-o')
    plt.show()
