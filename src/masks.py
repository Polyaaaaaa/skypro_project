def masked_card_num(num: str) -> str:
    """функция принимает номер карты и возвращает замаскированный номер
    @rtype: object
    """
    number = 4
    return f"{num[:number]} {num[number:number + 2]}** **** {num[number + 8:]}"


def masked_account_num(num: str) -> str:
    """функция принимает номер счёта и возвращает замаскированный номер"""
    return f"**{num[-4:]}"
