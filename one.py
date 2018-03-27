#!/usr/bin/env python
import sys

def sum(list):
    sum = 0
    for i in list: 
        sum += i
    return sum

def sumOfMultiplesOf4And5Below(x):
    multiples = []
    
    for i in range(1, x):
        if (i % 4 == 0 or i % 5 == 0):
            multiples.append(i)
  
    print "List of multiples of 4 and 5 are :"+'\n', multiples       
    return sum(multiples)

x=input("Enter the higher limit of the number")
Total = sumOfMultiplesOf4And5Below(x)

print "Sum of no is",Total
