import json
import logging

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_json(filename: str) -> tuple[str, set[str]]:
    """
    Функция чтения JSON-файла принимает путь к файлу JSON в качестве аргумента и возвращает список словарей с данными
    о финансовых транзакциях.
    """
    try:
        logger.debug(f"Безопасное открытие файла {filename}")
        with open(filename, "r", encoding="utf-8") as f:
            logger.info(f"файл {filename} имеет JSON-формат")
            operations_file = json.load(f)
            if not isinstance(operations_file, list):
                logger.warning(f"JSON-файл {filename} должен быть списком")
                raise TypeError("JSON-файл должен содержать список.")
        return operations_file
    except FileNotFoundError or PermissionError:
        logger.error(f"Ошибка: файл {filename} не найден по пути")
        return f"Ошибка: файл {filename} не найден по пути"
    except json.JSONDecodeError as ex:
        logger.error(f"Ошибка: Файл {filename} {ex}.")
        return f"Ошибка: Файл {filename} {ex}."
