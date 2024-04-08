from src.masks import masked_card_num, masked_account_num
from datetime import datetime


def mask_elements(element: str) -> str:
    if element[0] == 'С':
        for i in range(len(element)):
            if element[i].isalpha():
                pass
            elif element[i].isdigit():
                mask = masked_account_num(element[i:])
                return f"Счёт {mask}"

    else:
        for i in range(len(element)):
            if element[i].isalpha():
                continue
            elif element[i].isdigit():
                mask = masked_card_num(element[i:])
                return f'{element[:-16]}{mask}'
                #return mask


def get_date(date: str) -> str:
    day, month, year = date[8:10], date[5:7], date[:4]
    return f'{day}.{month}.{year}'git



