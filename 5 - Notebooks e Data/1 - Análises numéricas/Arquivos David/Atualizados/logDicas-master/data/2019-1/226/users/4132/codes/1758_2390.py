from numpy import *
v = array(eval(input("Digite: ")))
vf = array(eval(input("Digite faltantes: ")))
aux=arange(size(v))
i = 0
j = 0
mes=0

while(i<size(v)):
	aux[i]=v[i]-vf[i]
	i=i+1
	
maior=aux[0]
while(j<size(aux)):
	if(aux[j]>maior):
		maior=aux[j]
		mes=j
	j+=1
print(mes+1)
	


