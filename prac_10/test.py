"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return s * n


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) > length


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # Test Car's fuel setting with default value
    test_car = Car()
    assert test_car._fuel == 0, "Car does not set fuel correctly (default)"

    # Test Car's fuel setting with custom value
    test_car = Car(fuel=10)
    assert test_car._fuel == 10, "Car does not set fuel correctly (custom value)"


run_tests()

doctest.testmod()
def format_as_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a single full stop.
    >>> format_as_sentence('hello')
    'Hello.'
    >>> format_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_as_sentence('testing this function')
    'Testing this function.'
    """
    if not phrase:
        return ""
    formatted_phrase = phrase.capitalize()
    if formatted_phrase[-1] != '.':
        formatted_phrase += '.'
    return formatted_phrase