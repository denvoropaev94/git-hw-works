from tabulate import tabulate


def select_action() -> int:
    print("Выберите необходимое действие")
    print("1. Поиск заметки")
    print("2. Добавить заметку")
    print("3. Удалить заметку")
    print("4. Обновить данные заметки")
    print("5. Экспортировать данные ")
    print("6. Вывести список заметок")
    print("7. Закончить работу")
    user_choice = int(input("Введите номер необходимого действия: "))

    if user_choice == 1:
        print("По какому критерию предпочитаете осуществить поиск заметки(ов)")
        print("1. Найти заметку по названию")
        print("2. Сделать выборку заметок по рубрике")
        print("3. Сделать выборку заметок по автору")
        user_choice = int(input("Введите цифру ")) + 10
        # print(user_choice)
        return user_choice
    else:
        return user_choice


def find_note():
    search_note = input("Введите название заметки: ")
    return search_note


def select_note_heading():
    select_heading = input("Введите рубрику: ")
    return select_heading


def select_note_author():
    select_author = input("Введите автора: ")
    return select_author


def add_note():
    print("Добавьте заметку: ")
    archive = {"id": ""}
    archive["name"] = (input("Введите название заметки: "))
    archive["text"] = (input("Введите текст заметки: "))
    archive["author"] = (input("Введите автора заметки: "))
    archive["number_note"] = (input("Введите номер заметки: "))
    archive["heading"] = (input("Введите рубрику заметки: "))
    return archive


def delete_note():
    del_note = input("Введите название заметки, которую хотите удалить: ")
    return del_note


def edit_note_data():
    print("Введите все данные заметки")
    edit = {"id": ""}
    edit["name"] = (input("Введите название заметки: "))
    edit["text"] = (input("Введите текст заметки: "))
    edit["author"] = (input("Введите автора заметки: "))
    edit["number_note"] = (input("Введите номер заметки: "))
    edit["heading"] = (input("Введите рубрику заметки: "))
    return edit


# def export_data():
#     return int(input("Введите 1 для экспорта в формате json или 2 для экспорта в формате csv: "))


def end_work():
    print("Программа завершена")


def print_all_notes(data):
    data_to_print = []

    for i in range(len(data)):
        listik = list(data[i].values())
        listik.pop(0)
        data_to_print.append(listik)

    col_names = ["Название", "Текст", "Автор", "Номер заметки", "Рубрика"]
    print(tabulate(data_to_print, headers=col_names, tablefmt="fancy_grid", showindex="never"))
