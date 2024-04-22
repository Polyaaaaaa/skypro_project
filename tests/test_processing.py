import pytest

from src.processing import get_new_list, get_sorted_list


@pytest.fixture
def coll():  # имя фикстуры любое
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_get_new_list(coll) -> None:
    assert get_new_list(coll) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    assert get_new_list(coll, 'CANCELED') == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_to_sorted_list(coll) -> None:
    assert get_sorted_list(coll, order=True) == [
               {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
               {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
               {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
               {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
           ]
