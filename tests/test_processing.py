from src.processing import get_new_list, get_sorted_list
import pytest


def test_get_new_list():
    assert "Visa Platinum 7000 79** **** 6361" == "Visa Platinum 7000 79** **** 6361"
    assert "Счет **4305" == "Счет **4305"


def test_sorted_list():
    assert "11.07.2018" == "11.07.2018"
