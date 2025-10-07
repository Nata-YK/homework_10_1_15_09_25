from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number_list: Union[str], card_number_mask: Union[str]) -> None:
    assert get_mask_card_number(card_number_list) == card_number_mask


def test_get_mask_account(card_account_list: Union[str], card_account_mask: Union[str]) -> None:
    assert get_mask_account(card_account_list) == card_account_mask


def test_get_mask_account_sign(card_empty: Union[str]) -> None:
    assert get_mask_account(card_empty) == "Incorrect number of characters, in the account should be 20"


def test_get_mask_card_empty() -> None:
    assert get_mask_account("") == "You haven't entered anything."


def test_get_mask_card_number_sign(card_empty: Union[str]) -> None:
    assert get_mask_card_number(card_empty) == "Incorrect number of characters, should be 16."


def test_get_mask_account_empty() -> None:
    assert get_mask_card_number("") == "You haven't entered anything."
