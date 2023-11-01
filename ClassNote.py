from functools import total_ordering
from TimeStamp import TimeStamp

class Note:

    def __init__(self,heading:str, note:str, note_id:int) -> None:
        self.__heading:str = heading
        self.__note: str = note
        self.__note_id: int = note_id
        self.__time_of_created: str = TimeStamp().GetTime
    
    def __init__(self, object:dict):
        for key,value in object.items():
            self.__heading:str = key
            value_of_note = value
        self.__note = value_of_note["note"]
        self.__note_id = value_of_note["note_id"]
        self.__time_of_created = value_of_note["time_of_created"]


    def __str__(self) -> str:
        return self.GetNote()
    
    def __lt__(self, other):
        return self.__time_of_created < other.__time_of_created

    def __eq__(self, other):
        return self.__time_of_created == other.__time_of_created
    
    def PrintNote(self):
        print(f" \n Created at {self.__time_of_created} Id = {self.__note_id} ")
        print(f" \n Note {self.__heading}: \n {self.__note} ")
    
    def GetNote(self)-> dict:
        value = {"time_of_created":self.__time_of_created,"note_id":self.__note_id, 
                 "note":self.__note}
        return {self.__heading:value}
    
    def GetHead(self):
        return {self.__heading}
    
    def GetNotesId(self):
        return {self.__note_id}
    
    def GetTimeOfCreated(self):
        return {self.__time_of_created}
    
    def SetNote(self,note: str):
        self.__note = note