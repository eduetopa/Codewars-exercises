import pytest
from rgb_to_hex_conversion import rgb  

def test_rgb_normal_values():
    assert rgb(255, 255, 255) == "FFFFFF"
    assert rgb(0, 0, 0) == "000000"
    assert rgb(255, 0, 0) == "FF0000"
    assert rgb(0, 255, 0) == "00FF00"
    assert rgb(0, 0, 255) == "0000FF"
    assert rgb(173, 216, 230) == "ADD8E6"

def test_rgb_boundary_values():
    assert rgb(1, 2, 3) == "010203"
    assert rgb(254, 253, 252) == "FEFDFC"

def test_rgb_below_zero():
    assert rgb(-20, 0, 0) == "000000"
    assert rgb(-5, -1, -255) == "000000"

def test_rgb_above_255():
    assert rgb(256, 300, 500) == "FFFFFF"
    assert rgb(0, 255, 300) == "00FFFF"

def test_rgb_mixed_limits():
    assert rgb(-10, 128, 300) == "0080FF"
