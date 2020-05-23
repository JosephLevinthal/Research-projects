tem = int(input("Quantidade inicial: "))
cresce = int(input("Percentual de crescimento: "))
mes = 0
while (tem > 0 and tem < 8000):
	tira = int(input("Quantidade retirada: "))
	tem = tem + (tem*cresce)/100
	tem = tem - tira
	mes = mes + 1
if (tem <= 0):
	print("ZERO")
else:
	print("MAXIMO")
print(mes)
	

	
	
	
