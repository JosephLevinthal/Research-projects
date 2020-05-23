from numpy import*

p= array(eval(input("Insira o indice de glicose dos pacientes: ")))
i=0
o=0

while (i < size(p)):
	if (p[i]>99):
		o+=1
		print(i)
	i+=1

print(o)