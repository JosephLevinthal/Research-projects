from numpy import*
e = array(eval(input("sequencia de Eusapia: ")))
b = array(eval(input("sequencia de Barsanulfo: ")))

i = 0     #indice
x = 0     #elemento no vetor
ve = 0    #pontos eusabia
vb = 0    #pontos barsanulfo

while (i < size(e)) or (i < size(b)):
	i = i + 1
	if e[x] > b[x]:
		ve = ve + 1
	elif e[x] < b[x]:
		vb = vb + 1
	else:
		vb = vb
		ve = ve
	x = x + 1
print(i)
if ve > vb:
	print("EUSAPIA")
elif ve < vb:
	print("BARSANULFO")
else:
	print("EMPATE")