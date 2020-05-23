from numpy import*
x = int(input("digite x: "))
j = 0
for i in range(x):
	print((x*"*") + ("o"*j) + ("o"*j) + (x*("*")))
	j = j + 1
	x = x-1