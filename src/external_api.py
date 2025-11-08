import os
from typing import Dict, Union, Any

import requests
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из окружения .env

API_KEY = os.getenv("API_KEY")


def get_transaction_amount(transaction: Dict) -> float | tuple[str, set[int]]:
    """функция принимает на вход одну транзакцию и возвращает сумму транзакции в рублях"""
    if "operationAmount" in transaction:
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            return round(float(transaction["operationAmount"]["amount"]), 2)
        elif transaction["operationAmount"]["currency"]["code"] in ["EUR", "USD"]:
            url = "https://api.apilayer.com/exchangerates_data/convert"
            payload = {
                "to": "RUB",
                "from": transaction["operationAmount"]["currency"]["code"],
                "amount": transaction["operationAmount"]["amount"],
            }
            headers = {"apikey": API_KEY}
            response = requests.get(url, headers=headers, params=payload)
            status_code = response.status_code
            result = response.json()
            if status_code == 200:
                return round(result["result"], 2)
            else:
                return "Не удалось перевести валюту в рубли", {status_code}
    else:
        return "Список отсутствует"
