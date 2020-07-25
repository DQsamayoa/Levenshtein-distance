__all__ = ['levenshtein.py']

# Defining the modules to import
from .levenshtein import *

Levenshtein = levenshtein.Levenshtein

# Defining variables to import
import os
import json

this_dir, this_filename = os.path.split(__file__)
data_path = os.path.join(this_dir, "data", "alphabet.json")

with open(data_path) as json_file:
    alphabet_json = json.load(json_file)

del data_path
del this_dir
del this_filename