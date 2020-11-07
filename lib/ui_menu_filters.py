from lib.ui_base import prompt_continue, prompt, prompt_range
from lib.filters import filters_to_descriptions, filter_data, add_filter_scalar, add_filter_species, remove_filter
from lib.data import bacteria_species


def display_filters_menu(state, menu):
    prompt(menu, filters_to_descriptions(state.filters))

def display_filters_add_menu(state, menu):
    prompt(menu, filters_to_descriptions(state.filters))

def display_filters_add_scalar_menu(state, filters_menu, scalar_getter, scalar_name):
    (min, max) = prompt_range()
    add_filter_scalar(state.filters, scalar_getter, scalar_name, min, max)
    
    state.filtered_data = filter_data(state.filters, state.raw_data)
    
    display_filters_menu(state, filters_menu)


def display_filters_add_species_menu(state, filters_menu):
    add_filter_func = lambda i: lambda: add_filter_species(state.filters, i)
    options = [(s, add_filter_func(i)) for i, s in bacteria_species.items()]
    
    prompt(options, 
           filters_to_descriptions(state.filters), 
           msg="Choose species to include")
    
    state.filtered_data = filter_data(state.filters, state.raw_data)
    
    display_filters_menu(state, filters_menu)


def display_filters_remove_menu(state, filters_menu):
    #NOTE: Capturing index as parameter to avoid closure in second lambda
    remove_filter_func = lambda i: lambda: remove_filter(state.filters, i)
    descriptions = filters_to_descriptions(state.filters)
    
    if len(descriptions) == 0:
        prompt_continue("No filters to remove - press enter to continue...")
        
        display_filters_menu(state, filters_menu)
        return

    options = [(desc, remove_filter_func(i)) for i, desc in enumerate(descriptions)]
    prompt(options, msg="Choose filter to remove")

    state.filtered_data = filter_data(state.filters, state.raw_data)

    display_filters_menu(state, filters_menu)