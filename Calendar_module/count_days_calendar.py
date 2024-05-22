import calendar 

class MyCustomCalendar(calendar.Calendar):
    # weekday is a number between 0-6, 0 is Monday
    def __init__(self):
        super().__init__()
    
    def count_weekday_in_year(self, year, weekday):
        weeks = 0
        weekday = (weekday - self.firstweekday) % 7  # Adjusting weekday to match calendar's internal representation
        for month in range(1, 13):
            for week in self.monthdays2calendar(year, month):
                if week[weekday][0] != 0:
                    weeks += 1
        return weeks

my_calendar = MyCustomCalendar()
days = my_calendar.count_weekday_in_year(2019, 0)
print(days)