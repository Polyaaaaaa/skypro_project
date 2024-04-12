def get_new_list(list_of_dicts, state="EXECUTED"):
    new_list = []
    for i in list_of_dicts:
        if i["state"] == state:
            new_list.append(i)
    print(new_list)



