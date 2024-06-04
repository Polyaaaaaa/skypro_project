transactions = [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            },
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160",
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657",
            },
        ]


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакициями.")
    print(
        """Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из json файла
2. Получить информацию о транзакциях из csv файла
3. Получить информацию о транзакциях из xlsx файла"""
    )

    user_input_1 = int(input())

    if user_input_1 == 1:
        print("Для обработки выбран json файл.")
    elif user_input_1 == 2:
        print("Для обработки выбран csv файл.")
    elif user_input_1 == 3:
        print("Для обработки выбран xlsx файл.")

    print(
        """Введите статус по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
    )

    user_input_2 = input()
    user_input_2_upper = user_input_2.upper()

    if user_input_2_upper == "EXECUTED" or user_input_2_upper == "CANCELED" or user_input_2_upper == "PENDING":
        print(f'Операции отфильтрованы по статусу "{user_input_2_upper}"')
    else:
        print(f'Статус операции "{user_input_2}" недоступен.')
        print(
            """Введите статус по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )


        print("Отсортировать операции по дате? Да/Нет")
        user_input_3 = input()
        print("Отсортировать по возрастанию или по убыванию?")
        user_input_4 = input()
        print("Выводить только рублевые тразакции? Да/Нет")
        user_input_5 = input()
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_input_6 = input()
        print("Распечатываю итоговый список транзакций...")

        print(f"Всего банковских операций в выборке: {len(transactions)}")


