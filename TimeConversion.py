#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour = int(s[:2])
    if s[-2:] == "PM":
        if hour != 12:
            hour += 12
    elif hour == 12:
        hour = 0

    new_s = str(hour).zfill(2) + s[2:-2]
    return new_s




if __name__ == '__main__':

   print(timeConversion('07:05:45PM'))
   print(timeConversion('12:05:00AM'))
   print(timeConversion('12:05:00PM'))

