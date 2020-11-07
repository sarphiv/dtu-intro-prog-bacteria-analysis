from lib.state import State
from lib.ui_menu_plots import display_plots
from lib.ui_menu_statistics import display_statistic, display_statistics_menu
from lib.ui_menu_filters import display_filters_add_menu, display_filters_add_scalar_menu, display_filters_add_species_menu, display_filters_menu, display_filters_remove_menu
from lib.ui_menu_data import display_load_data_menu
from lib.ui_menu_main import display_main_menu
from lib.ui_utilities import display_previous_menu
from lib.statistics import get_temperature, get_growth_rate

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





"""
The program state consists of:
    Raw data loaded in.
    Filtered data of the raw data.
    Active filters.
"""
#Initialize state of program
state = State()


"""
The following section defines the various menus in the program.
The menus are defined as lists of tuples,
where the first element in the tuple is the menu option text,
while the second element in the tuple is the function to call if the option is selected.

The state of the program is passed into each menu together with other required parameters.
A commonly required parameter is the next menu to show 
or the menu to return to after an operation has completed execution.
"""

#Define main filter menu. This is where filters can be added and removed.
filters_menu = [
    #Parameters consist of the program state, and the definition of the menu to show.
    ("Add filter",             lambda: display_filters_add_menu(state, filters_add_menu)),
    ("Remove filter",          lambda: display_filters_remove_menu(state, filters_menu)),
    #Option to return to previous menu
    ("Back",                   display_previous_menu),
]

#Define menu for adding filters.
filters_add_menu = [
    #Parameters consist of 
    # program state, 
    # the definition of the menu to return to after completion,
    # a function to retrieve the scalar to filter out of the data,
    # and the name of the scalar being selected for.
    ("Add temperature filter", lambda: display_filters_add_scalar_menu(state, filters_menu, get_temperature, "temperatures")),
    ("Add growth rate filter", lambda: display_filters_add_scalar_menu(state, filters_menu, get_growth_rate, "growth rates")),
    #Parameters consist of program state, and the definition of the menu to return to after completion
    ("Add species filter",     lambda: display_filters_add_species_menu(state, filters_menu))
]

#Define menu for choosing which statistic to calculate and show.
statistics_menu = [
    #Parameters consist of 
    # program state, 
    # the definition of the menu to return to after completion,
    # and a string describing the statistic being calculated
    ("Mean temperature",       lambda: display_statistic(state, statistics_menu, "Mean temperature")),
    ("Mean growth rate",       lambda: display_statistic(state, statistics_menu, "Mean growth rate")),
    ("Std temperature",        lambda: display_statistic(state, statistics_menu, "Std temperature")),
    ("Std growth rate",        lambda: display_statistic(state, statistics_menu, "Std growth rate")),
    ("Rows",                   lambda: display_statistic(state, statistics_menu, "Rows")),
    ("Mean cold growth rate",  lambda: display_statistic(state, statistics_menu, "Mean cold growth rate")),
    ("Mean hot growth rate",   lambda: display_statistic(state, statistics_menu, "Mean hot growth rate")),
    #Option to return to previous menu
    ("Back",                   display_previous_menu)
]


#Define main menu of the program. This is where the program starts.
main_menu = [
    #Parameters consist of program state and definition of the menu to show.
    # Some options do not have a second parameter,
    # because they do not lead to menus.
    ("Load data",              lambda: display_load_data_menu(state)),
    ("Filter data",            lambda: display_filters_menu(state, filters_menu)),
    ("Display statistics",     lambda: display_statistics_menu(state, statistics_menu)),
    ("Generate plots",         lambda: display_plots(state)),
    #Option to close the program
    ("Quit",                   exit),
]



#At this point, the program state has been initialized
# and all the menus have also been defined.

#Show the main menu
display_main_menu(state, main_menu)
