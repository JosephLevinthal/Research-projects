from numpy import *
v = array(eval(input("v: ")))
v1 = array(eval(input("v: ")))
i = 0 
soma1 = 0
soma2 = 0
while(i < size(v)):
	if ((v[i] == 11 and v1[i] == 33) or (v[i] == 33 and v1[i] == 22) or (v[i] == 22 and v1[i] == 11)):
		soma1 = soma1 + 1
	elif((v1[i] == 22 and v[i] == 11) or (v1[i] == 33 and v[i] == 22) or (v1[i] == 11 and v[i] == 33)):
		soma2 = soma2 + 1
	i = i + 1
if(soma1 > soma2):
	print(i)
	print("EUSAPIA")
elif(soma2 > soma1):
	print(i)
	print("BARSANULFO")
elif(soma1 == soma2):
	print(i)
	print("EMPATE")