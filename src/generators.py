from typing import Any, Generator, List, Union


def filter_by_currency(dict_for_test: List[dict], forex: Union[str] = "USD") -> Generator[Any, Any, None]:
    """
    Функция, которая принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции, где валюта операции соответствует задан-
    ной (например, USD).
    """
    try:
        if dict_for_test != []:
            if dict_for_test:
                for k in dict_for_test:
                    if k["operationAmount"]["currency"]["name"] == forex:
                        yield k
                    elif k["operationAmount"]["currency"]["name"] != forex:
                        yield f"Данная валюта отсутствует: {forex}"
        else:
            yield "Отсутствует итерируемый объект"
    except TypeError:
        yield "Информации о валютах нет в списке"


def transaction_descriptions(dict_for_test: List[dict]) -> Generator[Any, Any, None]:
    """
    Функция, которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    """
    if dict_for_test != []:
        for k in dict_for_test:
            yield k["description"]
    else:
        yield "Отсутствует итерируемый объект"


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
    else:
        yield "Не верное значение должно быть от 1 до 9999999999999999"
