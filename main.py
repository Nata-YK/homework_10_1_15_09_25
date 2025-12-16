import os.path
from typing import Any, Union

from dateutil.parser import parse

from src.generators import filter_by_currency
from src.libraries_collections import look_to_dictionary
from src.processing import filter_by_state, sort_by_date
from src.read_file_csv_xlsx import read_csv_file, read_xlsx_file
from src.utils import read_json
from src.widget import format_card_account

folder = "data"
file_json = "operations.json"
file_csv = "transactions.csv"
file_xlsx = "transactions_excel.xlsx"
file_path_json = os.path.join(folder, file_json)
file_path_csv = os.path.join(folder, file_csv)
file_path_xlsx = os.path.join(folder, file_xlsx)
abs_path_json = os.path.abspath(file_path_json)
abs_path_csv = os.path.abspath(file_path_csv)
abs_path_xlsx = os.path.abspath(file_path_xlsx)


def print_hi() -> Union[int | str]:
    """
    Функция выбора вида списка  для анализа JSON-файла или CSV-файла или XLSX-файла.
    """
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями. \nВыберите необходимый пункт меню:"
        "\n1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла\n3. "
        "Получить информацию о транзакциях из XLSX-файла."
    )
    while True:
        try:
            choice_file = int(input().strip())
            if choice_file in {1, 2, 3}:
                break
            else:
                print("Выбери существующий вариант: 1,2,3")

        except ValueError as e:
            print(f"Ошибка: недопустимое значение\n{e}\nВыбери существующий вариант: 1,2,3 ")
    print(f"Выбран №: {choice_file}")
    return choice_file


def get_inform() -> Any:
    """
    Функция принимает JSON-файла или CSV-файла или XLSX-файла и сортирует его по статусу EXECUTED, CANCELED, PENDING
    """
    choice = print_hi()
    print(
        "Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, "
        "CANCELED, PENDING"
    )
    while True:
        try:
            status_coice = input().strip()
            if status_coice.upper() in {"EXECUTED", "CANCELED", "PENDING"}:
                if choice == 1:
                    json_file = read_json(abs_path_json)
                    filtered_transactions_json = filter_by_state(json_file, status_coice.upper())
                    print(f"Для обработки выбран: {status_coice}")
                    return filtered_transactions_json
                if choice == 2:
                    csv_file = read_csv_file(abs_path_csv)
                    filtered_transactions_csv = filter_by_state(csv_file, status_coice.upper())
                    print(f"Для обработки выбран: {status_coice}")
                    return filtered_transactions_csv
                if choice == 3:
                    xlsx_file = read_xlsx_file(file_path_xlsx)
                    filtered_transactions_xlsx = filter_by_state(xlsx_file, status_coice.upper())
                    print(f"Для обработки выбран: {status_coice}")
                    return filtered_transactions_xlsx
                else:
                    print("Файл отсутствует")
                    break
            else:
                print(f"Данный статус: {status_coice} недоступен. Попробуйте снова")
        except UnboundLocalError as ex:
            print(f"Статус {status_coice} отсутствует в этом списке, ошибка х{ex}")


def sort_date() -> Any:
    """
    Функция, которая сортирует по дате: убывания и возрастания.
    """
    try:
        file_get = get_inform()
        if not file_get:
            print("Не найдено ни одной транзакции")
            return

        while True:
            print("Отсортировать операции по дате? Да/Нет")
            choice_sort = input().strip()
            if choice_sort.title() in ["Да", "Нет"]:
                break
        else:
            'Пожалуйста введите "Да" или "Нет"'

        if choice_sort.title() == "Да":

            while True:
                print("Отсортировать по возрастанию или по убыванию?")
                choice_sort_true = input().strip()
                if choice_sort_true.title() in ["Возрастанию", "Убыванию"]:
                    break
            else:
                'Пожалуйста введите "возрастанию" или "убыванию"'

            if choice_sort_true.lower() == "убыванию":
                file_sored_true = sort_by_date(file_get, sort_parameter=True)
                return file_sored_true
            elif choice_sort_true.lower() == "возрастанию":
                file_sored_false = sort_by_date(file_get, sort_parameter=False)
            return file_sored_false
        else:
            return file_get
    except Exception as ex:
        print(f"Ошибка при фильтрации транзакций: {ex}")


def sort_rub() -> Any:
    """Функция, которая фильтрует транзакции по критерию отбора: только "RUB" или все транзакции"""
    try:
        sorted_rub = sort_date()
        if not sorted_rub:  # Если список пустой, сразу возвращаем его
            return []
        while True:
            print("Выводить только рублевые транзакции? Да/Нет")
            rub_sorted_input = input().strip()
            if rub_sorted_input.title() in ["Да", "Нет"]:
                break
            else:
                'Пожалуйста введите "Да" или "Нет"'

        if rub_sorted_input.title() == "Да":
            rub_get_currency = filter_by_currency(sorted_rub, forex="RUB")  # Фильтруем только "RUB" транзакции
            if not rub_get_currency:
                print('"RUB" ранзакций не найдено')
                return []
            return rub_get_currency
        else:  # Список не изменился, передаем все транзакции
            return sorted_rub
    except Exception as ex:
        print(f"Ошибка при фильтрации транзакций: {ex}")


def look_for() -> Any:
    """
    Функция для фильтрации транзакций и подсчета их количества.
    """
    try:
        # Получаем отсортированные транзакции
        file_to_look = sort_rub()

        # Если список пустой, сразу возвращаем его
        if not file_to_look:
            print("Не найдено ни одной транзакции, подходящей под вашиm условия фильтрации")
            return []

        # Спрашиваем о фильтрации по ключевому слову
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        filter_trans_word = input().strip()

        if filter_trans_word.title() == "Да":
            print("Введите слово для поиска:")
            word_look_for = input().strip()

            # Фильтруем транзакции по ключевому слову
            filtered_transactions = look_to_dictionary(file_to_look, word_look_for)

            # Проверяем, найдены ли транзакции
            if not filtered_transactions:
                print("Не найдено транзакций с указанным ключевым словом")
                return []

            len_count = len(filtered_transactions)
            print(f"Распечатываю итоговый список транзакций\nВсего банковских операций в выборке: {len_count}")
            return filtered_transactions

        elif filter_trans_word.title() == "Нет":
            len_count_not = len(file_to_look)
            print(f"Распечатываю итоговый список транзакций\nВсего банковских операций в выборке: {len_count_not}")
            return file_to_look

        else:
            print("Некорректный ввод. Будут показаны все транзакции.")
            len_count_not = len(file_to_look)

        print(f"Распечатываю итоговый список транзакций\nВсего банковских операций в выборке: {len_count_not}")
        return file_to_look

    except TypeError as ex:
        print(f"Ошибка типа данных: {ex}")
        return []
    except Exception as ex:
        print(f"Произошла ошибка: {ex}")
        return []


def main() -> Any:
    """
    Функция, которая выводит на печать отфильтрованные транзакции в заданном формате.
    """
    print_t = look_for()  # Получаем отфильтрованные транзакции

    if not print_t:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    # Маскируем номера карт/счетов
    masked_transactions = format_card_account(print_t)

    # Проверяем, что masked_transactions - это список
    if isinstance(masked_transactions, str):
        # Если format_card_account вернул строку (ошибка)
        print(masked_transactions)
        return

    for i, d in enumerate(print_t):
        # Получаем соответствующую замаскированную транзакцию
        if i < len(masked_transactions):
            masked = masked_transactions[i]
        else:
            masked = d

        # Форматируем дату
        date_ob = parse(d["date"])
        formatted_date = date_ob.strftime("%d.%m.%Y")

        # Получаем сумму и валюту (упрощенная логика)
        amount = d.get("amount") or d.get("operationAmount", {}).get("amount")
        currency = (
            d.get("currency_code")
            or d.get("operationAmount", {}).get("currency", {}).get("code")
            or d.get("operationAmount", {}).get("currency", {}).get("name")
        )

        if d["description"] == "Открытие вклада":
            # Для вклада выводим только 'to'
            to_account = masked.get("to", "")
            print(f'{formatted_date} {d.get("description", "")}')
            print(f"{to_account}")
            print(f"Сумма: {amount} {currency}\n")
        else:
            # Для переводов выводим 'from' и 'to'
            from_account = masked.get("from", "")
            to_account = masked.get("to", "")
            print(f'{formatted_date} {d.get("description", "")}')
            print(f"{from_account} -> {to_account}")
            print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    print(main())

    print(25 * "~**~")

