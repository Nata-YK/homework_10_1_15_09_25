import csv
from typing import Dict

import pandas as pd


def read_csv_file(data_file_csv: str) -> Dict:
    """
    Функция  для считывания финансовых операций из CSV принимает путь к файлу CSV в качестве аргумента.
    """
    try:
        result = []
        with open(data_file_csv, encoding="utf-8") as file_csv:
            data_file_csv_read = csv.DictReader(file_csv, delimiter=";")
            for row in data_file_csv_read:
                result.append(row)
        return result
    except FileNotFoundError:
        return f"Ошибка: файл {data_file_csv} не найден по пути"
    except PermissionError:
        return f"Ошибка: к файлу {data_file_csv} нет прав с доступом"
    except Exception as ex:
        return f"Ошибка: Файл {data_file_csv} {ex}."


def read_xlsx_file(data_file_xlsx) -> Dict:
    """
    Функция  для считывания финансовых операций из Excel  принимает путь к Excel файлу в качестве аргумента.
    """
    try:
        data_file_xlsx_read = pd.read_excel(data_file_xlsx)
        result_dict = data_file_xlsx_read.to_dict(orient="records")
        return result_dict
    except FileNotFoundError:
        return f"Ошибка: файл {data_file_xlsx} не найден по пути"
    except PermissionError:
        return f"Ошибка: к файлу {data_file_xlsx} нет прав с доступом"
    except Exception as ex:
        return f"Ошибка: Файл {data_file_xlsx} {ex}."
