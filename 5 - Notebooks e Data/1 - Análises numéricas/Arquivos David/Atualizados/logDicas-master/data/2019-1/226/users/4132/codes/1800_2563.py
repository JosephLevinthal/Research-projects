from numpy import *
v = array(eval(input("Digite: ")))

while (size(v)>1):
	aux=0
	for i in v:
		if(i >=5)and (i<7):
			aux+=1
	print(aux)
	v = array(eval(input("Digite: ")))
	