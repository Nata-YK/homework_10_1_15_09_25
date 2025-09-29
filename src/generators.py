from typing import Any, Generator, List, Union


def filter_by_currency(dict_for_test: List[dict], forex: Union[str] = "USD") -> Generator[Any, Any, None]:
    """
    Функция, которая принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции, где валюта операции соответствует задан-
    ной (например, USD).
    """

    if not dict_for_test or dict_for_test == []:
        print("Отсутствует итерируемый объект.")
    else:
        for k in dict_for_test:
            if k.get("operationAmount", {}).get("currency", {}).get("name") == forex:
                yield k
            elif k.get("operationAmount", {}).get("currency", {}).get("name") != forex:
                print("Информация о валюте отсутствует в строке.")


def transaction_descriptions(dict_for_test: List[dict]) -> Generator[Any, Any, None]:
    """
    Функция, которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    """
    if dict_for_test != []:
        for k in dict_for_test:
            yield k.get("description")
    else:
        print("Отсутствует итерируемый объект.")


def card_number_generator(start: Union[int] = 1, stop: Union[int] = 9999999999999999) -> Generator[Any, Any, None]:
    """
    Создайте генератор card_number_generator, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где
    X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до
    9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.
    """
    if 0 < start < stop:
        for card in range(start, stop + 1):
            number_card = str(start).zfill(16)
            yield (f"{number_card[0:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:]}")
            start += 1
    elif start > stop:
        print("Не верное значение должно быть от 1 до 9999999999999999.")
