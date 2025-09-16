from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(information_number: Union[str]) -> Union[str]:
    """
    Функ-я принимает на вход строку для маскировки номера карты/счета и используются ранее написанные функции из модуля
    """
    card_split = information_number.rsplit(" ", 1)
    num_card = card_split[1]
    if card_split[0] == "Счет":
        return f"{card_split[0]} {get_mask_account(num_card)}"
    else:
        return f"{card_split[0]} {get_mask_card_number(num_card)}"


def get_date(listing_date: Union[str]) -> Union[str]:
    """
    Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку
    с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
    """
    data_ = []
    point = "."
    for d in listing_date:
        data_.append(d)
    return "".join(data_[8:10]) + point + "".join(data_[5:7]) + point + "".join(data_[:4])
