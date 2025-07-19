import pytest
from counterfeit_dollar import counterfeit_dollar  


def test_counterfeit_coin_is_light_on_right_side():
    results = [
        "ABCD EFGH even",
        "ABCI EFJK up",
        "ABIJ EFGH even"
    ]
    assert counterfeit_dollar(results) == "K is the counterfeit coin and it is light."

def test_counterfeit_coin_is_heavy_on_right_side():
    results = [
        "ABCD EFGH even",
        "ABCI EFJK down",
        "ABIJ EFGH even"
    ]
    assert counterfeit_dollar(results) == "K is the counterfeit coin and it is heavy."

def test_counterfeit_coin_is_heavy_on_left_side():
    results = [
        "ABCD EFGH even",
        "EFJK ABCI up",
        "ABIJ EFGH even"
    ]
    assert counterfeit_dollar(results) == "K is the counterfeit coin and it is heavy."

def test_counterfeit_coin_is_light_on_left_side():
    results = [
        "ABCD EFGH even",
        "EFJK ABCI down",
        "ABIJ EFGH even"
    ]
    assert counterfeit_dollar(results) == "K is the counterfeit coin and it is light."

def test_counterfeit_coin_is_d_and_heavy():
    results = [
        "ABCD EFGH up",
        "ABCI EFJK even",
        "EFGH IJKL even"
    ]
    assert counterfeit_dollar(results) == "D is the counterfeit coin and it is heavy."

def test_coin_not_in_even_weighings_cannot_be_confirmed():
    results = [
        "ABCD EFGH down",
        "EFJK ABCI even",
        "IJKL ABCD even"
    ]
    assert counterfeit_dollar(results) == "???"

def test_all_weighings_even_results_in_unknown():
    results = [
        "ABCD EFGH even",
        "IJKL ABCD even",
        "EFGH IJKL even"
    ]
    assert counterfeit_dollar(results) == "???"

def test_multiple_conflicting_candidates_results_in_unknown():
    results = [
        "ABCD EFGH up",
        "IJKL ABCD down",
        "EFGH IJKL up"
    ]
    assert counterfeit_dollar(results) == "???"

def test_suspected_coin_gets_eliminated_later():
    results = [
        "ABCD EFGH up",
        "ABCI EFJK even",
        "KLMN OPQR even"
    ]
    assert counterfeit_dollar(results) == "???"

def test_same_weighing_flips_causes_invalid_state():
    results = [
        "ABCD EFGH up",
        "ABCD EFGH down",
        "ABCD EFGH even"
    ]
    assert counterfeit_dollar(results) == "???"
