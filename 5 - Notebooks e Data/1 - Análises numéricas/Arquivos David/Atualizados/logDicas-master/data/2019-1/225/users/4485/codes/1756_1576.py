from numpy import *

v1 = array(eval(input("Jogadas Eusapia: ")))
v2 = array(eval(input("Jogadas Barsanulfo: ")))

cont = 0
cont1 = 0 #variavel contadora de EUSAPIA
cont2 = 0 #variavel contadora de BARSABULFO
#representacao de valores
pe = 11
pa = 22
t = 33

while(cont < size(v1)):
	if (v1[cont] == pa and v2[cont] == pe):
		cont1 = cont1 + 1
	elif(v1[cont] == pe  and v2[cont] == t):
		cont1 = cont1 + 1
	elif(v1[cont] == t and v2[cont] == pa):
		cont1 = cont1 + 1
	elif(v1[cont] != v2[cont]):
		cont2 = cont2 + 1
	cont = cont + 1
				
print(size(v1))

if(cont1 == cont2):
	print("EMPATE")
else:
	if(cont1 > cont2):
		print("EUSAPIA")
	else:
		print("BARSANULFO")		