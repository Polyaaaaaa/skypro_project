from src.processing import get_new_list, get_sorted_list
from src.utils import (
    find_string,
    get_csv_file_as_DataFrame,
    get_dict,
    get_list_of_transactions,
    get_sum_transactions,
    get_xlsx_file_as_DataFrame,
)
from src.widget import get_date, mask_elements


def main():
    """
    Связующая функция
    """

    global transactions, sorted_list_by_date, found_word, mask_elements
    print("Привет! Добро пожаловать в программу работы с банковскими транзакициями.")
    print(
        """Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из json файла
2. Получить информацию о транзакциях из csv файла
3. Получить информацию о транзакциях из xlsx файла"""
    )

    user_input_1 = int(input())

    if user_input_1 == 1:
        transactions = get_list_of_transactions(
            r"C:\Users\Student Free\PycharmProjects\pythonProject2\data\operations.json"
        )
        print("Для обработки выбран json файл.")
    elif user_input_1 == 2:
        transactions = get_csv_file_as_DataFrame(
            r"C:\Users\Student Free\PycharmProjects\pythonProject2\data\operations.json"
        )
        print("Для обработки выбран csv файл.")
    elif user_input_1 == 3:
        transactions = get_xlsx_file_as_DataFrame(
            r"C:\Users\Student Free\PycharmProjects\pythonProject2\data\operations.json"
        )
        print("Для обработки выбран xlsx файл.")

    print(
        """Введите статус по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
    )

    user_input_2 = input()
    user_input_2_upper = user_input_2.upper()

    if user_input_2_upper == "EXECUTED" or user_input_2_upper == "CANCELED" or user_input_2_upper == "PENDING":
        print(f'Операции отфильтрованы по статусу "{user_input_2_upper}"')
        filtered_list = get_new_list(transactions, user_input_2_upper)
    else:
        print(f'Статус операции "{user_input_2}" недоступен.')
        print(
            """Введите статус по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )
        user_input_3 = input()
        user_input_3_upper = user_input_3.upper()
        filtered_list = get_new_list(transactions, user_input_3_upper)

    print("Отсортировать операции по дате? Да/Нет")
    user_input_4 = input()
    if user_input_4 == "Да":
        print("Отсортировать по возрастанию или по убыванию?")
        user_input_5 = input()
        if user_input_5 == "по возрастанию":
            sorted_list_by_date = get_sorted_list(filtered_list, False)
        else:
            sorted_list_by_date = get_sorted_list(filtered_list, True)
    else:
        sorted_list_by_date = filtered_list

    print("Выводить только рублевые тразакции? Да/Нет")
    user_input_6 = input()
    transact_list = []
    if user_input_6 == "Да":
        for transaction in sorted_list_by_date:
            transactions_ = get_sum_transactions(transaction)
            transact_list.append(transactions_)
    else:
        for transaction in sorted_list_by_date:
            transactions_ = get_sum_transactions(transaction)
            transact_list.append(transactions_)
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_input_7 = input()
    if user_input_7 == "Да" and user_input_6 == "Да":
        print("Введите слово/выражение по которому хотите найти отфильтровать транзакции")
        search_bar = input()
        found_word = find_string(sorted_list_by_date, search_bar)
        print("Распечатываю итоговый список транзакций...")
    if len(sorted_list_by_date) == 0:
        print("Не найдено ни одной транзакции подходящей под ваши условия фильтрации")
    else:
        if user_input_7 == "Да" and user_input_6 == "Да":
            print(f"Всего банковских операций в выборке: {len(found_word)}")
            print(found_word)
            for element in sorted_list_by_date:
                date = element["date"]
                description = element["description"]
                from_ = element.get("from", "None card/account")
                to = element["to"]
                print(
                    f"""{get_date(date)} {description}
            {mask_elements(from_)} -> {mask_elements(to)}
            Сумма: {get_sum_transactions(element)}
            """
                )
        else:
            print(f"Всего банковских операций в выборке: {len(sorted_list_by_date)}")
            for element in sorted_list_by_date:
                date = element["date"]
                description = element["description"]
                from_ = element.get("from", "None card/account")
                to = element["to"]
                print(
                    f"""{get_date(date)} {description}
{mask_elements(from_)} -> {mask_elements(to)}
Сумма: {get_sum_transactions(element)}
"""
                )
    return "That's all"


if __name__ == '__main__':
    main()
