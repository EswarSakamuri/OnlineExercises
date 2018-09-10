#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = neg = zero = 0
    total = len(arr)
    for a in arr:
        if a >0:
            pos += arr.count(a)
        elif a <0:
            neg += arr.count(a)    
        else:
            zero += arr.count(a)
        arr = list(set(arr))
        arr.remove(a)
    print(round(pos/total, total)) 
    print(round(neg/total, total)) 
    print(round(zero/total, total))
    return True
        

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

