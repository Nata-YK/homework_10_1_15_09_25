from typing import Iterable


def filter_by_state(list_diction: Iterable[dict], state='EXECUTED') -> Iterable[dict]:
    """
    Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению.
    """
    new_diction = []
    for k in list_diction:
        if k['state'] == state:
            new_diction.append(k)
    return new_diction