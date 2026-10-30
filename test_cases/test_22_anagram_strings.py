
from importlib import import_module

is_anagram = import_module("22_anagram_strings").is_anagram


def test_normal_anagram():
    assert is_anagram("listen", "silent") is True


def test_different_case():
    assert is_anagram("Listen", "Silent") is True


def test_with_spaces():
    assert is_anagram("rail safety", "fairy tales") is True


def test_not_anagram():
    assert is_anagram("hello", "world") is False


def test_empty_strings():
    assert is_anagram("", "") is True
