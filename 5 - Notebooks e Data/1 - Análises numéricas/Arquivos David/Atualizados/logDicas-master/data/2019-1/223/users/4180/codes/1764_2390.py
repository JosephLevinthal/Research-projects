from numpy import*
fre = array(eval(input("Entrada: ")))
maior_fre = max(fre)

i = 0
while(i < size(fre)):
	if(fre[i] == maior_fre):
		mes = i + 1
	i = i + 1
print(mes)

