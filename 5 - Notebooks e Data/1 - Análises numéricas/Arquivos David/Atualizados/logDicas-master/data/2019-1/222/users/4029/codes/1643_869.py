x= float(input("Digite o valor da sua compra: R$ "))
if (x >= 200):
	compra= x - ((x * 5) / 100)
else: 
	compra = x
print(round(compra, 2))