class WeekDayError(Exception):
    pass
	

class Weeker:
    __days = ['Mon', 'Thu', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        if day not in Weeker.__days:
            raise WeekDayError
        self.__day_index = Weeker.__days.index(day)

    def __str__(self):
        return Weeker.__days[self.__day_index]

    def add_days(self, n):
        self.__day_index += n
        self.__day_index %= len(Weeker.__days)

    def subtract_days(self, n):
        self.__day_index -= n
        self.__day_index %= len(Weeker.__days)

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")