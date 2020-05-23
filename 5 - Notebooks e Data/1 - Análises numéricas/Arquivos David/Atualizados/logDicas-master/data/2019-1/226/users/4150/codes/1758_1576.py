from numpy import* 

j1 = array(eval(input("qual elemento: ")))
j2 = array(eval(input("qual elemento: ")))

i = 0
soma1 = 0
soma2 = 0


while ( i < size(j1)):
	if((j1[i]== 11 and j2[i]==33) or (j1[i]==22 and j2[i]==11 or (j1[i] == 33 and j2[i] == 22))):
		soma1 = soma1 + 1
	elif ((j1[i]==33 and j2[i]== 11) or (j1[i]== 11 and j2[i]== 22) or( j1[i] == 22 and j2 [i]==33)):
		soma2 = soma2 + 1
	i = i+1

print(size(j1))

if soma1>soma2:
	print("EUSAPIA")
elif soma2>soma1:
	print("BARSANULFO")
else:
	print("EMPATE")