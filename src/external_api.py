import os

from dotenv import load_dotenv
import requests

from src.utils import read_json

load_dotenv() # Загружаем переменные из окружения .env

API_KEY = os.getenv('API_KEY')

def get_transaction_amount(transactions_list):
    list_total_rub = []
    for transaction in transactions_list:
        if 'operationAmount' in transaction:
            if transaction['operationAmount']['currency']['code'] == 'RUB':
                list_total_rub.append(float(transaction['operationAmount']['amount']))
            if transaction['operationAmount']['currency']['code'] in ['EUR', 'USD']:
            #elif transaction['operationAmount']['currency']['code'] == 'EUR' or 'USD':
                url = f'https://api.apilayer.com/exchangerates_data/convert'
                payload = {
                    'to': 'RUB',
                    'from': transaction['operationAmount']['currency']['code'],
                    'amount': transaction['operationAmount']['amount']
                }
                headers = {"apikey":API_KEY}
                response = requests.get(url, headers=headers, params=payload)
                status_code = response.status_code
                result = response.json()
                print(result)
                if status_code == 200:
                    print(result["amount"])
                    list_total_rub.append(result['result'])
                    #return (result['result'])
                else:
                    print('Не удалось перевести валюту в рубли')
                    return(status_code)
        else:
            return('Нет информации о сумме транзакции')
    return list_total_rub


if __name__ == "__main__":
    # print(read_json('../data/operations.json'))
    print(get_transaction_amount(read_json('../data/operations.json')))

