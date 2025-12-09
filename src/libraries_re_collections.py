import re
from collections import Counter, defaultdict


def look_to_dictionary(dict_list, string):
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

def count_transactions(dict_list, class_list):
    filtered_transactions = []
    for key in dict_list:
        if key.get("description") == class_list:
            filtered_transactions.append(key["description"])
    return Counter(filtered_transactions)

