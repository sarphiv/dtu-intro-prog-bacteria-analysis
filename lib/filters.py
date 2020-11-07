from lib.ui_utilities import check_data_unavailable, inform_if_data_unavailable
from lib.statistics import get_temperature, get_growth_rate, get_species
from lib.data import bacteria_species

import numpy as np


def empty_filter():
    return [[], []]

def filters_to_array(filters):
    return [*filters[0], *filters[1]]

def filters_to_descriptions(filters):
    return [description for _, description in filters_to_array(filters)]


def filter_data(filters, data):
    if check_data_unavailable(data):
        return []

    #AND all filter groups together
    #species filter group is inclusive inside of group (OR species together)
    scalar_indexes = np.ones(len(data), dtype=bool)
    for filter, _ in filters[0]:
        scalar_indexes &= filter(data)
    
    if len(filters[1]) > 0:
        species_indexes = np.zeros(len(data), dtype=bool)
        for filter, _ in filters[1]:
            species_indexes |= filter(data)
    else:
        species_indexes = np.ones(len(data), dtype=bool)


    return data[scalar_indexes & species_indexes]


def remove_filter(filters, index):
    len_scalar_group = len(filters[0])
    if (index < len_scalar_group):
        del filters[0][index]
    else:
        del filters[1][index - len_scalar_group]



def add_filter_scalar(filters, scalar_getter, scalar_name, min, max):
    filters[0].append((
        lambda data: filter_scalar(scalar_getter(data), min, max),
        f"Filtering for {scalar_name} in the range [{min}, {max}["))

def filter_scalar(scalar_data, min, max):
    return (min <= scalar_data) & (scalar_data < max)


def add_filter_temperature(filters, min, max):
    add_filter_scalar(filters, get_temperature, "temperatures", min, max)
    # filters[0].append((
    #     lambda data: filter_temperature(data, min, max),
    #     f"Filtering for temperatures in the range [{min}, {max}["))
    
# def filter_temperature(data, min, max):
#     temperatures = get_temperature(data)

#     return (min <= temperatures) & (temperatures < max)


def add_filter_growth_rate(filters, min, max):
    add_filter_scalar(filters, get_growth_rate, "growth rates", min, max)
    # filters[0].append((
    #     lambda data: filter_growth_rate(data, min, max),
    #     f"Filtering for growth rates in the range [{min}, {max}["))
    
# def filter_growth_rate(data, min, max):
#     growth_rates = get_growth_rate(data)

#     return (min <= growth_rates) & (growth_rates < max)


def add_filter_species(filters, species):
    filters[1].append((
        lambda data: filter_species(data, species),
        f"Filtering for the species {bacteria_species[species]}"))
    
def filter_species(data, species):
    return get_species(data) == species