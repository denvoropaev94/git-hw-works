
key_data = ['id', 'name', 'text', 'author', "number_note", "heading"]


def last_id(data):
    id_list = [i["id"] for i in data if type(i["id"]) is int]
    return max(id_list)


# Найти заметку

def find_what_note(what_find, data): #только одно слово - название
    return [i for i in data if i['name'] == what_find]


# Сделать выборку заметок по рубрике
def select_note_heading(select_heading, data):
    return [i for i in data if i['heading'] == select_heading]

# Сделать выборку сотрудников по автору

def select_note_author(select_author, data):
    return[i for i in data if i['author'] == select_author]

# Добавление заметки без проверки
def note_add_data(user_list, data_new):
    new_note = dict(zip(key_data, user_list))
    new_note["id"] = last_id(data_new) + 1
    return data_new.append(new_note)

# Создание новой заметки
def new_note_create(user_list, data_new):
    name = user_list[1]
    if len(find_what_note(name, data_new)) != 0:
        print("Похожая заметка есть! ")
        print(find_what_note(name, data_new))
        print('Хотите изменить строчку? ')
        user_choose = int(input('Добавить - 1, изменить строчку - 2: '))

        if user_choose == 1:
            note_add_data(user_list, data_new)
        elif user_choose == 2:
            id_old = int(input(("Введите id строки, которую надо изменить: ")))
            index_el = 0
            for i in range(len(data_new)):
                if data_new[i]["id"] == id_old:
                    index_el = i
                    break
            new_note = dict(zip(key_data, user_list))
            new_note["id"] = id_old
            data_new[index_el] = new_note
    else: note_add_data(user_list, data_new)


# Удалить заметку
def delet_what_note(del_note, data):
    if len(find_what_note(del_note, data)) != 0:
        print("Похожая заметка уже есть")
        print(find_what_note(del_note, data))
        user_choose = int(input('Какую строчку вы хотите удалить? Введите id строчки'))
        index_el = None
        for i in range(len(data)):
            if data[i]["id"] == user_choose:
                index_el = i
                break
        del data[index_el]
    else:
        print("Похожая заметка не найдена!")


def choose_what_note(edit, data): # добавили переменную edit из view, в которой находятся данные от пользователя
    name = edit[1]
    if len(find_what_note(name, data)) != 0:
        print("Похожая заметка есть")
        print(find_what_note(name, data))
        print('Какую строчку вы хотите удалить? Введите id строчки')
        user_choose = int(input('Какую строчку вы хотите удалить? Введите id строчки'))
        index_el = 0
        for i in range(len(data)):
            if data[i]["id"] == user_choose:
                index_el = i
                break
        new_note = dict(zip(key_data, edit))
        new_note["id"] = user_choose
        data[index_el] = new_note
    else:
        print("Похожая заметка не найдена!")
