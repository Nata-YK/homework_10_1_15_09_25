from typing import Iterable, List, Union


def filter_by_state(list_diction: Iterable[dict], state: Union[str] = "EXECUTED") -> List[dict]:
    """
    Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению.
    """
    filtered_transactions = []
    for k in list_diction:
        if k.get("state") == state:
            filtered_transactions.append(k)
    return filtered_transactions


def sort_by_date(list_diction: Iterable[dict], sort_parameter: bool = True) -> List[dict]:
    """
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date).
    """
    sorted_list_data = sorted(list_diction, key=lambda x: x["date"], reverse=sort_parameter)
    return sorted_list_data
