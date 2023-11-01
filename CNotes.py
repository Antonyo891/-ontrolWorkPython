import random, json, os, time
from collections import OrderedDict
from NoteController import NoteController
from FileWork import save
from FileWork import load
from ClassNote import Note


def Menu():
    print()
    print('1 - Добавить новую заметку')
    print('2 - Сохранить заметки')
    print('3 - Изменить заметку')
    print('4 - Показать заметки')
    print('5 - Сохранить и выйти')
    print('6 - Удалить заметку')


  
os.system('cls')
load_from_file: OrderedDict = load()
if load_from_file==None:
    print("У вас нет заметок")
else:
    print("Загрузка заметок выполнена успешно")
    print(f"У вас {len(load_from_file)} заметок.")
# notes:list = list()
note_controller:NoteController = NoteController()
if load_from_file!=None:
    for item in load_from_file:
        temp_heading = item
        temp_dict_created = load_from_file[item]
        temp_note = temp_dict_created["note"]
        temp_note_id = temp_dict_created["note_id"]
        temp_time_of_created = temp_dict_created["time_of_created"]
        note:Note = Note(temp_heading,temp_note,temp_note_id, temp_time_of_created)
        note_controller.AddNote(note)

while True:
    Menu()
    command = input("Введите номер команды: ")
    if command == "1":
        note_controller.CreateNote()
        os.system('cls')
        print("Заметка добавлена")
    elif command == "4":
        os.system('cls')
        print("Список всех заметок:")
        read_notes: dict = note_controller.ReadNotes()
        keys = read_notes.keys()
        try:
            choise: int = int(input("Введите номер заметки для просмотра" +
                            "(либо нажмите ввод для выхода в меню): "))
            if  choise in keys:
                os.system('cls')
                note_controller.GetNote(read_notes[choise])
                input("Нажмите Enter")
        except:
            os.system('cls')
    elif command == "3":
        os.system('cls')
        name = input("Введите название заметки для изменения: ")
        note_controller.EditNote(name)
    elif command == "2":
        os.system('cls')
        notes_for_load = OrderedDict()
        notes = note_controller.GetNotesList()
        for item in notes:
            note_temp:Note = item
            temp_dict = note_temp.GetNote()
            notes_for_load.update(temp_dict)
        save(notes_for_load)
    elif command == '5':
        os.system('cls')
        notes_for_load = OrderedDict()
        notes = note_controller.GetNotesList()
        for item in notes:
            note_temp:Note = item
            temp_dict = note_temp.GetNote()
            notes_for_load.update(temp_dict)
        save(notes_for_load)
        print("До скорого")
        break
    elif command == "6":
        os.system('cls')
        name = input("Введите название заметки для удаления: ")
        note_controller.RemoveNote(name)
    else:
        print(f"Вы ввели недопустимый символ {command}")