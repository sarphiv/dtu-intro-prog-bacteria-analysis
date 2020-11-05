import matplotlib.pyplot as plt
from lib.statistics import dataStatistics
from lib.data import bacteria_species


axis_label_style = { "fontsize": 12, "fontweight": "bold" }


def draw_bar_plot(fig, key_value):
    #Draw horizontal grid lines
    fig.yaxis.grid(zorder=0)
    
    #Draw bar graph for input data
    fig.bar(
        list(key_value.keys()), 
        list(key_value.values()),
        zorder=2
    )
    
    #Set axis labels
    fig.set_title("Number of bacteria by species", **axis_label_style)
    fig.set_xlabel("Species", **axis_label_style)
    fig.set_ylabel("Number of bacteria", **axis_label_style)

    #Rotate x-axis tick labels
    for label in fig.get_xticklabels():
        label.set_fontsize(9)
        label.set_rotation(16)
        label.set_ha("right")


def draw_line_graph(fig, x, y, color):
    pass


def dataPlot(data):
    fig, (fig_num, fig_growth) = plt.subplots(1, 2)
    fig.subplots_adjust(bottom=0.24)
    fig.set_size_inches(13, 6)

    species_num = dataStatistics(data, "rows by species")
    species_num = { bacteria_species[s]: num for s, num in species_num.items() }

    draw_bar_plot(fig_num, species_num)
    #fig_num.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    #fig_num.axis([0, 6, 0, 20])
    plt.show()

