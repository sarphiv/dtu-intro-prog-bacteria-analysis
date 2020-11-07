from lib.ui_base import prompt_continue
from lib.data import file_exists, dataLoad

from os import getcwd, path


def display_load_data_menu(state):
    print("Input data file path:")
    data_path = input(getcwd() + path.sep)
    
    if file_exists(data_path):
        print("Loading data...")
        state.raw_data = dataLoad(data_path)
        print("Loaded data")

        state.filtered_data = state.filters.apply(state.raw_data)

        prompt_continue()
    else:
        prompt_continue("Path does not lead to a file - press enter to continue...", start_newline=True)
