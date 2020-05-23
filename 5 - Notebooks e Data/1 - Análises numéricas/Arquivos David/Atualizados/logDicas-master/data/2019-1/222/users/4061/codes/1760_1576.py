from numpy import *
eusapia =array(eval(input("digite jogada: ")))
barsanulfo =array(eval(input("digite jogada: ")))

cont1 = 0
cont2 = 0
empate = 0
i = 0
tam = size(eusapia)
while(size(eusapia- 1) > i):
	jogada1 = eusapia[i]
	jogada2 = barsanulfo[i]
	if(eusapia[i] == barsanulfo[i]):
		empate = empate + 1
	elif(jogada1 == 11 and jogada2 == 33):
		cont1 = cont1 + 1
	elif(jogada1 == 33  and jogada2 == 22):
		cont1 = cont1 + 1
	elif(jogada1 == 22  and jogada2 == 11):
		cont1 = cont1 + 1
	elif(jogada2 == 11 and jogada1 == 33):
		cont2 = cont2 + 1
	elif(jogada2 == 33  and jogada1 == 22):
		cont2 = cont2 + 1
	else:
		cont2 = cont2 + 1
	i = i + 1
	
print(tam)

if(cont1 == cont2):
	print("EMPATE")
elif(cont1 > cont2):
	print("EUSAPIA")
else:
	print("BARSANULFO")
	
	
