#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    colors = {}

    # create a hash map with the total number of each color
    for color in ar:
        colors[color] = colors.get(color, 0) + 1

    # get pairs
    pairs = 0
    for count in colors.values():
        pairs += count // 2
    
    return pairs

if __name__ == '__main__':
    # HackerRank example
    print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))  # Expected: 3

    # all pairs
    print(sockMerchant(4, [1, 1, 2, 2]))                          # Expected: 2

    # no pairs
    print(sockMerchant(3, [1, 2, 3]))                             # Expected: 0

    # all same color
    print(sockMerchant(6, [5, 5, 5, 5, 5, 5]))                   # Expected: 3

    # odd count of one color
    print(sockMerchant(5, [1, 1, 1, 1, 1]))                      # Expected: 2

    # single sock
    print(sockMerchant(1, [7]))                                   # Expected: 0
