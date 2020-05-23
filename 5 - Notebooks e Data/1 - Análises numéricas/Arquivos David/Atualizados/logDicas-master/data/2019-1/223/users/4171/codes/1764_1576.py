from numpy import *

v1 = array(eval(input("v1: ")))
v2 = array(eval(input("v2: ")))

Ev = 0
Bv = 0
i = 0

while i < size(v1):
	if (v1[i]) == v2[i]:
		Ev += 0
		Bv += 0
	elif (v1[i]) == 11 and v2[i] == 33 or (v1[i]) == 33 and v2[i] == 22 or (v1[i]) == 22 and v2[i] == 11:
		Ev += 1

	elif (v2[i]) == 11 and v1[i] == 33 or (v2[i]) == 33 and v1[i] == 22 or (v2[i]) == 22 and v1[i] == 11:
		Bv += 1
		
	i += 1
	
print(i)

if Ev > Bv:
	print("EUSAPIA")
elif Bv > Ev:
	print("BARSANULFO")
else:
	print("EMPATE")