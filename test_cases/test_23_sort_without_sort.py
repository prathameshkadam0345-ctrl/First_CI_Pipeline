
from importlib import import_module

bubble_sort = import_module("23_sort_without_sort").bubble_sort


def test_normal_list():
    assert bubble_sort([5, 2, 8, 1]) == [1, 2, 5, 8]


def test_already_sorted():
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_reverse_order():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_empty_list():
    assert bubble_sort([]) == []


def test_duplicate_numbers():
    assert bubble_sort([4, 2, 4, 1, 2]) == [1, 2, 2, 4, 4]
