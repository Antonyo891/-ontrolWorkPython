import time
import datetime  
from datetime import datetime
from functools import total_ordering


class TimeStamp:
    def __init__(self) -> None:
        self.__second = time.time()
        self.__date = time.localtime(self.__second)
        self.__now = datetime.now()
        self.__ti = str(self.__now.strftime("%Y-%m-%d %H:%M:%S"))
    
    def __eq__(self, __value: object) -> bool:
        timest:TimeStamp = __value
        return self.__second==timest.__second
    
    def __lt__(self, __value: object):
        timest:TimeStamp = __value
        return self.__second<timest.__second

    def __str__(self)-> str:
        return str(self.__ti)

    def GetTime(self):
        return self.__ti
