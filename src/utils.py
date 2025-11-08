import json
from typing import Union, Any


def read_json(filename: str) -> tuple[str, set[str]]:
    """
    Функция чтения JSON-файла принимает путь к файлу JSON в качестве аргумента и возвращает список словарей с данными
    о финансовых транзакциях.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            operations_file = json.load(f)
            if not isinstance(operations_file, list):
                raise TypeError("JSON-файл должен содержать список.")
        return operations_file
    except FileNotFoundError or PermissionError:
        return "Ошибка: Файл не найден по пути", {filename}
    except json.JSONDecodeError:
        return "Ошибка: Файл пустой.", {filename}
