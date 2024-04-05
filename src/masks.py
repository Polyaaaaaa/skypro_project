def return_masked_card_num(num: str) -> str:
    """функция принимает номер карты и возвращает замаскированный номер"""
    i = 4
    return f"{num[:i]} {num[i:i+2]}** **** {num[i + 8:]}"


def return_masked_account_num(num: str) -> str:
    """функция принимает номер счёта и возвращает замаскированный номер"""
    return f"**{num[-4:]}"
