from numpy import *
x = input()
a = ""
h = 0
for i in range(len(x)):
	if x[i] == "a" or x[i] == "A":
		h += 1
	else:
		a += x[i]
print(a)

