from puzzles.day_2 import get_final_position, puzzle_2
from tests.helpers import get_test_data

test_input = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def test_get_final_position():

    data = get_test_data(test_list=test_input)

    result = get_final_position(data=data)

    assert result == 150


def test_puzzle_2():
    data = get_test_data(test_list=test_input)
    result = puzzle_2(data=data)

    assert result == 900
