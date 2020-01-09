from datetime import datetime

print(datetime.now())

moment = datetime.now()
print(moment.year)
print(moment.month)
print(moment.day)
print(moment.hour)
print(moment.minute)
print(moment.second)
print(moment.microsecond)

print(datetime.ctime(moment))

print("#")
print(datetime.strftime(moment,"%Y"))

print(datetime.strftime(moment,"%B"))

print(datetime.strftime(moment,"%A"))

print(datetime.strftime(moment,"%X"))

print(datetime.strftime(moment,"%D"))

print(datetime.strftime(moment,"%Y %B %A"))

import locale
print(locale.setlocale(locale.LC_ALL,""))

print(datetime.strftime(moment,"%Y %B %A")) # locale ile bulunduğumuz yerin diline çevirebiliyoruz.

print(datetime.timestamp(moment))
seconds = datetime.timestamp(moment)
time = datetime.fromtimestamp(seconds)
print(time)


date1 = datetime(2019,12,1)
date2 = datetime.now()
fark = date2 - date1
print(fark)
print(fark.days)
print(fark.seconds)
print(fark.microseconds)