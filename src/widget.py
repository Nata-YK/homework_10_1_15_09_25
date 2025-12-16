import re
from typing import Any, Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(information_number: Union[str]) -> Union[str]:
    """
    Функ-я принимает на вход строку для маскировки номера карты/счета и используются ранее написанные функции из модуля
    """
    card_split = information_number.rsplit(" ", 1)
    num_card = card_split[1]
    if card_split[0] == "Счет":
        return f"{card_split[0]} {get_mask_account(num_card)}"
    else:
        return f"{card_split[0]} {get_mask_card_number(num_card)}"


def get_date(listing_date: Union[str | list]) -> Any:
    """
    Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку
    с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
    """
    data_ = []
    point = "."
    if len(listing_date) > 0:
        for d in listing_date:
            data_.append(d)
        return "".join(data_[8:10]) + point + "".join(data_[5:7]) + point + "".join(data_[:4])
    else:
        return "Внесите данные"


patterns = [
    re.compile(r"(\d{20})"),  # Счет 20 цифр - группа 1
    re.compile(r"(\w+\s\d{16})"),  # Карта 16 цифр после названия - группа 1
    re.compile(r"([A-Za-z]+\s[A-Za-z]+)\s(\d{16})"),  # Формат "Слово Слово 16цифр" - группа 1
]


def format_card_account(transactions_filter: Any) -> Any:
    """
    Функция принимает список транзакций и маскирует номера карт/счетов
    """
    if not transactions_filter:
        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"

    formatted_transactions = []

    for transaction in transactions_filter:
        formatted_transaction = transaction.copy()  # Создаем копию для изменений

        # Обрабатываем поле 'to'
        if transaction.get("to"):
            masked_to = transaction["to"]
            for pattern in patterns:
                match = pattern.search(transaction["to"])
                if match:
                    if pattern.pattern == r"(\d{20})":  # Счет
                        number = match.group(1)
                        masked_to = f"Счет **{number[-4:]}"
                        break
                    elif pattern.pattern == r"(\w+\s\d{16})":  # Карта типа "Visa 1234..."
                        full_match = match.group(1)
                        card_match = re.search(r"(\d{16})", full_match)
                        if card_match:
                            card_number = card_match.group(1)
                            card_name = full_match.replace(card_number, "").strip()
                            masked_to = f"{card_name} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
                        break
                    elif pattern.pattern == r"(\w+\s\w+\s\d{16})":  # Формат типа "Visa Platinum 7000..."
                        full_match = match.group(1)
                        card_match = re.search(r"(\d{16})", full_match)
                        if card_match:
                            card_number = card_match.group(1)
                            card_name = full_match.replace(card_number, "").strip()
                            masked_to = f"{card_name} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
                        break
            formatted_transaction["to"] = masked_to

        # Обрабатываем поле 'from'
        if transaction.get("from"):
            masked_from = transaction.get("from")
            for pattern in patterns:
                match = pattern.search(transaction["from"])
                if match:
                    if pattern.pattern == r"(\d{20})":  # Счет
                        number = match.group(1)
                        masked_from = f"Счет **{number[-4:]}"
                        break
                    elif pattern.pattern == r"(\w+\s\d{16})":  # Карта типа "Visa 1234..."
                        full_match = match.group(1)
                        # Ищем 16 цифр
                        card_match = re.search(r"(\d{16})", full_match)
                        if card_match:
                            card_number = card_match.group(1)
                            # Сохраняем название карты
                            card_name = full_match.replace(card_number, "").strip()
                            masked_from = f"{card_name} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
                        break
                    elif pattern.pattern == r"(\w+\s\w+\s\d{16})":  # Формат типа "Visa Platinum 7000..."
                        full_match = match.group(1)
                        # Ищем 16 цифр
                        card_match = re.search(r"(\d{16})", full_match)
                        if card_match:
                            card_number = card_match.group(1)
                            # Сохраняем название карты
                            card_name = full_match.replace(card_number, "").strip()
                            masked_from = f"{card_name} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
                        break

            formatted_transaction["from"] = masked_from

        formatted_transactions.append(formatted_transaction)

    return formatted_transactions

