from math import *
np = float(input())

prob = 1 - ( factorial(365) / factorial(365 - np) )  * (1/365**np) 

print(round(prob*100,2))