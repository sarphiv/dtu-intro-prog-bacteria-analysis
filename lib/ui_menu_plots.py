from lib.ui_utilities import inform_if_data_unavailable
from lib.plot import dataPlot


def display_plots(state):
    if inform_if_data_unavailable(state.filtered_data):
        return

    print("Close plots window to continue...", end="\n\n")
    dataPlot(state.filtered_data)
