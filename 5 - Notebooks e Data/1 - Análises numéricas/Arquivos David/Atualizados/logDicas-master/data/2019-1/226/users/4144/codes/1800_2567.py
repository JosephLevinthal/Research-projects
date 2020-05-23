from numpy import *
a = int(input("digite o nro.: "))

for i in range(a):
	print((a-i)*"*")
	i = i - 1
for i in range(a+1):
	print(i*"*")
	i = i +1
	
	