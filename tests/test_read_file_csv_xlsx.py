import os
from typing import Any, Dict
from unittest.mock import mock_open, patch, Mock

import pandas as pd

from src.read_file_csv_xlsx import read_csv_file, read_xlsx_file


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="id;state;date;amount;currency_name;currency_code;from;to;description\n650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n",
)
def test_read_csv_file(mock_open: Any) -> None:
    result = read_csv_file("path_to_file.csv")
    expected = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    assert result == expected


def test_read_scv_file_not_file() -> None:
    file_path = os.path.join("data", "transactions..csv")
    assert read_csv_file(file_path) == f"Ошибка: файл {file_path} не найден по пути"


@patch("pandas.read_excel")
def test_read_xlsx_file(mock_get: Mock, transactions: Dict) -> None:
    mock_get_return_value = transactions
    mock_get.return_value = pd.DataFrame(mock_get_return_value)

    result = read_xlsx_file("path_to_file.xlsx")
    assert result == transactions


def test_read_xlsx_file_not_file() -> None:
    file1_path = os.path.join("data", "transactions_excel1.xlsx")
    assert read_xlsx_file(file1_path) == f"Ошибка: файл {file1_path} не найден по пути"
