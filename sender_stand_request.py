import requests
import configuration
import data

#   Создаётся новый пользователь
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=user_body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())
#   Берем authToken с ответа и передаем в "новый набор"
auth_token = response.json().get("authToken")


#  Создаётся новый набор с authToken созданного пользователя
def post_new_client_kit(kit_body, auth_token):
    auth_headers = data.headers.copy()
    auth_headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_PRODUCTS_KIT_PATH,
                         json=kit_body,
                         headers=auth_headers)

response = post_new_client_kit(data.kit_body, auth_token)
print(response.status_code)
print(response.json())