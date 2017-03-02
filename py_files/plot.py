# python package
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_bar_graph_within(alternative_list, observered_data, result_data, title):
    names = alternative_list

    # counts = data_duration_counts

    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = np.arange(alternative_list.__len__()) * 2
    ax.bar(x, observered_data, align='center', color='red')
    ax.bar(x + 1, result_data, align='center', color='blue')

    red_patch = mpatches.Patch(color='red', label='Observered Value')
    blue_patch = mpatches.Patch(color='blue', label='Estimated Value')

    ax.xaxis.set_major_locator(plt.FixedLocator(x))
    ax.xaxis.set_major_formatter(plt.FixedFormatter(names))
    ax.set_title(title)

    plt.legend(handles=[red_patch, blue_patch])
    plt.show()


    return
