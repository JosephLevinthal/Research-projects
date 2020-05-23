from math import *
x = int(input("digite x: "))
n = 0
e = 0

while x > n:
		e = e +  (1/factorial(n))
		n = n + 1
print(round(e,8))