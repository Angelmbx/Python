### Dates ###

'''import datetime

now = datetime.datetime'''

from datetime import datetime

current_time = datetime.now() # now() es un metodo propio del sitema

print("-----------------------")
print("Print de 'datetime.now()'")
print(current_time)
print("-----------------------")


print("Print de 'current_time.timestamp()'")
timestamp = current_time.timestamp()
print (timestamp) # representación universal del momento concreto en un objeto float para facilitar el envío del mismo
print("-----------------------")


# quiero crear una fecha que indique el comienzo del año
year_2023 = datetime(2023,1,1) #admite año, mes, dia, hora, minuto...

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)

print("Print de 'print_date(current_time)'")
print_date(current_time)
print("-----------------------")
