import sender_stand_request
import data


def get_new_track(order_response):
    """Извлекает трек-номер из ответа на создание заказа."""
    return order_response.json().get("track")


def positive_assert():
    """Проверяет успешность получения данных о заказе по трек-номеру."""
    # Создаем новый заказ
    order_response = sender_stand_request.post_new_order(data.order_body)

    # Получаем трек-номер из ответа на создание заказа
    track_number = get_new_track(order_response)

    # Сохраняем трек-номер для последующего запроса
    data.params_get["t"] = track_number

    # Выполняем запрос на получение данных о заказе по трек-номеру
    track_response = sender_stand_request.get_order(data.params_get["t"])

    # Проверяем, что код ответа равен 200
    assert track_response.status_code == 200


def test_order():
    """Основная функция теста."""
    positive_assert()

# Алина Петрова, 20А когорта — Финальный проект. Инженер по тестированию плюс