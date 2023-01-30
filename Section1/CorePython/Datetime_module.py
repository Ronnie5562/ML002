# Datetime Module - How to work with Dates, Times, Timedeltas, and Timezones
import datetime
    # [1] TO get the weekday [.date]
# [A] => WEEKDAY <=
#Moday => 0 | Sunday => 1
WEEKDAY = datetime.date.today().weekday()
print('{:02}'.format(WEEKDAY))

# [B] => ISOWEEKDAY <=
# Moday => 1 | Sunday => 7
ISOWEEKDAY = datetime.date.today().isoweekday()
print('{:02}'.format(ISOWEEKDAY))
    # Timedelta  - manipulating days
tday = datetime.date.today()
tdelta = datetime.timedelta(days=1)


date = (tday + tdelta)
check = datetime.date(2023, 1, 31)
if check == date:
    print('HELLO')

    # To get time [.time]
t = datetime.time(9, 30, 45, 999999)
print(t.hour) 

#   To get both time and date [.datetime]

dt = datetime.datetime.today()
print(f"{dt.day}/{dt.month}/{dt.year}")
print(f"{dt.hour}:{dt.minute}:{dt.second}")

#   To get both time and date for yesterday [24 hours earlier]
bdt = datetime.datetime.today()  # we can also use [.now() / .utcnow()]

tdelta_2 = datetime.timedelta(days=1)

yesterday = bdt - tdelta_2

print(yesterday)

# install the pytz package to work with timezones
# To install, use: pip install pytz

import pytz
pydt = datetime.datetime.now()
print(pydt)

time = datetime.datetime.now(tz=pytz.UTC)
print(time)

# To loop through all the timezoness we have, run th code below
#Remember to first install the pytz package first with - [pip install pytz]
#import pytz
# for pz in pytz.all_timezones:
#     print(pz)