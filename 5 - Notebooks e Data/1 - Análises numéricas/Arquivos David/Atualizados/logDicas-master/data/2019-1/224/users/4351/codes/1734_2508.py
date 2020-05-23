n= float(input("numero k: "))
pia= 3
c=0
i= 2
if (n==1):
	pia=3.0
	print(round(pia, 8))
else:
	while (c<n-1):
		sinal= (-1)**c
		pia= pia+ sinal*4/((i)* (i+1)*(i+2))
		c=c+1
		i= i + 2
	print(round(pia, 8))