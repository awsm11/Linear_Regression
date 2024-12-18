from gd_excel import x_axis, y_axis, n
import numpy as np
from gradient_plot import plt_modelfunction


def cost_function(x, y, w, b):
    total_error = 0

    for i in range(n):
        f_wb = w * x[i] + b
        error = (f_wb - y[i]) ** 2
        total_error += error

    j_wb = (1 / (2 * n)) * total_error
    return j_wb


def compute_gradient(x, y, w, b):
    total_error_w = 0
    total_error_b = 0

    for i in range(n):
        f_wb = w * x[i] + b
        error_w = (f_wb - y[i]) * x[i]
        error_b = f_wb - y[i]
        total_error_w += error_w
        total_error_b += error_b

    dev_jw = (1 / n) * total_error_w
    dev_jb = (1 / n) * total_error_b

    return dev_jw, dev_jb


def gradient_descent(x, y, w_in, b_in, alpha, num_iteration, cost_function, gradient_function):

    j_wb_storage = []
    w_storage = []
    b_storage = []
    w = w_in
    b = b_in
    w_model = []
    b_model = []

    for i in range(num_iteration):
        dev_jw, dev_jb = gradient_function(x, y, w, b)

        w = w - alpha * dev_jw
        b = b - alpha * dev_jb

        j_wb_storage.append(cost_function(x, y, w, b))
        w_storage.append(w)
        b_storage.append(b)

    j_wb_min = np.min(j_wb_storage)

    for i in range(num_iteration):
        if j_wb_storage[i] == j_wb_min:
            w_model = w_storage[i]
            b_model = b_storage[i]
            print("w_model = {} and b_model = {}".format(w_model, b_model))

    population = float(input("Please enter the population:")) / 10000
    profit = w_model * population + b_model
    print("Population: {} and Profit: {}$".format(population * 10000, profit * 10000))

    plt_modelfunction(w_model, b_model, population, profit)


w_in = 0
b_in = 0
num_iteration = 1500
alpha = 0.01

gradient_descent(x_axis, y_axis, w_in, b_in, alpha, num_iteration, cost_function, compute_gradient)


