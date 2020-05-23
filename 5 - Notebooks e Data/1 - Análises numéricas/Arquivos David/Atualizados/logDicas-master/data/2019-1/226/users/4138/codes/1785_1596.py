from numpy import *
v = array(eval(input("insira as notas:")))
i = 0 #contador de ciclo
soma = 0 #contador da soma
a = sum(v) - min(v)
b = size(v) - 1
c = a/b
print(round(c,2))
	
		