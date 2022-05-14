#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'counts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY teamA
#  2. INTEGER_ARRAY teamB
#

def counts(teamA, teamB):
    # Write your code here
    
    matches = []
    teamA.sort()
    
    for i in teamB:
        lo, hi = 0, len(teamA) - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            if teamA[mi] > i:
                hi = mi - 1
            else:
                lo = mi + 1
        matches.append(lo)
    
    return matches
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    teamA_count = int(input().strip())

    teamA = []

    for _ in range(teamA_count):
        teamA_item = int(input().strip())
        teamA.append(teamA_item)

    teamB_count = int(input().strip())

    teamB = []

    for _ in range(teamB_count):
        teamB_item = int(input().strip())
        teamB.append(teamB_item)

    result = counts(teamA, teamB)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()