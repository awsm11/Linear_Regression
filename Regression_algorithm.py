import numpy as np
from Reading_excel import data, target_data
from tqdm import tqdm
from plot_graph import plt_graph

# Please have a look at "README" file before running the code and getting more info in detail about the project

x_train = data
y_train = target_data


# error calculator
def cost_function(x, y, w, b):
    m = x_train.shape[0]
    cost_sum = 0
    for i in range(m):
        model_function = w * x[i] + b
        cost = (model_function - y[i]) ** 2
        cost_sum = cost + cost_sum
    total_cost = (1 / (2 * m)) * cost_sum
    return total_cost


def compute_parameters(x1, y1):

    # common w and b ranges and spaces, these values are changeable with respect to data
    w_range = np.array([200-300, 200+300])
    b_range = np.array([-3000, 10000])
    b_space = np.linspace(*b_range, 900)
    w_space = np.linspace(*w_range, 300)

    tmp_b, tmp_w = np.meshgrid(b_space, w_space)
    z = np.zeros_like(tmp_b)

    # iterations
    for i in tqdm(range(tmp_w.shape[0])):
        for j in range(tmp_w.shape[1]):
            z[i, j] = cost_function(x1, y1, tmp_w[i][j], tmp_b[i][j])
    j_min = np.min(z)
    w_count = -1
    b_count = -1
    print("cost:", j_min)
    for i in z:
        w_count += 1
        for j in i:
            b_count += 1
            if j == j_min:
                det_w = w_space[w_count]
                det_b = b_space[b_count - (w_count * 900)]
                print("Parameters, w :{} and b : {}".format(det_w, det_b))

    # the model function
    f = det_w * x1 + det_b

    x_int = float(input("Please enter the value you want to find out its result:"))
    f_est = det_w * x_int + det_b

    plt_graph(x1, y1, f, f_est, x_int)


# commit x and y values
compute_parameters(x_train, y_train)
