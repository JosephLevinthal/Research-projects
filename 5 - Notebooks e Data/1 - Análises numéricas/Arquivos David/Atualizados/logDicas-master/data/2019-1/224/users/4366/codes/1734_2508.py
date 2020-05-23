n=int(input("digite um numero natural:"))
pia=3
cont=0
i=2
if(n==1):
	pia=3.0
	print(round(pia,8))
else:
	while(cont<n-1):
		sinal=(-1)**cont
		pia= pia+sinal*4/((i)*(i+1)*(i+2))
		cont=cont+1
		i=i+2
print(round(pia,8))



