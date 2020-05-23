from numpy import *  
v = array(eval(input("Informe as notas: ")))
cont=0

for elemento in v:
	if(elemento >=2000):
		cont = cont +1
print(cont)
	


