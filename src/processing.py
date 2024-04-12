from datetime import datetime


def get_new_list(list_of_dicts, state="EXECUTED"):
    new_list = []
    for i in list_of_dicts:
        if i["state"] == state:
            new_list.append(i)
    return new_list


def get_sorted_list(list_of_dicts, order=False):
    list_of_dicts.sort(key=lambda a: datetime.strptime(a['date'], "%Y-%m-%dT%H:%M:%S.%f"), reverse=order)
    return list_of_dicts
