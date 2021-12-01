import os
from collections import OrderedDict


def get_input():
    input = OrderedDict()

    with open(f"{os.path.dirname(__file__)}/input.txt") as file:
        for i, line in enumerate(file):
            input[i] = int(line.strip())

    return input


def get_basic_increase_count(data):
    total = len(data)
    increase_count = 0
    for i in range(0, total):
        if i > 0 and data[i] > data[i - 1]:
            increase_count += 1

    return increase_count


def get_sliding_increase(data):
    total = len(data)
    increase_count = 0
    for i in range(0, total):
        if i >= 2 and i <= total - 2:
            first_window = data[i] + data[i - 1] + data[i - 2]
            second_window = data[i + 1] + data[i] + data[i - 1]

            if second_window > first_window:
                increase_count += 1
    return increase_count


print(f"puzzle 1 - {get_basic_increase_count(data=get_input())}")
print(f"puzzle 2 - {get_sliding_increase(data=get_input())}")
