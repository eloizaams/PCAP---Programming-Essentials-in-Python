class Timer:
    def __init__(self, hour=0,min=0,sec=0):
        self.__hour = hour
        self.__min = min
        self.__sec = sec

    def __str__(self):
       return self.__format_time(self.__hour,self.__min,self.__sec) 

    def next_second(self):
        self.__sec += 1
        if self.__sec == 60:
            self.__sec = 0
            self.__min += 1
            if self.__min == 60:
                self.__min = 0
                self.__hour += 1
                if self.__hour == 24:
                    self.__hour = 0

    def prev_second(self):
        self.__sec -= 1
        if self.__sec == -1:
            self.__sec = 59
            self.__min -= 1
            if self.__min == -1:
                self.__min = 59
                self.__hour -= 1
                if self.__hour == -1:
                    self.__hour = 23

    @staticmethod
    def __format_time(hour, min, sec):
        return f"{hour:02}:{min:02}:{sec:02}"
    

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
