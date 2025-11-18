import json
from unittest.mock import mock_open, patch

from src.utils import read_json


def test_read_valid_json() -> None:
    mock_data = [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"}]

    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        result = read_json("test.json")

    assert result == mock_data
    assert isinstance(result, list)
    assert len(result) == 1
