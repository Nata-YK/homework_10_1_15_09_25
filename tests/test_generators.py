from typing import List

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(
    dictionary_for_generator_filter_by_currency_1: List[str],
    dictionary_for_generator_filter_by_currency_2: List[str],
    dict_for_test: List[dict],
    dict_for_test_empty: List[dict],
) -> None:
    generator_filter_by_currency_ = filter_by_currency(dict_for_test, forex="USD")
    generator_filter_by_currency = filter_by_currency(dict_for_test)
    generator_filter_by_currency_currency = filter_by_currency(dict_for_test, forex="EURO")
    generator_filter_by_currency_empty = filter_by_currency(dict_for_test_empty)
    assert next(generator_filter_by_currency_) == dictionary_for_generator_filter_by_currency_1
    assert next(generator_filter_by_currency_) == dictionary_for_generator_filter_by_currency_2
    assert next(generator_filter_by_currency) == dictionary_for_generator_filter_by_currency_1
    assert next(generator_filter_by_currency) == dictionary_for_generator_filter_by_currency_2
    try:
        next(generator_filter_by_currency_empty)
    except StopIteration:
        print("Отсутствует итерируемый объект.")
    try:
        next(generator_filter_by_currency_currency)
    except StopIteration:
        print("Информация о валюте отсутствует в строке.")


def test_transaction_descriptions(dict_for_test: List[dict], dict_for_test_empty: List[dict]) -> None:
    generator_transaction_descriptions = transaction_descriptions(dict_for_test)
    generator_empty = transaction_descriptions(dict_for_test_empty)
    assert next(generator_transaction_descriptions) == "Перевод организации"
    assert next(generator_transaction_descriptions) == "Перевод со счета на счет"
    assert next(generator_transaction_descriptions) == "Перевод со счета на счет"
    try:
        next(generator_empty)
    except StopIteration:
        print("Отсутствует итерируемый объект.")


def test_card_number_generator() -> None:
    generator_card_number_generator = card_number_generator()
    assert next(generator_card_number_generator) == "0000 0000 0000 0001"
    assert next(generator_card_number_generator) == "0000 0000 0000 0002"
    assert next(generator_card_number_generator) == "0000 0000 0000 0003"
    assert next(generator_card_number_generator) == "0000 0000 0000 0004"
    assert next(generator_card_number_generator) == "0000 0000 0000 0005"


def test_card_number_generator_mistake() -> None:
    generator_card_number_generator_mistake = card_number_generator(10, 9)
    try:
        next(generator_card_number_generator_mistake)
    except StopIteration:
        print("Не верное значение должно быть от 1 до 9999999999999999.")
