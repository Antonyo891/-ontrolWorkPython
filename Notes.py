import random, json, os, time
from collections import OrderedDict

# notes = {"Дядя Петя": {"phone_numbers": [9998881234, 9997772233], "birth_day": "121276", "email": "mail@mail.ss"}, 
#               "Тетя Песя": {"phone_numbers": [9998881444]}}

notes = OrderedDict()

class TimeStamp:
    def __init__(self) -> None:
        second = time.time()
        date = time.localtime(second)
        self.ti = str(time.asctime(date))

    def GetTime(self) -> str:
        return self.ti

class Note:
    def __init__(self,heading:str, note:str, note_id:int) -> None:
        self.heading = heading
        self.note = note
        self.note_id = note_id
        self.time_of_created = TimeStamp().GetTime
    
    def PrintNote(self):
        print(f" \n Id = {self.note_id} Created at {self.time_of_created}  ")
        print(f" \n Note {self.heading}:\n {self.note} ")
    
    def GetNote(self)-> dict:
        value = {"time_of_created":self.time_of_created,"note_id":self.note_id, 
                 "note":self.note}
        return {self.heading:value}
    
    def SetNote(self, note: str):
        self.note = note
     
def save(notes:OrderedDict):
    with open("notes.json", "w", encoding="utf-8") as fh:
        try:
            fh.write(json.dumps(notes, ensure_ascii=False))
            print("Notes saved successfully")
        except:
            print("Saving failed with an error")

def load():
    # global notes
    with open("notes.json", "r", encoding="utf-8") as fh:
        try:
            notes = json.load(fh)
            print("The notes were uploaded successfully")
        except:
            print("Loading failed with an error")
    return notes

def Delete(notes:OrderedDict) -> OrderedDict:
#    with open("notes.json", "r", encoding="utf-8") as fh:
#        try:
#            notes = OrderedDict(json.load(fh))
#        except:
#            print("failed to upload file")
    os.system('cls')
    print(*notes)
    name = input("Enter the note title")
    while name not in notes:
        name=input(f"The note whith title {name} not in the notes.\
                   Enter the note title: ")
    os.system('cls')
    print(f"Note whith title {name} was deleted")
    notes.pop(name)
    return  notes

def EditNotes(notes:OrderedDict)->OrderedDict:
    name_for_change = input("Enter the note title: ")
    while name_for_change not in notes:
        name_for_change=input(f"The note whith title {name} not in the notes.\
                   Enter the note title: ")
    name = name_for_change
    notes_data:dict=notes[name]
    time_of_created:list=notes_data['time_of_created']
    note_id = notes_data['note_id']
    note = notes_data['note']
    notes.pop(name)
    value = {"time_of_created":time_of_created,"note_id":note_id, 
                 "note":note}
    os.system('cls')
    while True: #еще не правил
        print('Что именно хотите поменять в контакте: ')
        print(f'1 - Имя - {name}')
        print(f'2 - Телефон - {phone_number} ')
        print(f'3 - Дату рождения - {birth_day}')
        print(f'4 - Электронную почту - {email}')
        print(f'5 - Сохранить изменения и выйти - {name}: {value} ')
        command = input('Введите номер команды для изменения контакта')
        if command == '1':
            os.system('cls')
            print(f'1 - Имя - {name}')
            name = input("Введите новое имя контакта: ")
        elif command == '2':
            os.system('cls')
            print(f'2 - Телефон - {phone_number} ')
            number_of_phoneNumber=1
            phone_number=[]
            while True:
                number = input(f"Введите {number_of_phoneNumber}й номер телефона. Если его нет нажмите  Enter: ")
                if number!='':
                    phone_number.append(number)
                    number_of_phoneNumber+=1
                else:
                    break
        elif command=='3':
            os.system('cls')
            print(f'3 - Дату рождения - {birth_day}')
            birth_day = input('Введите новую дату рождения: ')
        elif command=='4':
            os.system('cls')
            print(f'4 - Электронную почту - {email}')
            email = input('Введите новый адрес электронной почты: ')
        elif command=='5':
            break            
    value = {"phone_numbers": phone_number, "birth_day": birth_day, "email": email}
    phone_book[name]=value 
    os.system('cls')
    print(f"Контакт {name} был изменен")
    return  phone_book

def Menu():
    print('1 - Add New Note')
    print('2 - Save Notes')
    print('3 - Edit Note')
    print('4 - Show Notes')
    print('5 - Exit')



    
os.system('cls')
time1: TimeStamp = TimeStamp()
print(time1.GetTime()) 
""" notes = load()
print("Загрузка контактов выполнена успешно")
while True:
    Menu()
    number_of_telNumbrs:int = 1
    command = input("Введите номер команды: ")
    if command == "1":
        name = input("Введите имя нового контакта: ")
        tel_number:list=[]
        while True:
            number = input(f"Введите {number_of_telNumbrs}й номер телефона. Если его нет нажмите  Enter: ")
            if number!='':
                tel_number.append(number)
                number_of_telNumbrs+=1
            else:
                break
        bith_day = input("Введите ДР: ")
        mail = input("Введите email: ")
        notes[name] = {"phone_numbers": tel_number, "birth_day": bith_day, "email": mail}
        os.system('cls')
        print("Контакт добавлен")
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