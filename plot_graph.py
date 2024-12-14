import matplotlib.pyplot as plt


def plt_graph(x, y, f, f_est, x_int):
    x_name = input("Please type the name of your input:")
    y_name = input("Please type the name of target:")

    fig = plt.figure()
    ax = fig.add_axes([0.14, 0.14, 0.75, 0.75])

    ax.set_title("{} Prediction".format(y_name), color='blue')
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    plt.scatter(x, y, marker='x', c='r', label='data points')
    plt.plot(x, f, label='model function')
    plt.scatter(x_int, f_est, marker='o', c='yellow', edgecolor='black', s=75, label='prediction point')
    plt.text(x_int, round(f_est, 5), f'({x_int}, {round(f_est, 3)})', verticalalignment='bottom',
             horizontalalignment='right')
    print("Target Prediction:", f_est,"$")
    plt.legend()
    plt.show()
