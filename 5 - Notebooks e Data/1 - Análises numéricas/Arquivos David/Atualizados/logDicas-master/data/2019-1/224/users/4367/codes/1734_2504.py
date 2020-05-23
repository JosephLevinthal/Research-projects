qiv=int(input("quantidade de virus: "))
qil=int(input("quantidade de leucocitos: "))
pv=float(input("percentual de virus no sangue: "))
pl=float(input("percentual de leucocitos no sangue: "))
laco=0
while(qil<2*qiv):
	v=qiv*(pv/100)
	qiv=qiv+v
	l=qil*(pl/100)
	qil=qil+l
	laco=laco+1
print(laco)