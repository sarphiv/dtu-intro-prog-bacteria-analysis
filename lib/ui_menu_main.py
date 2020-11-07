from lib.ui_base import prompt
from lib.filters import filters_to_descriptions



def display_main_menu(state, menu):
    try:
        while True:
            prompt(menu, filters_to_descriptions(state.filters))
            
    except SystemExit:
        pass
