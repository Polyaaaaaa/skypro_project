import json
import logging
import os
import re
from collections import Counter
from typing import Any

import pandas as pd
import requests
from dotenv import load_dotenv

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("loggers_info.txt")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_list_of_transactions(filepath: str) -> Any:
    """
    функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях
    """
    logger.info(f"start get_list_of_transactions {filepath}")
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            dicts_in_list = json.load(file)
    except json.decoder.JSONDecodeError:
        result_1: Any = []
        logger.info(f"the resulting list {result_1}")
        return result_1
    except FileNotFoundError:
        result_2: Any = []
        logger.info(f"the resulting list {result_2}")
        return result_2
    else:
        if len(dicts_in_list) > 0:
            result_3: Any = dicts_in_list
            logger.info(f"the resulting list {result_3}")
            return result_3
        elif not isinstance(dicts_in_list, list):
            result_4: Any = []
            logger.info(f"the resulting list {result_4}")
            return result_4

    result_5: Any = []
    logger.info(f"the resulting list {result_5}")
    return result_5


def get_sum_transactions(transaction: dict) -> float:
    """
    функция, которая принимает на вход транзакцию
    и возвращает сумму транзакции (amount) в рублях, возвращает тип float
    """
    logger.info(f"start get_sum_transactions {transaction}")
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
        result = response.json().get("result", 0.0)
        summ += result
    else:
        summ += float(amnt)
    result = summ
    logger.info(f"sum {result}")
    return float(result)


def get_xlsx_file_as_DataFrame(filepath: str) -> dict:
    """
    Реализовывает считывание финансовых операций с XLSX-файлов
    """
    reviews = pd.read_excel(filepath)
    filepath_dict = reviews.to_dict(orient="records")
    return filepath_dict


def get_csv_file_as_DataFrame(filepath: str) -> list:
    """
    Реализовывает считывание финансовых операций с CSV-файлов
    """
    reviews = pd.read_csv(filepath, sep=";")
    filepath_dict = reviews.to_dict(orient="records")
    return filepath_dict


def find_string(transactions: list, search_bar: str) -> list:
    """
    функция поиска операций с определенными словами в описании
    """
    result = []
    pattern = re.compile(search_bar, re.IGNORECASE)
    for transaction in transactions:
        if pattern.search(transaction["description"]):
            result.append(transaction)
    return result


def get_dict(transactions: list, categories: dict) -> dict:
    """
    функция подсчета количества операций определенной категории
    """
    pattern_1 = re.compile("Перевод организации", re.IGNORECASE)
    pattern_2 = re.compile("Перевод со счета на счет", re.IGNORECASE)
    pattern_3 = re.compile("Перевод с карты на карту", re.IGNORECASE)

    counter = Counter(transaction["description"] for transaction in transactions)

    categories["Перевод организации"] += counter[pattern_1.pattern]
    categories["Перевод со счета на счет"] += counter[pattern_2.pattern]
    categories["Перевод с карты на карту"] += counter[pattern_3.pattern]

    return categories
