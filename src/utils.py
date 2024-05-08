import json
import requests

API_KEY = "Y0NJSYiThQhh4r2ykGqyoeHJ8OISMbYU"


def get_list_of_transactions(filepath: str) -> list:
    try:
        with open(filepath, "r", encoding='utf-8') as file:
            dicts_in_list = json.load(file)
    except json.decoder.JSONDecodeError:
        return []
    else:
        if len(dicts_in_list) > 0:
            return dicts_in_list
        elif dicts_in_list is not list:
            return []


func = get_list_of_transactions("C:/Users/Student Free/PycharmProjects/pythonProject2/data/operations.json")
print(func)


def get_sum_transactions(transaction):
    summ = 0
    amnt = transaction.get('operationAmount')['amount']
    currency = transaction['operationAmount']['currency']['code']

    if currency != 'RUB':

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={currency}&amount={amnt}"

        payload = {}
        headers = {
            "apikey": API_KEY
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.json().get('result')
        summ += result
    else:
        summ += amnt
    return summ


print(get_sum_transactions({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "3.58",
        "currency": {
            "name": "руб.",
            "code": "EUR"
        }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
}))
