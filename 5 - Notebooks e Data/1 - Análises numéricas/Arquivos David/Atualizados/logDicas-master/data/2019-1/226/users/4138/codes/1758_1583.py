from numpy import *
x = input("insira a string:")

i = 0
k = 3
msg = ""
while(i < len(x)):
	if(i == len(x)-3):
		msg = msg + x[i:k]
		i = i + 3
		k = k + 3
	else:
		msg = msg + x[i:k] + "."
		i = i + 3
		k = k + 3
print(msg)

