import os
from collections import OrderedDict


def get_input_path(file_name):
    return f"{os.path.dirname(__file__)}/puzzle_data/{file_name}"


def get_data(file_name):

    input = OrderedDict()

    with open(get_input_path(file_name=file_name)) as file:
        for i, line in enumerate(file):
            input[i] = line.strip()

    return input
