from numpy import *
a = array(eval(input("digite as faltas: ")))
b = zeros(6, dtype = float)

for i in range(size(a)):
	if(a[i]==2):
		b[0] = b[0] + 1
	elif(a[i]==3):
		b[1] = b[1] +1
	elif(a[i]==4):
		b[2] = b[2] +1
	elif(a[i]==5):
		b[3] = b[3] + 1
	elif(a[i]==6):
		b[4] = b[4] + 1
	elif(a[i]==7):
		b[5] = b[5] + 1

for i in range(size(b)):
	b[i] = round((b[i]/size(a)*100),1)
	
print(b)