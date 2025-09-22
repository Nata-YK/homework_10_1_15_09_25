import pytest

from src.masks import get_mask_card_number, get_mask_account
from tests.conftext import card_number_list, card_number_mask, card_account_list, card_account_mask, card_empty


def test_get_mask_card_number(card_number_list, card_number_mask):
    assert get_mask_card_number(card_number_list) == card_number_mask

def test_get_mask_account(card_account_list, card_account_mask):
    assert get_mask_account(card_account_list) == card_account_mask

def test_get_mask_account_sign():
    assert get_mask_account(card_empty) == "Не вреное количество знаков, в номере счета их должно быть 20"

def test_get_mask_account_empty():
    assert get_mask_account('') == "Вы ничего не ввели"

def test_get_mask_card_number_sign():
    assert get_mask_card_number(card_empty) == "Не вреное количество знаков, в номере карты их должно быть 16"

def test_get_mask_account_empty():
    assert get_mask_card_number('') == "Вы ничего не ввели"

