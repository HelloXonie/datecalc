#!/bin/python3

import time
from datetime import date
from tqdm import tqdm
from time import sleep

#get the current date and subtract from the future date
today = date.today()
future = date(2028,12,20)

remaining_days = str(future - today)

print (remaining_days)

for i in tqdm(range(10)):
    time.sleep (0.1)







