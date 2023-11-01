from functools import total_ordering
from TimeStamp import TimeStamp

class Note:
    __timeStamp = TimeStamp()
    def __init__(self,heading:str, note:str, note_id:int,
                    __time_of_created:str = __timeStamp.GetTime()) -> None:
        self.__heading:str = heading
        self.__note: str = note
        self.__note_id: int = note_id
        self.__time_of_created: str = __time_of_created

    def __str__(self) -> str:
        return str(f"Id = {self.__note_id} {self.__time_of_created} {self.__heading} \n" +
                   self.__note)
    
    def __lt__(self, other):
        note_temp:Note = other
        return self.__time_of_created < note_temp.__time_of_created

    def __eq__(self, other):
        note_temp:Note = other
        return self.__time_of_created == note_temp.__time_of_created
    
    def PrintNote(self):
        print(f" \n Created at {self.__time_of_created} Id = {self.__note_id} ")
        print(f" \n Note {self.__heading}: \n {self.__note} ")
    
    def GetNote(self)-> dict:
        value = {"time_of_created":self.__time_of_created,"note_id":self.__note_id, 
                 "note":self.__note}
        return {self.__heading:value}
    
    def GetHead(self):
        return self.__heading
    
    def GetNotesId(self):
        return self.__note_id
    
    def GetTimeOfCreated(self):
        return str(self.__time_of_created)
    
    def SetNote(self,note: str):
        self.__note = note