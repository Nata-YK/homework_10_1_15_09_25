import logging
from typing import Union

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """
    Функция которая принимает номер карты, а выводит только первые 6 цифр карты и последние 4,
    а вместо остальных ставит **(звездочки)
    """
    card_num = []
    logger.debug("The card number was received and converted to a string")
    card_number_str = str(card_number)
    star_sp = "** **** "
    logger.info("The card number digits are hidden from 7 to 12")
    if len(card_number_str) == 16:
        logger.info("The card has 16 digits")
        for num in card_number_str:
            card_num.append(num)
            card_widget = "".join(card_num[:4]) + " " + "".join(card_num[4:6]) + star_sp + "".join(card_num[-4:])
        return card_widget
    elif len(card_number_str) > 0:
        logger.warning("Incorrect number of characters, should be 16.")
        return "Incorrect number of characters, should be 16."
    else:
        logger.error("You haven't entered anything.")
        return "You haven't entered anything."


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """
    Функция которая принимает номер счета, а выводит только последние 4 цифры,
    а вместо последних 5 и 6 цифр ставит **(звездочки)
    """
    account_num = []
    logger.debug("The account number was received and converted to a string")
    account_number_str = str(account_number)
    star_spice = "**"
    logger.info("The account number digits are hidden from 1 to 16")
    if len(account_number_str) == 20:
        logger.info("The account has 20 digits")
        for num in account_number_str:
            account_num.append(num)
            account_widget = star_spice + "".join(account_num[-4:])
        return account_widget
    elif len(account_number_str) > 0:
        logger.warning("Incorrect number of characters, should be 20.")
        return "Incorrect number of characters, in the account should be 20"
    else:
        logger.error("You haven't entered anything.")
        return "You haven't entered anything."
