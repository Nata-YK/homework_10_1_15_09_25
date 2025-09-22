from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """
    Функция которая принимает номер карты, а выводит только первые 6 цифр карты и последние 4,
    а вместо остальных ставит **(звездочки)
    """
    card_num = []
    card_number_str = str(card_number)
    star_sp = "** **** "
    if len(card_number_str) == 16:
        for num in card_number_str:
            card_num.append(num)
            card_widget = "".join(card_num[:4]) + " " + "".join(card_num[4:6]) + star_sp + "".join(card_num[-4:])
        return card_widget
    elif len(card_number_str) > 0:
        return "Не вреное количество знаков, в номере карты их должно быть 16"
    else:
        return "Вы ничего не ввели"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """
    Функция которая принимает номер счета, а выводит только последние 4 цифры,
    а вместо последних 5 и 6 цифр ставит **(звездочки)
    """
    account_num = []
    account_number_str = str(account_number)
    star_spice = "**"
    if len(account_number_str) == 20:
        for num in account_number_str:
            account_num.append(num)
            account_widget = star_spice + "".join(account_num[-4:])
        return account_widget
    elif len(account_number_str) > 0:
        return "Не вреное количество знаков, в номере счета их должно быть 20"
    else:
        return "Вы ничего не ввели"


