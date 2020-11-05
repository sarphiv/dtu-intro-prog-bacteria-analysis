from lib.data import bacteria_species

#Isolate temperature from each row
get_temperature = lambda data: data[:, 0]
#Isolate growth rate from each row
get_growth_rate = lambda data: data[:, 1]
#Isolate species from each row
get_species     = lambda data: data[:, 2]


#Dictionary mapping from statistic operation name to function
statistic_functions = {
    #Get mean of temperature
    "mean temperature":       lambda data: 
        get_temperature(data).mean(),

    #Get mean of growth rate
    "mean growth rate":       lambda data: 
        get_growth_rate(data).mean(),

    #Get standard deviation of temperature
    "std temperature":        lambda data: 
        get_temperature(data).std(),

    #Get standard deviation of growth rate
    "std growth rate":        lambda data: 
        get_growth_rate(data).std(),

    #Get length of first dimension (rows) of data
    "rows":                   lambda data: data.shape[0],

    #Get mean growth rate of rows with temperature below 20
    "mean cold growth rate":  lambda data: 
        dataStatistics(
            data[get_temperature(data) < 20],
            "mean growth rate"
        ),

    #Get mean growth rate of rows with temperature above 50
    "mean hot growth rate":   lambda data: 
        dataStatistics(
            data[get_temperature(data) > 50],
            "mean growth rate"
        ),

    #Data keyed by species
    "data by species":        lambda data: { 
            species: data[get_species(data) == species]
            for species in bacteria_species.keys()
        },
    
    #Amount of each species keyed by species {species: number}
    "rows by species":        lambda data: { 
            species: dataStatistics(entries, "rows")
            for species, entries in dataStatistics(data, "data by species").items()
        },

    #Temperature keyed by species
    "temperature by species": lambda data: { 
            species: get_temperature(entries)
            for species, entries in dataStatistics(data, "data by species").items()
        },

    #Growth rate keyed by species
    "growth rate by species": lambda data: { 
            species: get_growth_rate(entries)
            for species, entries in dataStatistics(data, "data by species").items()
        },
    #Temperature and growth rate keyed by species
    "temperature and growth rate by species": lambda data: { 
            species: entries[:, 0:2]
            for species, entries in dataStatistics(data, "data by species").items()
        },
}


def dataStatistics(data, statistic):
    """
    Calculate statistics on the provided data and returns the result.
    The statistic should be given as a string being one of (case sensitive):
        "mean temperature",
        "mean growth rate",
        "std temperature",
        "std growth rate",
        "rows",
        "mean cold growth rate",
        "mean hot growth rate",
        "data by species",
        "rows by species",
        "temperature by species",
        "growth rate by species",
        "temperature and growth rate by species"
    """
    #Get appropriate statistic function with string.
    # Apply function on data entries
    return statistic_functions[statistic](data)