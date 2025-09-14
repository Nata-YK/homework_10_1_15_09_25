# My homework from 14.09.2025
## В модуле processing
1) функция filter_by_state, которая принимает список словарей и опционально значение для ключа 
state  (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 
state соответствует указанному значению;
2) функция sort_by_date, которая принимает список словарей и необязательный параметр, задающий порядок сортировки 
(по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (
date).
3) код для функции filter_by_state
```
def filter_by_state(list_diction: Iterable[dict], state='EXECUTED') -> Iterable[dict]:
    new_diction = []
    for k in list_diction:
        if k['state'] == state:
            new_diction.append(k)
    return new_diction
```
4) код для функции sort_by_date
```
def sort_by_date(list_diction: Iterable[dict])-> Iterable[dict]:
    sorted_list_data = sorted(list_diction, key=lambda x: x['date'], reverse=True)
    return sorted_list_data
```
### Пример входных данных для проверки 
1) функция filter_by_state

[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
2) функция filter_by_state

[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]