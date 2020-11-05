#%%
from lib.utilities import eprint
from lib.data import file_exists, dataLoad
from lib.statistics import statistic_functions

from os import getcwd

"""
NOTE: Errors, warnings, and notes are output to stderr as usual so make sure you can read stderr.
NOTE: Some functions do not adhere to PEP-8. 
      The names and parameters are part of an interface specification not adhering to PEP-8.
      Function docstrings attempt adherence to PEP-257.

"""



"""
TODO: Write function documentation
"""

#%%
file_path = "dataset.txt"
if file_exists(file_path):
      data = dataLoad(file_path)
else:
      print("nope")
#%%
print(statistic_functions["mean hot growth rate"](data))

# %%
