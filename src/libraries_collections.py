import re
from collections import Counter
from typing import Any, Dict, Iterable, List, Union

from dateutil.parser import parse


def look_to_dictionary(dict_list: List[dict], string: Union[str]) -> Any:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка.
    """
    try:
        # Проверяем на None и пустую строку
        if string is None or string.strip() == "":
            return dict_list.copy()  # Возвращаем копию для безопасности

        pattern = re.compile(re.escape(string))  # Используем re.escape для поиска точного совпадения
        list_dictionary = []
        for dct in dict_list:  # Итерируемся по списку словарей
            for key, value in dct.items():  # Итерируемся по каждому словарю
                if isinstance(value, str) and pattern.search(value):
                    list_dictionary.append(dct)
                    if list_dictionary == []:
                        return "Значения нет в списке"
                        break  # Добавляем в словарь или прерываем внутренний цикл
        return list_dictionary
    except Exception as e:
        return f"Ошибка: {e}"


def count_transactions(dict_list: List[dict], categories: List[str]) -> Dict[str, int]:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой кате-
    гории.
    """
    # counter = Counter()
    # for key in dict_list:  # Итерируемся по списку словарей
    #     description_class = key.get('description', "")  # Проверяем, входит ли описание в список категорий
    #     if description_class in categories:
    #         counter[description_class] += 1
    # return dict(counter)  # для подсчета количества банковских операций воспользуемся Counter

    return dict(
        Counter(key.get("description", "") for key in dict_list if key.get("description", "") in set(categories))
    )


def look_date(dict_list: Iterable[dict]) -> Any:
    for item in dict_list:
        date_obj = parse(item["date"])
        formatted_date = date_obj.strftime("%d.%m.%Y")
        return formatted_date


# if __name__ == '__main__':
#     dict_word = [
#         {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702",
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188",
#         },
#         {
#             "id": 873106923,
#             "state": "EXECUTED",
#             "date": "2019-03-23T01:09:46.296404",
#             "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
#             "description": "Перевод со счета на счет",
#             "from": "Счет 44812258784861134719",
#             "to": "Счет 74489636417521191160",
#         },
#         {
#             "id": 895315941,
#             "state": "EXECUTED",
#             "date": "2018-08-19T04:27:37.904916",
#             "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод с карты на карту",
#             "from": "Visa Classic 6831982476737658",
#             "to": "Visa Platinum 8990922113665229",
#         },
#         {
#             "id": 594226727,
#             "state": "CANCELED",
#             "date": "2018-09-12T21:27:25.241689",
#             "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
#             "description": "Перевод организации",
#             "from": "Visa Platinum 1246377376343588",
#             "to": "Счет 14211924144426031657",
#         },
#     ]
#     categories = ["Перевод с карты на карту","Перевод организации"]
#     result = count_transactions(dict_word,categories)
#     print(result)
