from collections import OrderedDict

from day_1.puzzle_1 import get_sliding_increase

test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

test_data_as_dict = OrderedDict()

for i, reading in enumerate(test_data):
    test_data_as_dict[i] = int(reading)


def test_get_sliding_increase():
    result = get_sliding_increase(data=test_data_as_dict)

    assert result == 5
