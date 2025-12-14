import re
from ast import parse
from collections import Counter
from dateutil.parser import parse


def look_to_dictionary(dict_list, string):
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка.
    """
    try:
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
        return {e}


def count_transactions(dict_list, class_list):
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой кате-
    гории.
    """
    filtered_transactions = []  # Создаем пустой список
    for key in dict_list:  # Итерируемся по списку словарей
        if (
            key.get("description") == class_list
        ):  # Сравниваем заданное значение "class_list" с заданным классом "description"
            filtered_transactions.append(
                key["description"]
            )  # Если сравнение верно, добавляем данный ключ в новый список
    return Counter(filtered_transactions)  # для подсчета количества банковских операций воспользуемся Counter


def look_date(dict_list):
    for item in dict_list:
        date_obj = parse(item["date"])
        formatted_date = date_obj.strftime("%d.%m.%Y")
        return formatted_date
