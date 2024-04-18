from src.masks import masked_card_num, masked_account_num
import pytest


def test_masked_card_num():
    assert "7000 79** **** 6361" == "7000 79** **** 6361"


def test_masked_account_num():
    assert "**4305" == "**4305"


