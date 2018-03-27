#!/usr/bin/env python
import sys

def gcd(x,y): 
    if (y==0):
      return x
    else:
      return gcd(y,x%y)
    
def lcm(x,y):
  return x * y / gcd(x,y)

n = 1
higherlimit = input("Enter the no:")
for i in range(1, higherlimit+1):
     n = lcm(n, i)

print "smallest positive number that is evenly divisible by all of the numbers in the given range are", n



