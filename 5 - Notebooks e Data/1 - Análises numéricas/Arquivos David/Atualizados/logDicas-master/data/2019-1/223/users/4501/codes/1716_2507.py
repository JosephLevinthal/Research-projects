a=int(input("quantidade inicial: "))
b=int(input("percentual de crescimento: "))
mes = 0
while(0 < a < 8000):
	c=int(input("retirada: "))
	a = a + a * (b/100)- c
	mes = mes + 1
	if(a <= c):
		print("ZERO")
	if(a>=8000):
		print("MAXIMO")
print(mes)	