from typing import Union

import pytest

from src.widget import format_card_account, get_date, mask_account_card


@pytest.mark.parametrize(
    "string, number_card_and_account",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(string: Union[str], number_card_and_account: Union[str]) -> None:
    assert mask_account_card(string) == number_card_and_account


with pytest.raises(IndexError):
    mask_account_card("")


def test_mask_account_card_empty(card_empty: Union[str]) -> None:
    assert mask_account_card(card_empty) == " You haven't entered anything."


@pytest.mark.parametrize(
    "date_string, date_wind",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
    ],
)
def test_get_date(date_string: Union[str], date_wind: Union[str]) -> None:
    assert get_date(date_string) == date_wind


def test_get_date_empty() -> None:
    assert get_date("") == "Внесите данные"


def test_format_card_account_empty(dict_for_test_empty: Union[str]) -> None:
    assert (
        format_card_account(dict_for_test_empty)
        == "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
    )


def test_format_card_account() -> None:
    expected_result = [
        {"from": "Счет **3391", "to": "Счет **9397", "description": "Перевод организации"},
        {
            "from": "Discover 3172 60** **** 0065",
            "to": "Discover 0720 42** **** 4643",
            "description": "Перевод с карты на карту",
        },
        {
            "from": "Visa 1959 23** **** 4097",
            "to": "Visa 6804 11** **** 3710",
            "description": "Перевод с карты на карту",
        },
        {
            "from": "Express 8025 48** **** 0082",
            "to": "Discover 7955 89** **** 2061",
            "description": "Перевод с карты на карту",
        },
    ]

    assert (
        format_card_account(
            [
                {
                    "from": "Счет 58803664561298323391",
                    "to": "Счет 39745660563456619397",
                    "description": "Перевод организации",
                },
                {
                    "from": "Discover 3172601889670065",
                    "to": "Discover 0720428384694643",
                    "description": "Перевод с карты на карту",
                },
                {
                    "from": "Visa 1959232722494097",
                    "to": "Visa 6804119550473710",
                    "description": "Перевод с карты на карту",
                },
                {
                    "from": "American Express 8025488368550082",
                    "to": "Discover 7955892722142061",
                    "description": "Перевод с карты на карту",
                },
            ]
        )
        == expected_result
    )
