import os
import json

# Defining the modules to import
from .levenshtein import *

# Defining functions to import
Levenshtein = levenshtein.Levenshtein

# Defining variables to import
tmp_this_dir, tmp_this_filename = os.path.split(__file__)
tmp_data_path = os.path.join(tmp_this_dir, "data", "alphabet.json")

with open(tmp_data_path) as json_file:
    alphabet_json = json.load(json_file)

# Deleting temporary variables
del tmp_data_path
del tmp_this_dir
del tmp_this_filename