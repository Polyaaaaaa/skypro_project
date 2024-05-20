import json
from typing import Any
import requests
import os
from dotenv import load_dotenv


def get_list_of_transactions(filepath: str) -> Any:
    """
    функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            dicts_in_list = json.load(file)
    except json.decoder.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
    else:
        if len(dicts_in_list) > 0:
            return dicts_in_list
        elif not isinstance(dicts_in_list, list):
            return []

    return []


def get_sum_transactions(transaction: dict) -> float:
    """
    функция, которая принимает на вход транзакцию
    и возвращает сумму транзакции (amount) в рублях, возвращает тип float
    """
    summ = 0.0
    amnt = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency != "RUB":

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={currency}&amount={amnt}"
        load_dotenv()
        api_key = os.getenv("API_KEY")
        headers = {"apikey": api_key}
        payload: dict = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.json().get("result")
        summ += result
    else:
        summ += float(amnt)
    return summ


print(
    get_sum_transactions(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        }
    )
)
