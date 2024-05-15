import json
from typing import Any
import requests
import os


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
    summ = 0
    amnt = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency != "RUB":

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={currency}&amount={amnt}"

        api_key = os.getenv('API_KEY')
        headers = {"apikey": api_key}
        payload: dict = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.json().get("result")
        summ += result
    else:
        summ += amnt
    return summ