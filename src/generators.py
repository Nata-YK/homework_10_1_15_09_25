from typing import Any, Generator, Iterable, Union


def filter_by_currency(
    dict_filter_by_currency: Iterable[dict], forex: Union[str] = "USD"
) -> Generator[Any, Any, None]:
    """
    Функция, которая принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции, где валюта операции соответствует задан-
    ной (например, USD).
    """
    if dict_filter_by_currency != []:
        if dict_filter_by_currency:
            for k in dict_filter_by_currency:
                if k["operationAmount"]["currency"]["name"] == forex:
                    yield k
    else:
        yield "Отсутствует итерируемый объект"


def transaction_descriptions(dict_filter_by_currency: Iterable[dict]) -> Generator[Any, Any, None]:
    """
    Функция, которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    """
    if dict_filter_by_currency != []:
        for k in dict_filter_by_currency:
            yield k["description"]
    else:
        yield "Отсутствует итерируемый объект"

def card_number_generator() -> Generator[Any, Any, None]:
    """
    Создайте генератор card_number_generator, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где
    X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до
    9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.
    """

    num = int("1")
    for card in range(10000000000000000):
        number_card = str(num).zfill(16)
        yield (f"{number_card[0:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:]}")
        num += 1
