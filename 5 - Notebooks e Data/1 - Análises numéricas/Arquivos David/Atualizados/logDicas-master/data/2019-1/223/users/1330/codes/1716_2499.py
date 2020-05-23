from math import *

k = int(input())

a = 1
total = 0
while(a<k):
	total = 1/factorial(a) + total
	a = a + 1
	
final = total + 1
print(round(final,8))
