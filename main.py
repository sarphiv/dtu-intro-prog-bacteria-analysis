from lib.state import State
from lib.ui_menu_plots import display_plots
from lib.ui_menu_statistics import display_statistic, display_statistics_menu
from lib.ui_menu_filters import display_filters_add_menu, display_filters_add_scalar_menu, display_filters_add_species_menu, display_filters_menu, display_filters_remove_menu
from lib.ui_menu_data import display_load_data_menu
from lib.ui_menu_main import display_main_menu
from lib.statistics import get_temperature, get_growth_rate
from lib.ui_utilities import display_previous_menu

from sys import exit


"""
NOTE: Errors, warnings, and notes are output to stderr as usual so make sure you can read stderr.
NOTE: Some functions do not adhere to PEP-8. 
      The names and parameters are part of an interface specification not adhering to PEP-8.
NOTE: Function docstrings attempt adherence to PEP-257 (although, a very lousy attempt).

"""



"""
TODO: Describe overall structure of program
TODO: Write function documentation
TODO: Describe why our filter limits are inclusive/exclusive
"""



state = State()



filters_menu = [
    ("Add filter",             lambda: display_filters_add_menu(state, filters_add_menu)),
    ("Remove filter",          lambda: display_filters_remove_menu(state, filters_menu)),
    ("Back",                   display_previous_menu),
]

filters_add_menu = [
    ("Add temperature filter", lambda: display_filters_add_scalar_menu(state, filters_menu, get_temperature, "temperatures")),
    ("Add growth rate filter", lambda: display_filters_add_scalar_menu(state, filters_menu, get_growth_rate, "growth rates")),
    ("Add species filter",     lambda: display_filters_add_species_menu(state, filters_menu))
]

statistics_menu = [
    ("Mean temperature",       lambda: display_statistic(state, statistics_menu, "Mean temperature")),
    ("Mean growth rate",       lambda: display_statistic(state, statistics_menu, "Mean growth rate")),
    ("Std temperature",        lambda: display_statistic(state, statistics_menu, "Std temperature")),
    ("Std growth rate",        lambda: display_statistic(state, statistics_menu, "Std growth rate")),
    ("Rows",                   lambda: display_statistic(state, statistics_menu, "Rows")),
    ("Mean cold growth rate",  lambda: display_statistic(state, statistics_menu, "Mean cold growth rate")),
    ("Mean hot growth rate",   lambda: display_statistic(state, statistics_menu, "Mean hot growth rate")),
    ("Back",                   display_previous_menu)
]


main_menu = [
    ("Load data",              lambda: display_load_data_menu(state)),
    ("Filter data",            lambda: display_filters_menu(state, filters_menu)),
    ("Display statistics",     lambda: display_statistics_menu(state, statistics_menu)),
    ("Generate plots",         lambda: display_plots(state)),
    ("Quit",                   exit),
]



display_main_menu(state, main_menu)
