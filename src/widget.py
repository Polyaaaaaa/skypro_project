from src.masks import masked_account_num, masked_card_num


def mask_elements(element: str) -> str | None:
    """Функция, маскирующая любой элемент,
    как номер карты, так и номер счёта"""
    if element[0] == "С":
        for i in range(len(element)):
            if element[i].isalpha():
                continue
            elif element[i].isdigit():
                mask = masked_account_num(element[i:])
                return f"Счет {mask}"

    else:
        for i in range(len(element)):
            if element[i].isalpha():
                continue
            elif element[i].isdigit():
                mask = masked_card_num(element[i:])
                return f"{element[:-16]}{mask}"
    return None


def get_date(date: str) -> str:
    """функция получает дату из полученных данных, и выводит её"""
    day, month, year = date[8:10], date[5:7], date[:4]
    return f"{day}.{month}.{year}"
