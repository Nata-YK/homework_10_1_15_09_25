from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number_list: Union[str], card_number_mask: Union[str]) -> None:
    assert get_mask_card_number(card_number_list) == card_number_mask


def test_get_mask_account(card_account_list: Union[str], card_account_mask: Union[str]) -> None:
    assert get_mask_account(card_account_list) == card_account_mask


def test_get_mask_account_sign(card_empty: Union[str]) -> None:
    assert get_mask_account(card_empty) == "Не вреное количество знаков, в номере счета их должно быть 20"


def test_get_mask_card_empty() -> None:
    assert get_mask_account("") == "Вы ничего не ввели"


def test_get_mask_card_number_sign(card_empty: Union[str]) -> None:
    assert get_mask_card_number(card_empty) == "Не вреное количество знаков, в номере карты их должно быть 16"


def test_get_mask_account_empty() -> None:
    assert get_mask_card_number("") == "Вы ничего не ввели"
