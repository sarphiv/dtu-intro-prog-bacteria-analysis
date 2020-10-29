from utilities import eprint
import numpy as np
from os.path import exists, isfile


bacteria_species = {
    1: "Salmonella enterica",
    2: "Bacillus cereus",
    3: "Listeria",
    4: "Brochothrix thermosphacta"
}


def file_exists(file_path):
    """
    Returns whether a file path leads to a file
    """
    return not exists(file_path) or not isfile(file_path)


def parse_entry(entry):
    """
    Parses a line string from a dataset and returns an array [temperature, growth_rate, species]
    """
    #Helper functions for returning errors and success
    error = lambda message: (None, message)
    success = lambda entry: (entry, None)


    #Ensure data shape is valid
    parsed = entry.split(' ')
    
    if len(parsed) != 3:
        return error("Entries must have 3 elements separated by spaces")

    [temperature, growth_rate, species] = parsed

    #Parse data types
    try:
        temperature = float(temperature)
        growth_rate = float(growth_rate)
        species = int(species)
    except ValueError:
        return error("Invalid data type on one of the columns")

    #Validate temperature range
    if temperature < 10 or temperature > 60:
        return error("Temperature must be in the range [10; 60]")
    #Validate growth rate range
    if growth_rate <= 0:
        return error("Growth rate must be a positive number")
    if species not in bacteria_species:
        return error("Bacteria species is unknown")


    #Return parsed entry
    return success(np.array([temperature, growth_rate, species]))


def dataLoad(filename):
    """
    Loads data from a file and returns a numpy array with shape (-1,3): [[temperature, growth_rate, species], ...]
    Skips invalid entries and outputs them to stderr.
    """
    
    #Load and immediately close file
    with open(filename, mode='r') as file:
        lines = file.readlines()

    #Parse all data
    data = []
    for i, entry in enumerate(lines):
        #Attempt to parse entry 
        (parsed, error) = parse_entry(entry)
        
        #If parsing of line succeeded, store it
        if error == None:
            data.append(parsed)
        #Else, output failure
        else:
            eprint(f'Failed parsing line {i} with error "{error}" and with data "{entry}"')
            continue


    #Return valid entries
    return np.array(data)

