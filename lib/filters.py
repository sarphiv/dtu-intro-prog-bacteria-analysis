from lib.ui_utilities import check_data_unavailable
from lib.statistics import get_temperature, get_growth_rate, get_species
from lib.data import bacteria_species

import numpy as np


class Filters:
    """
    A DTO for the two types of filters.
    
    Initialized to not contain any filters.
    """
    
    def __init__(self):
        self.scalars = []
        self.species = []


    def as_array(self):
        return [*self.scalars, *self.species]

    def as_descriptions(self):
        return [description for _, description in self.as_array()]


    def filter_data(self, data):
        if check_data_unavailable(data):
            return []

        #AND all filter groups together
        #species filter group is inclusive inside of group (OR species together)
        scalar_indexes = np.ones(len(data), dtype=bool)
        for filter, _ in self.scalars:
            scalar_indexes &= filter(data)
        
        if len(self.species) > 0:
            species_indexes = np.zeros(len(data), dtype=bool)
            for filter, _ in self.species:
                species_indexes |= filter(data)
        else:
            species_indexes = np.ones(len(data), dtype=bool)


        return data[scalar_indexes & species_indexes]


    def remove(self, index):
        len_scalar_group = len(self.scalars)
        
        if (index < len_scalar_group):
            del self.scalars[index]
        else:
            del self.species[index - len_scalar_group]


    @staticmethod
    def filter_scalar(scalar_data, min, max):
        return (min <= scalar_data) & (scalar_data < max)
    
    def add_filter_scalar(self, scalar_getter, scalar_name, min, max):
        self.scalars.append((
            lambda data: Filters.filter_scalar(scalar_getter(data), min, max),
            f"Filtering for {scalar_name} in the range [{min}, {max}["))

    def add_filter_temperature(self, min, max):
        self.add_filter_scalar(get_temperature, "temperatures", min, max)

    def add_filter_growth_rate(self, min, max):
        self.add_filter_scalar(get_growth_rate, "growth rates", min, max)


    @staticmethod
    def filter_species(data, species):
        return get_species(data) == species
    
    def add_filter_species(self, species):
        self.species.append((
            lambda data: Filters.filter_species(data, species),
            f"Filtering for the species {bacteria_species[species]}"))
