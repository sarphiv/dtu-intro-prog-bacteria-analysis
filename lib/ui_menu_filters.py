from lib.ui_base import prompt_continue, prompt_options, prompt_range
from lib.data import bacteria_species


def display_filters_menu(state, menu):
    prompt_options(menu, state.filters.as_descriptions())

def display_filters_add_menu(state, menu):
    prompt_options(menu, state.filters.as_descriptions())

def display_filters_add_scalar_menu(state, filters_menu, scalar_getter, scalar_name):
    (min, max) = prompt_range()
    state.filters.add_filter_scalar(scalar_getter, scalar_name, min, max)
    
    state.filtered_data = state.filters.apply(state.raw_data)
    
    display_filters_menu(state, filters_menu)


def display_filters_add_species_menu(state, filters_menu):
    add_filter_func = lambda id: lambda: state.filters.add_filter_species(id)
    options = [(s, add_filter_func(id)) for id, s in bacteria_species.items()]
    
    prompt_options(options, 
                   state.filters.as_descriptions(), 
                   msg="Choose species to include")
    
    state.filtered_data = state.filters.apply(state.raw_data)
    
    display_filters_menu(state, filters_menu)


def display_filters_remove_menu(state, filters_menu):
    #NOTE: Capturing index as parameter to avoid closure in second lambda
    remove_filter_func = lambda i: lambda: state.filters.remove(i)
    descriptions = state.filters.as_descriptions()
    
    if len(descriptions) == 0:
        prompt_continue("No filters to remove - press enter to continue...")
        
        display_filters_menu(state, filters_menu)
        return

    options = [(desc, remove_filter_func(i)) for i, desc in enumerate(descriptions)]
    prompt_options(options, msg="Choose filter to remove")

    state.filtered_data = state.filters.apply(state.raw_data)

    display_filters_menu(state, filters_menu)