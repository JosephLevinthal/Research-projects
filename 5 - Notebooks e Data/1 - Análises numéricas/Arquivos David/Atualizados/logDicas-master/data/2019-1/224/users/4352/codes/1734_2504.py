qiv=int(input("quantidade inicial de virus: "))
qil=int(input("quantidade inicial de leucocitos: "))
pv=float(input("percentual de virus: "))
pl=float(input("percentual de leucocitos: "))
c=0
while(qil<2*qiv):
	pvv=qiv*(pv/100)
	qiv=qiv+pvv
	pll=qil*(pl/100)
	qil=qil+pll
	c=c+1
print(c)