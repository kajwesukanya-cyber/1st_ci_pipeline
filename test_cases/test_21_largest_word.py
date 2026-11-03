
import importlib

module = importlib.import_module("21_largest_word")

largest_word = module.largest_word


# Test Case 1
def test_simple_sentence():
    assert largest_word("I love programming") == "programming"


# Test Case 2
def test_punctuation_is_ignored():
    assert largest_word("Hello, world!") == "Hello"


# Test Case 3
def test_tie_returns_first_word():
    assert largest_word("cat dog bat") == "cat"


# Test Case 4
def test_single_word():
    assert largest_word("Python") == "Python"


# Test Case 5
def test_empty_sentence():
    assert largest_word("") == ""
