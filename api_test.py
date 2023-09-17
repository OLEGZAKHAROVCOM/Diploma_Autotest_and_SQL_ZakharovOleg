from config import API_URL, HEADERS  # Импорт констант из config.py
import requests  # Импорт библиотеки для отправки HTTP-запросов

# Функция для создания нового заказа
def create_order():
    # Формируем URL для создания заказа, используя базовый URL из конфигурационного файла
    url = f"{API_URL}/api/v1/orders"

    # Формируем тело запроса с необходимыми параметрами для создания заказа
    payload = {
        "firstName": "Иван",
        "lastName": "Петров",
        "address": "Ивановская, 12",
        "metroStation": 4,
        "phone": "+78003553535",
        "rentTime": 5,
        "deliveryDate": "2023-09-15",
        "comment": "Комментарий",
        "color": ["BLACK"]
    }

    # Отправляем POST-запрос к API для создания заказа
    response = requests.post(url, json=payload, headers=HEADERS)

    # Проверяем код ответа: если 201, то заказ успешно создан
    if response.status_code == 201:
        # Возвращаем трек-номер заказа для дальнейших операций
        return response.json()['track']
    else:
        # В случае ошибки возвращаем None
        return None

# Функция для получения информации о заказе по его трек-номеру
def get_order_by_track(track):
    # Формируем URL для запроса информации о заказе
    url = f"{API_URL}/api/v1/orders/track?t={track}"

    # Отправляем GET-запрос к API для получения информации о заказе
    response = requests.get(url, headers=HEADERS)

    # Проверяем код ответа: если 200, то информация о заказе успешно получена
    if response.status_code == 200:
        # Возвращаем всю полученную информацию о заказе
        return response.json()
    else:
        # В случае ошибки возвращаем None
        return None

# Точка входа в программу
if __name__ == "__main__":
    # Пытаемся создать новый заказ
    track = create_order()
    # Если заказ создан успешно
    if track:
        print(f"Заказ создан с номером трека: {track}")
        # Получаем информацию о созданном заказе
        order_info = get_order_by_track(track)
        # Если информация успешно получена
        if order_info:
            print(f"Информация о заказе: {order_info}")
        else:
            print("Не удалось получить информацию о заказе.")
    else:
        print("Не удалось создать заказ.")