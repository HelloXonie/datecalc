#!/bin/python3

from datetime import date
#from os_sys.progress import bar

#get the current date and subtract from the future date
today = date.today()
future = date(2028,12,20)

remaining_days = str(future - today)

print (remaining_days)

#progress bar
#bar = Bar ('Processing', max=20)
#for i in range(20):
#    bar.next()
#bar.finish()

#print (bar)






