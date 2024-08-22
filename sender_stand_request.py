import requests
import configuration

def post_new_order(body):
    """Функция для создания нового заказа."""
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=body)

def get_order(track_number):
    """Функция для получения данных о заказе по трек-номеру."""
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK, params={"t": track_number})
