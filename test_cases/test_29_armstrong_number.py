from importlib import import_module

is_armstrong = import_module("29_armstrong_number").is_armstrong


def test_armstrong_number_153():
    assert is_armstrong(153) == True


def test_armstrong_number_9474():
    assert is_armstrong(9474) == True


def test_non_armstrong_number():
    assert is_armstrong(123) == False


def test_zero():
    assert is_armstrong(0) == True


def test_negative_number():
    assert is_armstrong(-153) == False