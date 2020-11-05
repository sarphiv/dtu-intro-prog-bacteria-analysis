import matplotlib.pyplot as plt
from lib.statistics import dataStatistics, get_temperature, get_growth_rate
from lib.data import bacteria_species


#Define axis label style for subplots
axis_label_style = { "fontsize": 12, "fontweight": "bold" }


def draw_bar_plot(fig, key_value):
    """
    Draw a bar plot defined by the keys as categories and values as heights.
    """

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
        label.set_rotation(12)


def draw_line_graph(fig, x, y, name):
    """
    Draw a combined point and dashed line graph based on the given points.
    The graph is labeled.
    """
    
    #Draw grid lines
    fig.grid(zorder=0)
    
    #Draw points and grey lines
    fig.plot(x, y, "o", label=name, zorder=2)
    fig.plot(x, y, "k--", label=None, zorder=1)
    
    #Set axis limits
    fig.set_xlim(0, 60)
    fig.set_ylim(0)
    
    #Display legend
    fig.legend()
    
    #Set axis labels
    fig.set_title("Growth rate based on temperature", **axis_label_style)
    fig.set_xlabel("Temperature", **axis_label_style)
    fig.set_ylabel("Growth rate", **axis_label_style)



def dataPlot(data):
    """
    Shows a GUI with number of entries for each species and a growth-temperature plot for each species.
    NOTE: Blocks thread while the GUI is open.
    """

    #Create subplots and setup size
    fig, (fig_num, fig_growth) = plt.subplots(1, 2)
    fig.subplots_adjust(bottom=0.24)
    fig.set_size_inches(13, 6)


    #Get number of entries for each species and transform to key by string name
    species_num = dataStatistics(data, "rows by species")
    species_num = { bacteria_species[s]: num for s, num in species_num.items() }

    #Get temperature and growth data, then sort by temperature
    #NOTE: Sorts by getting a sorted array of indexes for the temperature column,
    # then accesses the original array in the order of the sorted indexes.
    species_temp_grow = dataStatistics(data, "temperature and growth rate by species")
    species_temp_grow = { s: e[e[:, 0].argsort()] for s, e in species_temp_grow.items()}


    #Draw number plot
    draw_bar_plot(fig_num, species_num)
    
    #Draw growth-temperature plots for each species
    for species, entries in species_temp_grow.items():
        draw_line_graph(fig_growth, 
                        x=get_temperature(entries),
                        y=get_growth_rate(entries), 
                        name=bacteria_species[species])


    #Show finished plot
    #NOTE: Blocks thread
    plt.show()
