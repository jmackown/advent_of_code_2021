from get_input import get_data


def get_basic_increase_count(data):
    total = len(data)
    return sum(i > 0 and data[i] > data[i - 1] for i in range(total))


def get_sliding_increase(data):
    total = len(data)
    increase_count = 0
    for i in range(total):
        if i >= 2 and i <= total - 2:
            first_window = data[i] + data[i - 1] + data[i - 2]
            second_window = data[i + 1] + data[i] + data[i - 1]

            if second_window > first_window:
                increase_count += 1
    return increase_count


data = get_data(file_name="day_1.txt")

print(f"puzzle 1 - {get_basic_increase_count(data=data)}")
print(f"puzzle 2 - {get_sliding_increase(data=data)}")
