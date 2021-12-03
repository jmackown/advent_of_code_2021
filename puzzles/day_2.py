from get_input import get_data

data = get_data(file_name="day_2.txt")


def get_final_position(data):
    horizontal_position = 0
    depth = 0

    for i, step in data.items():

        direction = step.split(" ")[0]
        amount = int(step.split(" ")[1])

        if direction == "forward":
            horizontal_position += amount
        elif direction == "down":
            depth += amount
        elif direction == "up":
            depth -= amount

    return horizontal_position * depth


def puzzle_2(data):
    horizontal_position = 0
    depth = 0
    aim = 0

    for i, step in data.items():

        direction = step.split(" ")[0]
        amount = int(step.split(" ")[1])

        if direction == "forward":
            horizontal_position += amount
            depth += aim * amount
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount

        # print(step)
        # print(f"horizontal_position: {horizontal_position}")
        # print(f"depth: {depth}")
        # print(f"aim: {aim}")
        # print("--------")

    return horizontal_position * depth


print(f"puzzle 1 - {get_final_position(data=data)}")
print(f"puzzle 2 - {puzzle_2(data=data)}")
