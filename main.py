#%%
from lib.utilities import eprint
from lib.data import file_exists, dataLoad
from lib.statistics import dataStatistics, statistic_descriptions
from lib.plot import dataPlot
from lib.ui import prompt

from sys import exit

"""
NOTE: Errors, warnings, and notes are output to stderr as usual so make sure you can read stderr.
NOTE: Some functions do not adhere to PEP-8. 
      The names and parameters are part of an interface specification not adhering to PEP-8.
      Function docstrings attempt adherence to PEP-257.

"""



"""
TODO: Write function documentation

"""


file_path = "dataset.txt"
if file_exists(file_path):
    data = dataLoad(file_path)
else:
    print("nope")



def display_main_menu():
    prompt(main_menu)


def display_statistics_menu():
    prompt(statistics_menu)

def display_statistic(statistic):
    stat_key = statistic.casefold()

    print(statistic_descriptions[stat_key])
    print(f"{statistic}: {dataStatistics(data, stat_key)}")

    input("\nPress enter to continue...")
    #Go back to statistics menu
    display_statistics_menu()


def display_plots():
    print("Close plots window to continue...", end="\n\n")
    dataPlot(data)


main_menu = [
    ("Load data", None),
    ("Filter data", None),
    ("Display statistics", display_statistics_menu),
    ("Generate plots", display_plots),
    ("Quit", exit),
]

statistics_menu = [
    ("Mean temperature",      lambda: display_statistic("Mean temperature")),
    ("Mean growth rate",      lambda: display_statistic("Mean growth rate")),
    ("Std temperature",       lambda: display_statistic("Std temperature")),
    ("Std growth rate",       lambda: display_statistic("Std growth rate")),
    ("Rows",                  lambda: display_statistic("Rows")),
    ("Mean cold growth rate", lambda: display_statistic("Mean cold growth rate")),
    ("Mean hot growth rate",  lambda: display_statistic("Mean hot growth rate")),
    ("Back", display_main_menu)
]



try:
    while True:
        display_main_menu()
except SystemExit:
    pass

