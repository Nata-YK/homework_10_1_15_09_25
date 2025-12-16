from typing import Any
from unittest.mock import Mock, patch

from src.external_api import get_transaction_amount


@patch("src.external_api.requests.get")
def test_get_transaction_amount(mock_get: Any) -> None:
    # Создаем мок ответа
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"success": True, "result": 795261.68}
    mock_get.return_value = mock_response

    # Тестовые данные
    test_transaction = {"state": "EXECUTED", "operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}}}

    # Вызываем функцию
    result = get_transaction_amount(test_transaction)

    # Проверяем результат
    assert result == 795261.68

    # Проверяем, что requests.get был вызван с правильными параметрами
    expected_url = "https://api.apilayer.com/exchangerates_data/convert"
    expected_params = {"to": "RUB", "from": "USD", "amount": "9824.07"}

    # Получаем фактический API_KEY из вашего модуля
    from src.external_api import API_KEY

    expected_headers = {"apikey": API_KEY}

    mock_get.assert_called_once_with(expected_url, headers=expected_headers, params=expected_params)
