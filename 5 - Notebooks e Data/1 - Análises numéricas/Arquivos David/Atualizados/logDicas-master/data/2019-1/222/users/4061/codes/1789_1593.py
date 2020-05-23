from numpy import *

notas = array(eval(input("digite notas: ")))
cont = 0
cont1 = 0
total = 0
while(cont < size(notas)):
	total = total + ((cont+1)*notas[cont])
	cont = cont +1
	cont1 = cont1 + cont
resultado =total/(cont1)
print(round(resultado,2))
