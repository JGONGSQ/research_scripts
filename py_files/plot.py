# python package
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def plot_bar_graph_within(names, observered_data, result_data, title, fig, sub_plot_index):
    """
    :param names: labels of x-axis
    :param observered_data: as variable name
    :param result_data: as variable name
    :param title: the title of the subplot
    :param fig: the fig object
    :param sub_plot_index: the index number is in order,
        such 221 means the generate a graph has 2 by 2 figure, which could have 4 subplots in it
        the 1 means the first subplot in the figure.
    :return: the fig object
    """
    # define the subplot
    ax = fig.add_subplot(sub_plot_index)

    x = np.arange(names.__len__()) * 2
    # set the value
    ax.bar(x, observered_data, align='center', color='red')
    ax.bar(x + 1, result_data, align='center', color='blue')

    # create the patch
    red_patch = mpatches.Patch(color='red', label='Observed Value')
    blue_patch = mpatches.Patch(color='blue', label='Simulated Value')

    # Set the label x-axis
    ax.xaxis.set_major_locator(plt.FixedLocator(x + 0.5))
    ax.xaxis.set_major_formatter(plt.FixedFormatter(names))
    ax.set_title(title)

    plt.legend(handles=[red_patch, blue_patch])

    return fig
