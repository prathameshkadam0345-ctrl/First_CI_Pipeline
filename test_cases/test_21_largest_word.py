
import importlib.util

spec = importlib.util.spec_from_file_location(
    "largest_word_module", "codes/21_largest_word.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
largest_word = module.largest_word

def test_normal_sentence():
    assert largest_word("Python is a programming language") == "programming"


def test_single_word():
    assert largest_word("Hello") == "Hello"


def test_empty_sentence():
    assert largest_word("") == ""


def test_same_length_words():
    assert largest_word("cat dog") == "cat"


def test_multiple_spaces():
    assert largest_word("I love     Python") == "Python"
