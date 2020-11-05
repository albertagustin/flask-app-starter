import json
import os

""" Helper functions for fixtures """


# helper function to load json file
def parse_json_file(file_path):
    with open(os.path.abspath(file_path), 'r') as file:
        record = json.load(file)
    return record
