from numpy import *
v1 = array(eval(input("Digite: ")))
v2 = array(eval(input("Digite: ")))
cont = 1
cont1 = 0
cont2 = 0
while (cont <= size(v1)):
	if (v1[cont-1] * 100 + v2[cont-1] == 1122):
		cont2 = cont2 + 1
	elif (v1[cont-1] * 100 + v2[cont-1] == 1133):
		cont1 = cont1 + 1
	elif (v1[cont-1] * 100 + v2[cont-1] == 2211):
		cont1 = cont1 + 1
	elif (v1[cont-1] * 100 + v2[cont-1] == 2233):
		cont2 = cont2 + 1
	elif (v1[cont-1] * 100 + v2[cont-1] == 3311):
		cont2 = cont2 + 1
	elif (v1[cont-1] * 100 + v2[cont-1] == 3322):
		cont1 = cont1 + 1
	cont = cont + 1
print(cont - 1)
if (cont1 > cont2):
	print('EUSAPIA')
elif (cont1 < cont2):
	print('BARSANULFO')
else:
	print('EMPATE')
		
	
	