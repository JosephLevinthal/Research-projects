nr=float(input("insira um numero real: "))
ni=int(input("insira a quantidade de termos:"))
i=1
c=0
s=0
while c<ni:
	f=(nr**i)/i
	s=s+f
	i=i+2
	c=c+1
print(round(s,7))