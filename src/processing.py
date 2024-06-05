from datetime import datetime


def get_new_list(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """функция, фильтрующая список"""
    new_list = []
    for i in list_of_dicts:
        if i.get("state") == state:
            new_list.append(i)
    return new_list


def get_sorted_list(list_of_dicts: list, order: bool = False) -> list:
    """функция, сортирующая список по дате"""
    list_of_dicts.sort(key=lambda a: datetime.strptime(a.get("date"), "%Y-%m-%dT%H:%M:%S.%f"), reverse=order)
    return list_of_dicts
