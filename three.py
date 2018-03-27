#!/usr/bin/env python
import sys
from itertools import takewhile
def prime():
   
    D = {} 
    q = 2  
    
    while True:
        if q not in D:
            yield q       
            D[q*q] = [q]  
        else:
            for p in D[q]: # move each witness to its next multiple
                D.setdefault(p+q,[]).append(p)
            del D[q]       
        q += 1

value=(sum(takewhile(lambda x: x < 2000000, prime())))
print  "The sum of prime nos less than the 2 million is: ", value
