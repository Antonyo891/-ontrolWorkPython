import time


class TimeStamp:
    def __init__(self) -> None:
        self.__second = time.time()
        self.__date = time.localtime(self.__second)
        self.__ti = time.asctime(self.__date)

    def __str__(self)-> str:
        return str(self.__ti)

    def GetTime(self):
        return self.__ti
