import re

from dateutil.parser import parse

from src.generators import filter_by_currency
from src.libraries_collections import look_to_dictionary, count_transactions, look_date
from src.processing import filter_by_state, sort_by_date
from src.read_file_csv_xlsx import read_csv_file, read_xlsx_file
from src.utils import read_json

import os.path

from src.widget import mask_account_card, format_card_account

folder = 'data'
file_json = 'operations.json'
file_csv = 'transactions.csv'
file_xlsx = 'transactions_excel.xlsx'
file_path_json = os.path.join(folder, file_json)
file_path_csv = os.path.join(folder, file_csv)
file_path_xlsx = os.path.join(folder, file_xlsx)
abs_path_json = os.path.abspath(file_path_json)
abs_path_csv = os.path.abspath(file_path_csv)
abs_path_xlsx = os.path.abspath(file_path_xlsx)



def print_hi() -> None:
    print(f"Привет! Добро пожаловать в программу работы с банковскими транзакциями. \nВыберите необходимый пункт меню:\n1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла.")
    choice_file = input()
    print(f'Пользователь: {choice_file}')
    return choice_file

def get_inform():
    choice = print_hi()
    if choice == '1':
        json_file = read_json(abs_path_json)
        print('Программа: Для обработки выбран JSON-файл.\n\nВведите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
        status_coice = input()
        filtered_transactions = filter_by_state(json_file, status_coice.upper())
        return filtered_transactions
    elif choice == '2':
        csv_file = read_csv_file(abs_path_csv)
        print('Программа: Для обработки выбран CSV-файла.\n\nВведите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
        status_coice = input()
        filtered_transactions = filter_by_state(csv_file, status_coice.upper())
        return filtered_transactions
    elif choice == '3':
        xlsx_file = read_xlsx_file(file_path_xlsx)
        print('Программа: Для обработки выбран XLSX-файла.\n\nВведите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
        status_coice = input()
        filtered_transactions = filter_by_state(xlsx_file, status_coice.upper())
        return filtered_transactions
    else:
        print("Файл отсутствует")

def sort_date():
    file_get = get_inform()
    print('Отсортировать операции по дате? Да/Нет')
    choice_sort = input()
    if choice_sort.title() == "Да":
        print('Отсортировать по возрастанию или по убыванию?')
        choice_sort_true = input()
        if choice_sort_true.lower() == 'убыванию':
            file_sored_true = sort_by_date(file_get, sort_parameter=True)
            return file_sored_true
        elif choice_sort_true.lower() == 'возрастанию':
            file_sored_false = sort_by_date(file_get, sort_parameter=False)
            return file_sored_false
    else:
        return file_get


def sort_rub():
    sorted_rub = sort_date()
    print('Выводить только рублевые транзакции? Да/Нет')
    rub_sorted_input = input()
    if rub_sorted_input.title() == "Да":
        rub_get_currency = filter_by_currency(sorted_rub, forex="RUB")
        return rub_get_currency
    else:
        return sorted_rub


def look_for():
    file_to_look = sort_rub()
    print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
    filter_trans_word = input()
    if filter_trans_word.title() == "Да":
        print('Слово для поиска')
        word_look_for = input()
        word_to = look_to_dictionary(file_to_look, word_look_for)
        len_count = len(word_to)
        print(f'Распечатываю итоговый список транзакций\nВсего банковских операций в выборке: {len_count}')
        return word_to
    elif filter_trans_word.title() == "Нет":
        list_count_not = file_to_look
        len_count_not = len(list_count_not)
        print(f'Распечатываю итоговый список транзакций\nВсего банковских операций в выборке: {len_count_not}')
        return file_to_look
    elif file_to_look  == []:
        print('Распечатываю итоговый список транзакций\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации')



def print_total():
    print_t = look_for()
    func_mask = format_card_account(print_t)
    for d in print_t:
        d["to"] = func_mask
        d["from"] = func_mask
        date_ob = parse(d["date"])
        formatted_date = date_ob.strftime("%d.%m.%Y")
        if d["description"] == "Открытие вклада":
            print(f'{formatted_date} {d.get("description")} \n{d["to"]}\nСумма: {d["amount"]} {d["currency_code"]}')
        elif d:
            arrow = "->"
            print(f'{formatted_date} {d.get("description")} \n{d["from"]} {arrow} {d["to"]}\nСумма: {d["amount"]} {d["currency_code"]}')




if __name__ == "__main__":
    print(print_total())



# print(mask_account_card("Visa Platinum 7000792289606361"))
# print(mask_account_card("Счет 73654108430135874305"))
# print(get_date("2024-03-11T02:26:18.671407"))
#
# print(
#     filter_by_state(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
# )
#
# print(
#     sort_by_date(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
# )

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
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

# dict_filter_by_currency_empty: List[dict] = []
#
# generator_1 = filter_by_currency(dict_filter_by_currency)
# print(next(generator_1))
# print(next(generator_1))
# # print(next(generator_1))
# # print(next(generator_1))
# try:
#     print(next(generator_1))
# except StopIteration:
#     print("Отсутствует итерируемый объект.")
#
# generator_2 = transaction_descriptions([])
# try:
#     print(next(generator_2))
# except StopIteration:
#     print("Отсутствует итерируемый объект.")
#
#
# generator_3 = card_number_generator(1, 9)
#
# print(next(generator_3))
# print(next(generator_3))
# print(next(generator_3))
# print(next(generator_3))
# print(next(generator_3))
# print(next(generator_3))
# print(next(generator_3))

# print(" * * *" * 25)
#
# print(get_mask_card_number("7000792289606361"))  # Номер карты имеет 16 цифр
# print(get_mask_account("70007922896063616541"))  # Номер счёта имеет 20 цифр
# print(read_json("data/operations.json"))

# print(
#     get_transaction_amount(
#         {"state": "EXECUTED", "operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}}}
#     )
# )
# print(
#     get_transaction_amount(
#         {
#             "id": 41428829,
#             "state": "EXECUTED",
#             "date": "2019-07-03T18:35:29.512364",
#             "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод организации",
#             "from": "MasterCard 7158300734726758",
#             "to": "Счет 35383033474447895560",
#         }
#     )
# )
# data = [
#     {
#         "id": "650703",
#         "state": "EXECUTED",
#         "date": "2023-09-05T11:30:32Z",
#         "amount": "16210",
#         "currency_name": "Sol",
#         "currency_code": "PEN",
#         "from": "Счет 58803664561298323391",
#         "to": "Счет 39745660563456619397",
#         "description": "Перевод организации",
#     }
# ]
print(25 * "~**~")
# print(read_csv_file("data/transactions.csv"))
# print(25 * "~")
# # {"state": "EXECUTED", "operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}}}
# print(read_xlsx_file("data/transactions_excel.xlsx"))

# result = look_to_dictionary(dict_filter_by_currency, 'CANCELED')
# print(result)

# class_list = "Перевод организации"
# print(count_transactions(dict_filter_by_currency, class_list))