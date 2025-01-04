#!/bin/python3

from datetime import date
today = date.today()
future = date(2028,01,01)

remaining_days = str(future - today)

print (remaining_days)


