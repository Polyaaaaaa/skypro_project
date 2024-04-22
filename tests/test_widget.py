from src.widget import get_date, mask_elements


def test_mask_elements() -> None:
    assert mask_elements("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_elements("Счет 73654108430135874305") == "Счет **4305"


def test_get_date() -> None:
    assert get_date("2018-07-11T02:26:18.671407") == "11.07.2018"
