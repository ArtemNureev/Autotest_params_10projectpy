import data
import sender_stand_request


# Функция для изменения значения в параметре name в теле запроса
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body


# Функция для позитивной проверки
def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, sender_stand_request.auth_token)
    assert kit_response.json()["name"] == name
    assert kit_response.status_code == 201


# Функция для негативной проверки
def negative_assert(name):
    kit_body_negative = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body_negative, sender_stand_request.auth_token)
    assert kit_response.status_code == 400


# Тесты
# 1 Допустимое количество символов (1):
def test_create_kit_1_symbol_in_name_get_success_response():
    positive_assert("a")


# 2 Количество max (511):
def test_create_kit_511_in_name_get_success_response():
    positive_assert(
        "ааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа")


# 3 Разрешены английские буквы:
def test_create_kit_english_in_name_get_success_response():
    positive_assert("QWErty")


# 4 Разрешены русские буквы:
def test_create_kit_russian_in_name_get_success_response():
    positive_assert("Мария")


# 5 Разрешены спецсимволы:
def test_create_kit_has_special_sym_in_name_get_success_response():
    positive_assert('"№%@",')


# 6 Разрешены пробелы:
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert("Человек и КО")


# 7 Разрешены цифры(строка):
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert("123")


# 8 Пусто:
def test_create_kit_empty_name_get_error_response():
    negative_assert("")


# 9 Количество символов больше допустимого (512):
def test_create_kit_512_in_name_get_error_response():
    negative_assert(
        "аааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа")


# 10 Параметр не передан в запросе:
def test_create_kit_no_name_get_error_response():
    current_kit_body_negative_noname = data.kit_body.copy()
    current_kit_body_negative_noname.pop("name")
    negative_assert(current_kit_body_negative_noname)


#   11 Ошибка. Тип параметра name: число
def test_create_kit_number_type_name_get_error_response():
    negative_assert(123)
