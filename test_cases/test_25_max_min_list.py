
from importlib import import_module

find_max_min = import_module("25_max_min_list").find_max_min


def test_normal_list():
    assert find_max_min([5, 2, 8, 1, 9]) == (9, 1)


def test_single_element():
    assert find_max_min([7]) == (7, 7)


def test_negative_numbers():
    assert find_max_min([-5, -2, -8, -1]) == (-1, -8)


def test_duplicate_numbers():
    assert find_max_min([4, 4, 4]) == (4, 4)


def test_empty_list():
    import pytest
    with pytest.raises(ValueError):
        find_max_min([])
