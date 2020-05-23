qp= int(input("qual a quantidade inicial de pirarucus?"))
cp= int(input("qual o percentual de crescimento?"))
pt=0
m=0
while (qp>0) and (qp<8000):
	qp=qp+(cp/100)*qp
	pt=int(input("qual a quantidade de pirarucus retirados?"))
	qp=qp-pt
	m=m+1
if (qp<=0):
	print("ZERO")
elif (qp>8000):
	print("MAXIMO")
print(m)