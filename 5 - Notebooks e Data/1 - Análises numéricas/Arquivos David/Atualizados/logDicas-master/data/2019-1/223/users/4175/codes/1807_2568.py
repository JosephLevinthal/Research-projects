from numpy import *
x = int(input())

y = "*"
o = "o"

for i in range(x):
	f= y*(x-i)+o*(2*i)+y*(x-i)
	print(f)