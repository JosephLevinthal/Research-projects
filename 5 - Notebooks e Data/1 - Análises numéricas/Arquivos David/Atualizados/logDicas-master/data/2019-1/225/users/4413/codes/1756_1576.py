from numpy import*
v= array(eval(int(input("Eusapia: "))))
vet = array(eval(int(input("Barsanulfo: "))))
a = 0
b = 0 
c = 0
while (a< size[v]):
	if(v[a]==22 and vet[a]==11 or v[a]==11 and vet[a]==33 or v[a]==33 and vet[a]==22)
	b=b+1 
	elif(vet[a]==22 and v[a]==11 or vet[a]==11 and v[a]==33 or vet[a]==33 and vet[a]==22)
	c =c+1
	else:
		b=b
		c=c
if(b)