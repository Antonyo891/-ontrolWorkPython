from ClassNote import Note

class NoteController:
    ___note_id = 0
    def __init__(self) -> None:
        self.__note_list = list()

    def LoadNotes(self, note_list:list):
        for i in note_list:
            self.__note_list=note_list
        
    def AddNote(self, note):
        self.__note_list.append(note)
        
    def NewId(self)-> int:
        temp_note:Note = self.__note_list[0]
        note_id = temp_note.GetNotesId()
        for i in range(1,self.__note_list.__len__):
            temp_note=self.__note_list[i]
            if note_id < temp_note.GetNotesId():
                note_id=temp_note.GetNotesId()
        return note_id+1 

    def CreateNote(self):
        heading:str = input("Введите название заметки: ")
        note: str = input("Введите заметку: ")
        note_id: int = self.NewId()
        temp_note = Note(heading,note,note_id)
        list.append(temp_note)
    
    def EditNote(self, heading:str ):
        edit_note = input("Введите новый текст редактируемой заметки")
        note_is_in_list: bool = False
        for i in range(0,self.__note_list.__len__):
            note:Note = self.__note_list[i]
            if heading == note.GetHead():
                note_is_in_list = True
                note_id: int = note.GetNotesId()
                self.__note_list.pop(i)
                break
        if note_is_in_list:
            note = Note(heading, edit_note, note_id)
            print(f"Заметка {note.GetHead()} успешно изменена")
        else: 
            print(f"Заметки с названием {heading} нет в списке")
        
    def ReadNotes(self)-> dict:
        sorted(self.__note_list)
        i:int = 1
        result:dict = dict()
        for item in self.__note_list:
            print(f"{i}.) {item.GetTimeOfCreated()} {item.GetHead()} \n")
            result[i] = item.GetHead()
            i+=1
        return result
    
    def RemoveNote(self, heading:str):
        note_is_in_list: bool = False
        for i in range(0,self.__note_list.__len__):
            note:Note = self.__note_list[i]
            if heading == note.GetHead():
                note_is_in_list = True
                self.__note_list.pop(i)
                break
        if note_is_in_list:
            print(f"Заметка {note.GetHead()} успешно изменена")
        else: 
            print(f"Заметки с названием {heading} нет в списке")
