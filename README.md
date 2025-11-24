# My homework from 05/10/25
## В модулях:
### masks.py
* функция get_mask_card_number, которая принимает номер карты, а выводит только первые 6 цифр карты и последние 4,
    а вместо остальных ставит **(звездочки)
* функция get_mask_account,принимает номер счета, а выводит только последние 4 цифры,
    а вместо последних 5 и 6 цифр ставит **(звездочки)
### widget.py
* функция mask_account_card, которая функция принимает на вход строку для маскировки номера карты/счета и используются 
ранее написанные функции get_mask_card_number и get_mask_account.
* функция get_date, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает 
строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
### processing.py
* функция filter_by_state, которая принимает список словарей и опционально значение для ключа 
state  (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 
state соответствует указанному значению;
* функция sort_by_date, которая принимает список словарей и необязательный параметр, задающий порядок сортировки 
(по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (
date).
### generators.py
* функция filter_by_currency, которая принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции, где валюта операции соответствует задан-
    ной (например, USD).
* функция transaction_descriptions, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
* генератор card_number_generator, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где
    X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до
    9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.
### decorators.py
* функция-декоратор log, декоратор может логировать работу функции и ее результат как в файл, так и в консоль
### utils.py
* функция read_json для чтения JSON-файла принимает путь к файлу JSON в качестве аргумента и возвращает список словарей с данными о финансовых транзакциях.
### external_api.py
* функция get_transaction_amount принимает на вход одну транзакцию и возвращает сумму транзакции в рублях
### read_file_csv_xlsx.py
* функция read_csv_file для считывания финансовых операций из CSV принимает путь к файлу CSV в качестве аргумента.
* функция read_xlsx_file для считывания финансовых операций из Excel  принимает путь к Excel файлу в качестве аргумента.
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
## Код для функции-декоратора log 
```
def log(filename="None"):
    def wrapper(function):
        @wraps(function)
        def time_log(*args, **kwargs):
            try:
                result = function(*args, *kwargs)
                message = f"\nName function: {function.__name__} Result: {result}"
                if filename:
                    with open(filename, "a") as f:
                        f.write(message)
                else:
                    print(message)
                return result
            except Exception as e:
                error_message = f"Name function: {function.__name__} error: {e}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(error_message)
                else:
                    print(error_message)
                raise e
        return time_log
    return wrapper
```
## Код для функции read_json(filename)
```
def read_json(filename: str) -> list:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            operations_file = json.load(f)
            if not isinstance(operations_file, list):
                raise TypeError("JSON-файл должен содержать список.")
        return operations_file
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути {filename}")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: Файл '{filename}' пустой.")
        return []

```
## Код для функции get_transaction_amount(transaction)
```
def get_transaction_amount(transaction: Dict) -> float:
    if "operationAmount" in transaction:
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            return round(float(transaction["operationAmount"]["amount"]), 2)
        if transaction["operationAmount"]["currency"]["code"] in ["EUR", "USD"]:
            url = f"https://api.apilayer.com/currency_data/convert"
            payload = {
                "to": "RUB",
                "from": transaction["operationAmount"]["currency"]["code"],
                "amount": transaction["operationAmount"]["amount"],
            }
            headers = {"apikey": API_KEY}
            response = requests.get(url, headers=headers, params=payload)
            status_code = response.status_code
            result = response.json()
            print(result)
            if status_code == 200:
                return round(result["result"], 2)
            else:
                print("Не удалось перевести валюту в рубли")
                return status_code
```
## Код для функции read_csv_file(data_file_csv):
```
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
   ```
## Код для функции read_xlsx_file(data_file_xlsx):
```
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
```
### Пример входных данных для проверки 
1) функция get_mask_card_number()

    7000 79** **** 6361

2) функция get_mask_account()

    **4305

3) функция mask_account_card()
    
    Visa Platinum 7000 79** **** 6361
    Счет **4305

4) функция get_date()
    11.03.2024

5) функция filter_by_state()

[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

6) функция filter_by_state()

[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

8) функция filter_by_currency
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}
{'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}

9) функция transaction_descriptions()
Перевод организации
Перевод со счета на счет

10) функция card_number_generator()
 0000 0000 0000 0001
11) функция-декоратор log()
Name function: sum_num Result: 30Name function: dividing error: division by zero. Inputs: (10, 0), {}
Name function: sum_num Result: 30Name function: dividing Result: 10.0
12) функция read_json(filename)
[{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'},
13) функция get_transaction_amount(transaction)
794466.42 
Не удалось перевести валюту в рубли
429
14) функция read_csv_file(data_file_csv):
[{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'}, {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': '29740', 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'}, {'id': '593027', 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': '30368', 'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'}]
15) функция read_xlsx_file(data_file_xlsx):
[{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0, 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'}, {'id': 3598919.0, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740.0, 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'}, {'id': 593027.0, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': 30368.0, 'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},]

## Тесты
1) К функциям get_mask_card_number и get_mask_account тесты написаны в тестовом файле test_masks.py, функциональный код покрыт тестами на 100%.
2) К функциям mask_account_card и get_date тесты написаны в тестовом файле test_widget.py, функциональный код покрыт тестами на 100%.
3) К функциям filter_by_state и sort_by_date тесты написаны в тестовом файле test_processing, функциональный код покрыт тестами на 100%.
4) К функциям filter_by_currency, transaction_descriptions и card_number_generator тесты написаны в тестовом файле test_generators, функциональный код покрыт тестами на 100%.
5)  К функция-декоратор log() тест написан в тестовом файле test_decorators, функциональный код покрыт тестами на 79%.
6) К функция read_json() тест написан в тестовом файле test_read_json, функциональный код покрыт тестами на 61%.
7) К функция get_transaction_amount() тест написан в тестовом файле test_get_transaction_amount, функциональный код покрыт тестами на 82%.
8)  К функция read_csv_file(data_file_csv) тест написан в тестовом файле test_csv_file, функциональный код покрыт тестами на 71%.
9)  К функция read_xlsx_file(data_file_xlsx) тест написан в тестовом файле test_xlsx_file, функциональный код покрыт тестами на 71%.
