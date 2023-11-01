import time
from functools import total_ordering


class TimeStamp:
    def __init__(self) -> None:
        self.__second = time.time()
        self.__date = time.localtime(self.__second)
        self.__ti = str(time.asctime(self.__date))
    
    def __eq__(self, __value: object) -> bool:
        return self.__second==__value.__second
    
    def __lt__(self, __value: object):
        return self.__second<__value.__second

    def __str__(self)-> str:
        return str(self.__ti)

    def GetTime(self):
        return self.__ti
