from numpy import *

x = input()
x = x.upper()

print(x.replace(" ",""))

if x[-1] == x[0]:
	print(1)
else:
	print(0)