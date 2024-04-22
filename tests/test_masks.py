import pytest

from src.masks import masked_account_num, masked_card_num


@pytest.fixture
def coll() -> list:  # имя фикстуры любое
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_masked_card_num() -> None:
    assert masked_card_num("7000799978996361") == "7000 79** **** 6361"


def test_masked_account_num() -> None:
    assert masked_account_num("98766667774305") == "**4305"
