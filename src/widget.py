from src.masks import masked_card_num, masked_account_num


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


print(mask_elements("Счет 73654108430135874305"))
print(mask_elements("Visa Platinum 7000792289606361"))