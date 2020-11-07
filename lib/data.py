from lib.utilities import eprint
import numpy as np
from os.path import exists, isfile


#Define allowed bacteria species
#NOTE: Using dictionary instead of list as it fits the purpose of checking for existence better
# - although at 4 entries a dictionary is much, much slower.
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
    return exists(file_path) and isfile(file_path)


def parse_entry(entry):
    """
    Parses a line string from a dataset and returns ([temperature, growth_rate, species]?, error_msg?).
    If parsing succeeded, the parsed data is provided.
    If parsing failed, an error message is provided.
    """
    #Utility functions for returning success and error
    success = lambda entry: (entry, None)
    error = lambda message: (None, message)


    #Ensure data shape is valid
    parsed = entry.strip().split(' ')
    
    if len(parsed) != 3:
        return error("Entries must have 3 elements separated by spaces")
    
    #Deconstruct list into individual variables
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
    #Validate species
    if species not in bacteria_species:
        return error("Bacteria species is unknown")


    #Return parsed entry
    return success(np.array([temperature, growth_rate, species]))


def dataLoad(filename):
    """
    Loads data from a file and returns a numpy array with shape (-1,3): [[temperature, growth_rate, species], ...]
    Skips invalid entries and outputs them to stderr.
    
    REMARK: Does not check for existence of file. Check before calling this function.
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
            eprint(f'Failed parsing line {i} with error "{error}" and with data "{entry.rstrip()}"')
            continue


    #Return valid entries
    return np.array(data)

