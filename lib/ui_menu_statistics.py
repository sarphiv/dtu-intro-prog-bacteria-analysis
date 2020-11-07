from lib.ui_base import prompt_continue, prompt
from lib.ui_utilities import inform_if_data_unavailable
from lib.filters import filters_to_descriptions
from lib.statistics import statistic_descriptions, dataStatistics


def display_statistics_menu(state, menu):
    if inform_if_data_unavailable(state.filtered_data):
        return
    
    prompt(menu, filters_to_descriptions(state.filters))


def display_statistic(state, statistics_menu, statistic):
    stat_key = statistic.casefold()

    print(statistic_descriptions[stat_key])
    print(f"{statistic}: {dataStatistics(state.filtered_data, stat_key)}")

    prompt_continue(start_newline=True)
    #Go back to statistics menu
    display_statistics_menu(state, statistics_menu)