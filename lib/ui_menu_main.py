from lib.ui_base import prompt_options


def display_main_menu(state, menu):
    try:
        while True:
            prompt_options(menu, state.filters.as_descriptions())
            
    except SystemExit:
        pass
