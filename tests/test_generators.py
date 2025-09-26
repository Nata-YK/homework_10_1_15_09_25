import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(
    dictionary_for_generator_filter_by_currency_1,
    dictionary_for_generator_filter_by_currency_2,
    dict_for_test,
    dict_for_test_empty,
):
    generator_filter_by_currency_ = filter_by_currency(dict_for_test, forex="USD")
    generator_filter_by_currency = filter_by_currency(dict_for_test)
    generator_filter_by_currency_empty = filter_by_currency(dict_for_test_empty)
    assert next(generator_filter_by_currency_) == dictionary_for_generator_filter_by_currency_1
    assert next(generator_filter_by_currency_) == dictionary_for_generator_filter_by_currency_2
    assert next(generator_filter_by_currency) == dictionary_for_generator_filter_by_currency_1
    assert next(generator_filter_by_currency) == dictionary_for_generator_filter_by_currency_2
    assert next(generator_filter_by_currency_empty) == "Отсутствует итерируемый объект"


def test_transaction_descriptions(dict_for_test, dict_for_test_empty):
    generator_transaction_descriptions = transaction_descriptions(dict_for_test)
    generator_empty = transaction_descriptions(dict_for_test_empty)
    assert next(generator_transaction_descriptions) == "Перевод организации"
    assert next(generator_transaction_descriptions) == "Перевод со счета на счет"
    assert next(generator_transaction_descriptions) == "Перевод со счета на счет"
    assert next(generator_empty) == "Отсутствует итерируемый объект"

def test_card_number_generator():
    generator_card_number_generator = card_number_generator()
    assert next(generator_card_number_generator) == "0000 0000 0000 0001"
    assert next(generator_card_number_generator) == "0000 0000 0000 0002"
    assert next(generator_card_number_generator) == "0000 0000 0000 0003"
    assert next(generator_card_number_generator) == "0000 0000 0000 0004"
