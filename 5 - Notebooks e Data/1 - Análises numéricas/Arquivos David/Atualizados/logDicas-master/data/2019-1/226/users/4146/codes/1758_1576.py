from numpy import *
e = array(eval(input("Jogador 1: ")))
b = array(eval(input("Jogador 2: ")))

i = 0
v1 = 0
v2 = 0

while (i < size(e)):
	if ((e[i] == 11) and (b[i] == 33)) or ((e[i] == 22) and (b[i] == 11)) or ((e[i] == 33) and (b[i] == 22)):
		v1 = v1 + 1
	elif ((e[i] == 33) and (b[i] == 11)) or ((e[i] == 11) and (b[i] == 22)) or ((e[i] == 22) and (b[i] == 33)):
		v2 = v2 + 1
	else:
		m = "EMPATE"
	i = i + 1
	
print(i)

if v1 > v2:
	print("EUSAPIA")
elif v2 > v1:
	print("BARSANULFO")
else:
	print("EMPATE")
	
	
		
	
	


