### Dates ###

'''import datetime

now = datetime.datetime'''

from datetime import datetime

current_date = datetime.now() # now() es un metodo propio del sitema

print("-----------------------")
print("Print de 'datetime.now()'")
print(current_date)
print("-----------------------")


print("Print de 'current_date.timestamp()'")
timestamp = current_date.timestamp()
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
    print(date.timestamp())

print("Print de 'print_date(current_date)'")
print_date(current_date)
print("-----------------------")

print("Print de 'print_date(year_2023)'")
print_date(year_2023)
# año mes y dia es lo minimo exigible para poder crear una fecha. En este caso las horas minutos y segundos los saca como '0' al no haberles dado un valor
print("-----------------------")


from datetime import time



current_time = time()

print(current_time.hour)
print(current_time.minute) # estos tres valores dan 0. No devuelve la hora actual
print(current_time.second)
print("-----------------------")

current_time = time(17, 25, 44) # doy valores a las horas minutos y segundos
print("current_time con valores introducidos en el constructor de time()")
print(current_time)
print("-----------------------")


from datetime import date
today_date = date.today() # fecha del sistema
print("Print de today_date.day .month . year")
print(today_date.day)
print(today_date.month)
print(today_date.year)
print("-----------------------")


## Modificar fechas
current_date = date(current_date.year + 20, current_date.month, current_date.day)
print("Print de fecha +20 años")
print(current_date)
print("-----------------------")
