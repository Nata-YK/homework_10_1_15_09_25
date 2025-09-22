# My homework from 22.09.2025
## В модулях:
### masks
* функция get_mask_card_number, которая принимает номер карты, а выводит только первые 6 цифр карты и последние 4,
    а вместо остальных ставит **(звездочки)
* функция get_mask_account,принимает номер счета, а выводит только последние 4 цифры,
    а вместо последних 5 и 6 цифр ставит **(звездочки)
### widget
* функция mask_account_card, которая функция принимает на вход строку для маскировки номера карты/счета и используются 
ранее написанные функции get_mask_card_number и get_mask_account.
* функция get_date, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает 
строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
### processing
* функция filter_by_state, которая принимает список словарей и опционально значение для ключа 
state  (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 
state соответствует указанному значению;
* функция sort_by_date, которая принимает список словарей и необязательный параметр, задающий порядок сортировки 
(по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (
date).
## Kод для функции get_mask_card_number
```
def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    card_num = []
    card_number_str = str(card_number)
    star_sp = "** **** "
    for num in card_number_str:
        card_num.append(num)
        card_widget = "".join(card_num[:4]) + " " + "".join(card_num[4:6]) + star_sp + "".join(card_num[-4:])
    return card_widget
```
## Kод для функции get_mask_account
```
def get_mask_account(account_number: Union[str]) -> Union[str]:
    account_num = []
    account_number_str = str(account_number)
    star_spice = "**"
    for num in account_number_str:
        account_num.append(num)
        account_widget = star_spice + "".join(account_num[-4:])
    return account_widget
```
## Kод для функции mask_account_card
```
def mask_account_card(information_number: Union[str]) -> Union[str]:
    card_split = information_number.rsplit(" ", 1)
    num_card = card_split[1]
    if card_split[0] == "Счет":
        return f"{card_split[0]} {get_mask_account(num_card)}"
    else:
        return f"{card_split[0]} {get_mask_card_number(num_card)}"
```
## Kод для функции get_date
```
def get_date(listing_date: Union[str]) -> Union[str]:
    data_ = []
    point = "."
    for d in listing_date:
        data_.append(d)
    return "".join(data_[8:10]) + point + "".join(data_[5:7]) + point + "".join(data_[:4])
```
## Kод для функции filter_by_state
```
def filter_by_state(list_diction: Iterable[dict], state='EXECUTED') -> Iterable[dict]:
    new_diction = []
    for k in list_diction:
        if k['state'] == state:
            new_diction.append(k)
    return new_diction
```
## Код для функции sort_by_date
```
def sort_by_date(list_diction: Iterable[dict])-> Iterable[dict]:
    sorted_list_data = sorted(list_diction, key=lambda x: x['date'], reverse=True)
    return sorted_list_data
```
### Пример входных данных для проверки 
1) функция get_mask_card_number

    7000 79** **** 6361

2) функция get_mask_account

    **4305

3) функция mask_account_card
    
    Visa Platinum 7000 79** **** 6361
    Счет **4305

4) функция get_date
    11.03.2024

5) функция filter_by_state

[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

6) функция filter_by_state

[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

## Тесты
1) К функциям get_mask_card_number и get_mask_account тесты написаны в тестовом файле test_masks.py, функциональный код покрыт тестами на 96%.
2) К функциям mask_account_card и get_date тесты написаны в тестовом файле test_widget.py, функциональный код покрыт тестами на 100%.
3) К функциям filter_by_state и sort_by_date тесты написаны в тестовом файле test_processing, функциональный код покрыт тестами на 100%.