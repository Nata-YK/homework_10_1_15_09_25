from typing import List

from src.libraries_collections import count_transactions, look_to_dictionary


def test_look_to_dictionary(dict_for_test: list) -> None:
    assert look_to_dictionary(dict_for_test, "CANCELED") == [
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "" "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        }
    ]
    assert look_to_dictionary(dict_for_test, "CANCELED000") == []


def test_count_transactions(dict_for_test: List[dict], categories: List[str]) -> None:
    assert count_transactions(dict_for_test, categories) == {"Перевод организации": 2, "Перевод с карты на карту": 1}
