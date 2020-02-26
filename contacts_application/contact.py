import re

import database


def create_contact():
    first_name = input("Введите имя:")
    second_name = input("Введите фамилию:")
    phone = read_phone_input()

    database.create(first_name, second_name, phone)
    print("Контакт сохранен в БД")


def read_phone_input():
    while True:
        phone = input("Введите телефон:")
        if not re.match(r'\d{10,12}', phone):
            print("Телефон введен некорректно. Используйте только цифры")
        else:
            return phone
