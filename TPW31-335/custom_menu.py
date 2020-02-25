import sys


def create():
    print("Пользователь выбрал создание записи")


def find():
    print("Пользователь выбрал найти записи")


def edit():
    print("Пользователь выбрал редактировать записи")


def delete():
    print("Пользователь выбрал удалить записи")


def close():
    print("Пользователь выбрал выход из программы")
    sys.exit(0)


def show_menu():
    print("Меню")
    print("1.Создать запись")
    print("2.Найти запись")
    print("3.Редактировать запись")
    print("4.Удалить записи")
    print("5.Выйти из програмы")
    on_item_selected()


def on_item_selected():
    try:
        selected = int(input("Выбирите действие:"))

        if selected == 1:
            create()
        elif selected == 2:
            find()
        elif selected == 3:
            edit()
        elif selected == 4:
            delete()
        elif selected == 5:
            close()
        else:
            print("Введите число от 1 до 5")
            on_item_selected()

    except ValueError:
        print("Введите число от 1 до 5")
        on_item_selected()
