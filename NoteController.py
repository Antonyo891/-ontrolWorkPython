from ClassNote import Note
from TimeStamp import TimeStamp

class NoteController:
    ___note_id = 0
    def __init__(self) -> None:
        self.__note_list = list()

    def LoadNotes(self, note_list:list):
        for i in note_list:
            self.__note_list=note_list
        
    def AddNote(self, note:Note):
        self.__note_list.append(note)
        
    def NewId(self)-> int:
        if len(self.__note_list)==0:
            return 0
        temp_note:Note = self.__note_list[0]
        note_id = temp_note.GetNotesId()
        for i in range(1,len(self.__note_list)):
            temp_note=self.__note_list[i]
            if note_id < temp_note.GetNotesId():
                note_id=temp_note.GetNotesId()
        return int(note_id+1) 

    def CreateNote(self):
        heading:str = input("Введите название заметки: ")
        note: str = input("Введите заметку: ")
        note_id: int = self.NewId()
        timeStamp = TimeStamp()
        temp_note = Note(heading,note,note_id,timeStamp.GetTime())
        self.__note_list.append(temp_note)
    
    def EditNote(self, heading:str ):
        edit_note = input("Введите новый текст редактируемой заметки")
        note_is_in_list: bool = False
        for i in range(0,len(self.__note_list)):
            note:Note = self.__note_list[i]
            if heading == note.GetHead():
                note_is_in_list = True
                note_id: int = note.GetNotesId()
                self.__note_list.pop(i)
                break
        if note_is_in_list:
            note = Note(heading, edit_note, note_id)
            self.AddNote(note)
            print(f"Заметка {note.GetHead()} успешно изменена")
        else: 
            print(f"Заметки с названием {heading} нет в списке")
        
    def ReadNotes(self)-> dict:
        sorted(self.__note_list)
        i:int = 1
        result:dict = dict()
        for item in self.__note_list:
            note:Note = item
            print(f"{i}.) {note.GetTimeOfCreated()} {note.GetHead()} \n")
            result[i] = note.GetHead()
            i+=1
        return result
    
    def RemoveNote(self, heading:str):
        note_is_in_list: bool = False
        for i in range(0,len(self.__note_list)):
            note:Note = self.__note_list[i]
            if heading == note.GetHead():
                note_is_in_list = True
                self.__note_list.pop(i)
                break
        if note_is_in_list:
            print(f"Заметка {note.GetHead()} успешно удалена")
        else: 
            print(f"Заметки с названием {heading} нет в списке")
    
    def GetNotesList(self)->list:
        return self.__note_list
    
    def GetNote(self,heading:str):
        for i in range(0,len(self.__note_list)):
            note:Note = self.__note_list[i]
            if heading == note.GetHead():
                print(note)
                return
        print("Такой записи нет")