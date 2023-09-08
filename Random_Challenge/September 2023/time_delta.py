#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    date1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    date2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    
    diff = abs(date1-date2)
    length = str(diff).split(' ')
    if len(length) > 1:
        new_diff = str(diff).split(',')
        days = int(new_diff[0].split()[0])
        times = new_diff[1]
        
        hours, minutes, seconds = map(int, str(times).split(':'))
        hours += days*24
        result = (hours*3600) + (minutes*60) + seconds
        return str(result)
    else:
        hours, minutes, seconds = map(int, str(diff).split(':'))
        result = (hours*3600) + (minutes*60) + seconds
        return str(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
