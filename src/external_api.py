import os
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из окружения .env

API_KEY = os.getenv("API_KEY")


def get_transaction_amount(transaction: Dict) -> float:
    """функция принимает на вход одну транзакцию и возвращает сумму транзакции в рублях"""
    if "operationAmount" in transaction:
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            return round(float(transaction["operationAmount"]["amount"]), 2)
        if transaction["operationAmount"]["currency"]["code"] in ["EUR", "USD"]:
            url = f"https://api.apilayer.com/currency_data/convert"
            payload = {
                "to": "RUB",
                "from": transaction["operationAmount"]["currency"]["code"],
                "amount": transaction["operationAmount"]["amount"],
            }
            headers = {"apikey": API_KEY}
            response = requests.get(url, headers=headers, params=payload)
            status_code = response.status_code
            result = response.json()
            print(result)
            if status_code == 200:
                return round(result["result"], 2)
            else:
                print("Не удалось перевести валюту в рубли")
                return status_code
