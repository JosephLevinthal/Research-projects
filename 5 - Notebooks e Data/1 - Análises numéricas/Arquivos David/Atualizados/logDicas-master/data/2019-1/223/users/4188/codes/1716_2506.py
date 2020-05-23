P=int(input("quantidade inicial: "))
perc=float(input("porcentagem: "))
r=int(input("quantidade retirado: "))
c=0
while(P>0 and P<12000):
	P = P + P*(perc/100) - r
	c=c+1
	if(P<=r):
		e="EXTINCAO"
	if (P>=1200):
		e="LIMITE"
print(e)
print(c)