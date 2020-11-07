from lib.utilities import eprint
from lib.data import file_exists, dataLoad, bacteria_species
from lib.filters import add_filter_scalar, empty_filter, filters_to_descriptions, filter_data, add_filter_growth_rate, add_filter_species, remove_filter
from lib.statistics import dataStatistics, statistic_descriptions, get_temperature, get_growth_rate
from lib.plot import dataPlot
from lib.ui_base import prompt_continue, prompt, prompt_range
from lib.ui_utilities import inform_if_data_unavailable

from sys import exit
from os import getcwd, path

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

raw_data = None
filtered_data = None

filters = empty_filter()
add_filter_growth_rate(filters, 0.1, 0.6)
add_filter_species(filters, 1)
add_filter_species(filters, 2)


def display_previous_menu():
    pass

def display_main_menu():
    prompt(main_menu, filters_to_descriptions(filters))
    
    
def display_load_data_menu():
    global raw_data
    global filtered_data

    print("Input data file path:")
    data_path = input(getcwd() + path.sep)
    
    if file_exists(data_path):
        print("Loading data...")
        raw_data = dataLoad(data_path)
        print("Loaded data")

        filtered_data = filter_data(filters, raw_data)

        prompt_continue()
    else:
        prompt_continue("Path does not lead to a file - press enter to continue...", start_newline=True)


def display_filters_menu():
    prompt(filters_menu, filters_to_descriptions(filters))

def display_filters_add_menu():
    prompt(filters_add_menu, filters_to_descriptions(filters))

def display_filters_add_scalar_menu(scalar_getter, scalar_name):
    #remember to refilter data and assign it after changing anything
    global filtered_data

    (min, max) = prompt_range()
    add_filter_scalar(filters, scalar_getter, scalar_name, min, max)
    
    filtered_data = filter_data(filters, raw_data)
    
    display_filters_menu()


def display_filters_add_species_menu():
    global filtered_data

    add_filter_func = lambda i: lambda: add_filter_species(filters, i)
    options = [(s, add_filter_func(i)) for i, s in bacteria_species.items()]
    
    prompt(options, 
           filters_to_descriptions(filters), 
           msg="Choose species to include")
    
    filtered_data = filter_data(filters, raw_data)
    
    display_filters_menu()


def display_filters_remove_menu():
    global filtered_data

    #NOTE: Capturing index as parameter to avoid closure in second lambda
    remove_filter_func = lambda i: lambda: remove_filter(filters, i)
    descriptions = filters_to_descriptions(filters)
    
    if len(descriptions) == 0:
        prompt_continue("No filters to remove - press enter to continue...")
        
        display_filters_menu()
        return

    options = [(desc, remove_filter_func(i)) for i, desc in enumerate(descriptions)]
    prompt(options, msg="Choose filter to remove")

    filtered_data = filter_data(filters, raw_data)

    display_filters_menu()


def display_statistics_menu():
    if inform_if_data_unavailable(filtered_data):
        return
    
    prompt(statistics_menu, filters_to_descriptions(filters))

def display_statistic(statistic):
    stat_key = statistic.casefold()

    print(statistic_descriptions[stat_key])
    print(f"{statistic}: {dataStatistics(filtered_data, stat_key)}")

    prompt_continue(start_newline=True)
    #Go back to statistics menu
    display_statistics_menu()


def display_plots():
    if inform_if_data_unavailable(filtered_data):
        return

    print("Close plots window to continue...", end="\n\n")
    dataPlot(filtered_data)



main_menu = [
    ("Load data",          display_load_data_menu),
    ("Filter data",        display_filters_menu),
    ("Display statistics", display_statistics_menu),
    ("Generate plots",     display_plots),
    ("Quit",               exit),
]

filters_menu = [
    ("Add filter",    display_filters_add_menu),
    ("Remove filter", display_filters_remove_menu),
    ("Back",          display_previous_menu),
]

filters_add_menu = [
    ("Add temperature filter", lambda: display_filters_add_scalar_menu(get_temperature, "temperatures")),
    ("Add growth rate filter", lambda: display_filters_add_scalar_menu(get_growth_rate, "growth rates")),
    ("Add species filter",     display_filters_add_species_menu)
]

statistics_menu = [
    ("Mean temperature",      lambda: display_statistic("Mean temperature")),
    ("Mean growth rate",      lambda: display_statistic("Mean growth rate")),
    ("Std temperature",       lambda: display_statistic("Std temperature")),
    ("Std growth rate",       lambda: display_statistic("Std growth rate")),
    ("Rows",                  lambda: display_statistic("Rows")),
    ("Mean cold growth rate", lambda: display_statistic("Mean cold growth rate")),
    ("Mean hot growth rate",  lambda: display_statistic("Mean hot growth rate")),
    ("Back",                  display_previous_menu)
]



try:
    while True:
        display_main_menu()
except SystemExit:
    pass

