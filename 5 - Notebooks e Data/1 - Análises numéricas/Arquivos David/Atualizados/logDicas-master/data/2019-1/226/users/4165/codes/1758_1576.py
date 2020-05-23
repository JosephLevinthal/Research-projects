from numpy import *

v0 = array(eval(input("Jogadas de Eusapia: ")))
v1 = array(eval(input("Jogadas de Barsanulfo: ")))

i = 0
j = 0
k = 0

while(i < size(v0) and size(v0) == size(v1)):
	if((v0[i] == 11 and v1[i] == 33) or (v0[i] == 22 and v1[i] == 11) or (v0[i] == 33 and v1[i] == 22 )):
		i = i + 1
		j = j + 1
	elif((v1[i] == 11 and v0[i] == 33) or (v1[i] == 22 and v0[i] == 11) or (v1[i] == 33 and v0[i] == 22 )):
		i = i + 1
		k = k + 1
	else:
		i = i + 1
print(i)
if(j > k):
	print("EUSAPIA")
elif(k > j):
	print("BARSANULFO")
else:
	print("EMPATE")