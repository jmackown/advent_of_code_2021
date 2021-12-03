from collections import OrderedDict


def get_test_data(test_list):

    input = OrderedDict()

    for i, line in enumerate(test_list):
        input[i] = line.strip()

    return input
