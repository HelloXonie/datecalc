#!/bin/python3

import sys
import os
import time
import progressbar
from io import StringIO
from datetime import date
from time import sleep

#get the current date and subtract from the future date
today = date.today()
future = date(2028,12,20)

remaining_days = str(future - today)

print (remaining_days)

output = StringIO()
sys.stdout = output

bar = progressbar.ProgressBar(maxval=100, \
    widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()

with open('log_file.txt','w') as log_file
for i in (range(20), file = log_file):
    bar.update(i+1)
    sleep(0.1)
bar.finish()
log_file.flush()








