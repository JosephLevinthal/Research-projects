a = int(input("qnt inicial de pirarucu: "))
b = float(input("percentual de crescimento: "))
c = int(input("qnt de pirarucu vendido a cada mes: "))
meses = 0
while(a>0 and a<8000):
	txcm= (a*b)/100
	a = a + txcm - c
	meses = meses + 1
	if(a>0 and a<8000):
		c = int(input("qnt de pirarucu vendido a cada mes: "))
if(a<0):
	print("ZERO")
elif(a>=8000):
	print("MAXIMO")
print(meses)