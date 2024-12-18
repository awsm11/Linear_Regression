import matplotlib.pyplot as plt
from gd_excel import x_axis, y_axis, n
import numpy as np


def plt_modelfunction(w_model, b_model, population, profit):
    fig = plt.figure()
    ax = fig.add_axes([0.14, 0.14, 0.75, 0.75])

    ax.set_xlabel("Population(10000s)")
    ax.set_ylabel("Profit (10000$)")
    plt.scatter(x_axis, y_axis, marker='x', c='r', label='data points')
    x = np.linspace(2, 30)
    f = w_model * x + b_model
    plt.plot(x, f, label='model function')

    plt.scatter(population, profit, marker='o', c='yellow', edgecolor='black', s=75, label='prediction point')
    plt.text(population, round(profit, 5), f'({population}, {round(profit, 3)})', verticalalignment='bottom',
             horizontalalignment='right')
    plt.legend()
    plt.show()







