import requests

# pip install requests
url = "https://api.nbp.pl/api/exchangerates/rates/A/USD/"

response = requests.get(url)
print(response)  # <Response [200]>
# 200 ok
# 3xx warning, przekierowanie
# 4xx błedy po stronie klienta 404, 400 Bad Request
# 5xx błedy po stronie serwera 500 Internal Server Error

print(response.text)
data = response.json()
print(type(data))  # <class 'dict'>
print(data['currency'])  # dolar amerykański

print(data['rates'])
# [
# {'no': '200/A/NBP/2025', 'effectiveDate': '2025-10-15', 'mid': 3.6585}
# ]
print(data['rates'][0])
# {'no': '200/A/NBP/2025', 'effectiveDate': '2025-10-15', 'mid': 3.6585}
print(data['rates'][0]['mid'])  # 3.6585
