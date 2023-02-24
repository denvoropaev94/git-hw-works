import view
import read
import additional
import write

note_data = read.read_json()


def main_logic():
    pos = 2
    while 1 < pos < 14:
        pos = view.select_action()
        if pos == 11:
            what_find = view.find_note()
            data_to_print = additional.find_what_note(what_find, note_data)
            view.print_all_notes(data_to_print)
        if pos == 12:
            what_find = view.select_note_heading()
            data_to_print = additional.select_note_heading(what_find, note_data)
            view.print_all_notes(data_to_print)
        if pos == 13:
            what_find = view.select_note_author()
            data_to_print = additional.select_note_author(what_find, note_data)
            view.print_all_notes(data_to_print)
        if pos == 2:
            what_find = view.add_note()
            data_to_print = additional.find_what_note(what_find['name'], note_data)
            view.print_all_notes(data_to_print)
            additional.new_note_create(list(what_find.values()), note_data)
            view.print_all_notes(note_data)
            write.write_json(note_data)
            write.write_csv(note_data)
        if pos == 3:
            what_find = view.delete_note()
            additional.delet_what_note(what_find, note_data)
            view.print_all_notes(note_data)
            write.write_json(note_data)
            write.write_csv(note_data)
        if pos == 4:
            note_list = list(view.edit_note_data().values())
            additional.choose_what_note(note_list, note_data)
            view.print_all_notes(note_data)
            # print(note_data)
            write.write_json(note_data)
            write.write_csv(note_data)
        if pos == 5:
            what_save = view.export_data()
            if what_save == 1:
                write.write_json(note_data)
            elif what_save == 2:
                write.write_csv(note_data)
            else:
                print('Некорректный ввод')
        if pos == 6:
            view.print_all_notes(note_data)
        if pos == 7:
            view.end_work()
            break
