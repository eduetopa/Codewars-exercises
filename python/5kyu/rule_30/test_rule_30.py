import pytest
from rule_30 import rule30  # Cambia 'your_module' por el nombre real de tu archivo sin .py

def test_no_iterations_returns_same_array():
    assert rule30([0, 1, 0], 0) == [0, 1, 0]

def test_all_zeros_are_padded_when_no_ones():
    # Con n=3, añade 6 ceros más
    assert rule30([0, 0, 0], 3) == [0, 0, 0, 0, 0, 0, 0, 0, 0]

def test_single_1_iter_1():
    assert rule30([1], 1) == [1, 1, 1]

def test_single_1_iter_2():
    assert rule30([1], 2) == [1, 1, 0, 0, 1]

def test_single_1_iter_3():
    assert rule30([1], 3) == [1, 1, 0, 1, 1, 1, 1]

def test_asymmetric_input():
    assert rule30([1, 0, 1], 1) == [1, 1, 0, 1, 1]

def test_multiple_iterations_centered_seed():
    assert rule30([0, 1, 0], 2) == [1, 1, 0, 0, 0, 0, 1]

def test_single_1_iter_5():
    result = rule30([1], 5)
    expected = [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1]
    assert result == expected

