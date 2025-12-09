from typing import Union

from src.external_api import get_transaction_amount
from src.libraries_re_collections import look_to_dictionary, count_transactions
# from src.external_api import get_transaction_amount
# from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.read_file_csv_xlsx import read_csv_file, read_xlsx_file
from src.utils import read_json


def print_hi(name: Union[str]) -> None:
    print(f"Hi, {name}")


if __name__ == "__main__":
    print_hi("PyCharm")

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

print(" * * *" * 25)

print(get_mask_card_number("7000792289606361"))  # Номер карты имеет 16 цифр
print(get_mask_account("70007922896063616541"))  # Номер счёта имеет 20 цифр
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

result = look_to_dictionary(dict_filter_by_currency, 'CANCELED')
print(result)

class_list = "Перевод организации"
print(count_transactions(dict_filter_by_currency, class_list))