from importlib import import_module

decimal_to_binary = import_module("30_decimal_to_binary").decimal_to_binary


def test_decimal_10():
    assert decimal_to_binary(10) == "1010"


def test_zero():
    assert decimal_to_binary(0) == "0"


def test_one():
    assert decimal_to_binary(1) == "1"


def test_decimal_255():
    assert decimal_to_binary(255) == "11111111"


def test_negative_number():
    import pytest
    with pytest.raises(ValueError):
        decimal_to_binary(-10)