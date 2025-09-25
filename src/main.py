from typing import Union

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


def print_hi(name: Union[str]) -> None:

    print(f"Hi, {name}")


if __name__ == "__main__":
    print_hi("PyCharm")

print(get_mask_card_number("7000792289606361"))
print(get_mask_account("70007922896063616541"))
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))

print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)

print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)

print("#" * 10)
dict_filter_by_currency = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 142264643,
        "state": "EXECUTED",
        "date": "2025-01-01T23:20:05.206878",
        "operationAmount": {"amount": "25000", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 142264978,
        "state": "EXECUTED",
        "date": "2025-02-01T23:20:05.206878",
        "operationAmount": {"amount": "50000", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 142264643,
        "state": "EXECUTED",
        "date": "2025-01-02T23:20:05.206878",
        "operationAmount": {"amount": "35000", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод с карты на карту",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]
generator_1 = filter_by_currency(dict_filter_by_currency, forex="RUB")
print(next(generator_1))
# print(next(generator_1))
# print(next(generator_1))

generator_2 = transaction_descriptions(dict_filter_by_currency)
print(next(generator_2))
print(next(generator_2))


generator_3 = card_number_generator()
print(next(generator_3))
