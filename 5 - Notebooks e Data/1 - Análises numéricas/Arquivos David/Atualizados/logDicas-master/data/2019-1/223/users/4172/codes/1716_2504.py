qiv=int(input("quantidade inicial do virus: "))
qil=int(input("quantidade incial de leucocitos: "))
pv=int(input("percentual de crescimento do virus: "))
pl=int(input("percentual de crescimento de lrucocitos: "))

d=0

while(qil<qiv*2):
	qiv=qiv+(qiv*(pv/100))
	qil=qil+(qil*(pl/100))
	d+=1
print(d)