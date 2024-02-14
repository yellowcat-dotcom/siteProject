import requests

# Устанавливаем токен в заголовок Authorization
token = 'b1825e6cfc36d8942fbb7e5bdf175a0571c16288'
headers = {'Authorization': f'Token {token}'}

# URL эндпоинта, который вы хотите запросить
url = 'http://127.0.0.1:8000/api/reservations/'

data = {
    'meeting_room': 1,  # Замените на ID нужной комнаты
    'start_time': '2024-07-20T10:00:00Z',  # Замените на нужное время начала
    'end_time': '2024-07-20T11:00:00Z',    # Замените на нужное время окончания
}
# Выполняем POST-запрос с токеном в заголовке и данными в теле запроса
response = requests.post(url, headers=headers, data=data)

# Выполняем GET-запрос с токеном в заголовке
#response = requests.get(url, headers=headers)

# Обработка ответа
if response.status_code == 201:  # Код 201 означает, что запись успешно создана (Created)
    print("Бронирование успешно создано.")
    data = response.json()
    print(headers)
    # Ваши действия с данными, если необходимо
else:
    print(f"Ошибка: {response.status_code} - {response.text}")