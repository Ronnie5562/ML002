# Write a script to calculate the number of months that it would take to pay off a credit card!! { Sounds amazing right? } 🔥🔥🔥

import datetime
import calendar

balance = 10000
interest_rate = 0.13
monthly_payment = 600

today = datetime.date.today()
# Python has a method called .monthrange() in the calendar module. The .monthrange() takes in two arguments {the year, the month} and returns 
# a tuple containing (1) The day in which the first day of the month falls on [it actually retutns an integer which is decoded as 
# {0 - Monday, 1 - Tuesday and so on...}] and (2) The number of days in the specified month.

days_in_current_month = calendar.monthrange(today.year, today.month)[1]

# print(days_in_current_month)
# print(today.year)
# print(today.month)
# print(today.day)

days_till_month_end = days_in_current_month - today.day
#print(days_till_month_end)
start_date = today + datetime.timedelta(days=days_till_month_end + 1)
end_date = start_date

while balance > 0:
    monthly_charge = (interest_rate / 12) * balance
    balance += monthly_charge 
    balance -= monthly_payment

    balance = round(balance, 2)
    if balance < 0:
        balance = 0

    print(end_date, balance)

    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days=days_in_current_month)
