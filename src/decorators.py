from functools import wraps
from time import time
from typing import Union, Iterable



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


@log(filename="mylog.txt")
def sum_num(*args):
    return sum(args)


@log(filename="")
def filter_by_state_1(list_diction: Iterable[dict], state: Union[str] = "") -> list[dict]:
    filtered_transactions = []
    for k in list_diction:
        if k.get("state") == state:
            filtered_transactions.append(k)
    return filtered_transactions

sum_num(1,2,5,6,7,8,0,1)


filter_by_state_1([
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ])

@log(filename="mylog.txt")
def dividing(x,y):
    return x / y


print(dividing(10,1))
