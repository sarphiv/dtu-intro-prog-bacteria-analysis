from lib.ui_base import prompt


def display_main_menu(state, menu):
    try:
        while True:
            prompt(menu, state.filters.as_descriptions())
            
    except SystemExit:
        pass
