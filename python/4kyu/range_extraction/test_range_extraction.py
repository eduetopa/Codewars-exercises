import pytest
from range_extraction import range_extraction  # Reemplaza 'tu_archivo' por el nombre real del archivo .py

def test_example_case():
    assert range_extraction([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]) == "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"

def test_all_individuals():
    assert range_extraction([1, 3, 5, 7, 9]) == "1,3,5,7,9"

def test_all_ranges():
    assert range_extraction([1, 2, 3, 4, 5, 6]) == "1-6"

def test_mixed_ranges_and_individuals():
    assert range_extraction([1, 2, 3, 5, 6, 9, 10, 11, 13]) == "1-3,5,6,9-11,13"

def test_minimum_range_length():
    assert range_extraction([1, 2]) == "1,2"
    assert range_extraction([1, 2, 3]) == "1-3"

def test_with_negative_numbers():
    assert range_extraction([-3, -2, -1, 0, 1, 3, 5, 6, 7, 9]) == "-3-1,3,5-7,9"

def test_single_element():
    assert range_extraction([42]) == "42"

def test_two_elements_not_a_range():
    assert range_extraction([7, 8]) == "7,8"

def test_two_elements_forming_range():
    assert range_extraction([7, 8, 9]) == "7-9"
