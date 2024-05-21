import datetime
import locale

# Definindo a localização para português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

str_date = '4 de novembro de 2020, 14:53:00'

date = datetime.datetime.strptime(str_date, '%d de %B de %Y, %H:%M:%S')
print (date.strftime("%Y/%m/%d %H:%M:%S"))
print(date.strftime("%y/%B/%d %H:%M:%S %p"))
print(date.strftime("%a, %Y %b %d"))
print(date.strftime("%A, %Y %B %d"))
print(date.strftime("Weekday: %w"))
print(date.strftime("Day of the year: %j"))
print(date.strftime("Week number of the year: %U"))

