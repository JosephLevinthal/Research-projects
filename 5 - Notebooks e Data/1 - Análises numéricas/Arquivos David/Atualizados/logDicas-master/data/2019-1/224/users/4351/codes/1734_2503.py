n= int(input("valor de n: "))
pia=0
c=1
d=-1
while (c<=n):
	sinal= (-1)**c
	pia= pia+ sinal*((4)/d)
	c= c+1
	d= d-2
print(round(pia, 8))
