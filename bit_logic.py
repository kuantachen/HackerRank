#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER lo
#  2. INTEGER hi
#  3. INTEGER k
#

def maxXor(lo, hi, k):
    # Write your code here
    max_xor = 0
    for i in range(lo, hi+1):
        for j in range(lo, hi+1):
            if i == j:
                continue
            max_xor = max(max_xor, i ^ j)
    
    if max_xor <= k:
        return max_xor
    else:
        return k
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lo = int(input().strip())

    hi = int(input().strip())

    k = int(input().strip())

    result = maxXor(lo, hi, k)

    fptr.write(str(result) + '\n')

    fptr.close()