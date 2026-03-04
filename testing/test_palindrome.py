import pytest
from lib.palindrome import longest_palindromic_substring

# Test case for input "babad"
# Longest palindrome can either be "bab" or "aba"
def test_babad():
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]

# Test case for input "cbbd"
# Longest palindrome is "bb"
def test_cbbd():
    assert longest_palindromic_substring("cbbd") == "bb"

# Test case for a single character string
# A single character is always a palindrome
def test_single_character():
    assert longest_palindromic_substring("a") == "a"

# Test case for two different characters
# Either "a" or "c" is a valid longest palindrome
def test_two_characters():
    result = longest_palindromic_substring("ac")
    assert result in ["a", "c"]

# Test case where whole string is a palindrome
# Function should retire entire string
def test_full_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"

# Test case with an empty string
# Input: ""; Function should return an empty string
def test_empty_string():
    assert longest_palindromic_substring("") == ""

# Test case with a palindrome in the middle of the string
# Input: "forgeeksskeegfor"; Function should return "geeksskeeg"
def test_palindrome_in_middle():
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"
