import json
import os
import tempfile
from typing import Union
from unittest.mock import mock_open, patch

import pytest

from src.utils import read_json


def test_read_valid_json() -> None:
    mock_data = [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"}]

    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        result = read_json("test.json")

    assert result == mock_data
    assert isinstance(result, list)
    assert len(result) == 1


@pytest.mark.parametrize(
    "json_content,expected_error",
    [
        ('{"not": "a list"}', TypeError),  # Не список
        ("[invalid json", json.JSONDecodeError),  # Некорректный JSON
    ],
)
def test_multiple_cases(json_content: str, expected_error: Union[TypeError]) -> None:
    """Параметризованный тест для различных случаев"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        f.write(json_content)
        temp_filename = f.name

    try:
        if expected_error == TypeError:
            with pytest.raises(TypeError):
                read_json(temp_filename)
        else:
            # Для JSONDecodeError функция возвращает строку с ошибкой
            result = read_json(temp_filename)
            assert "Ошибка: Файл" in result
    finally:
        os.unlink(temp_filename)
