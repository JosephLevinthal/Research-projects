from numpy import*
p=array(eval(input("escreva ows presentes: ")))
f=array(eval(input("escreva os faltantes: ")))
pf=p-f
i=0
while(i<size(pf)):
	if(pf[i]==max(pf)):
		print(i+1)
	i=i+1