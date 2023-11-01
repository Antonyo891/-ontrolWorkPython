import random, json, os, time
from collections import OrderedDict
from NoteController import NoteController
from FileWork import save
from FileWork import load
from ClassNote import Note
# notes = {"Дядя Петя": {"phone_numbers": [9998881234, 9997772233], "birth_day": "121276", "email": "mail@mail.ss"}, 
#               "Тетя Песя": {"phone_numbers": [9998881444]}}

def Menu():
    print()
    print('1 - Добавить новую заметку')
    print('2 - Сохранить заметки')
    print('3 - Изменить заметкы')
    print('4 - Показать заметки')
    print('5 - Сохранить и выйти')



    
os.system('cls')
load_from_file: OrderedDict = load()
print("Загрузка заметок выполнена успешно")
notes:list = list()
for item in load_from_file:
    notes.append(Note(item))
note_controller:NoteController = NoteController()
while True:
    Menu()
    command = input("Введите номер команды: ")
    if command == "1":
        note_controller.CreateNote()
        os.system('cls')
        print("Заметка добавлена")
    elif command == "4":
        os.system('cls')
        print("Список всех контактов")
        print(notes)
    elif command == "3":
        os.system('cls')
        name = input("Введите имя для поиска: ")
        if name in notes:
            print(name, notes[name])
    elif command == "2":
        save()
    elif command == '5':
        break """