k=float(input("digite k: "))
p=3
cont=0
i=2
if(k==1):
	p=3.0
	print(round(p,8))
else:
	while(cont<k-1):
		sinal =(-1)**cont
		p= p+sinal*4/((i)*(i+1)*(i+2))
		cont=cont+1
		i=i+2
	print(round(p,8))
				 



