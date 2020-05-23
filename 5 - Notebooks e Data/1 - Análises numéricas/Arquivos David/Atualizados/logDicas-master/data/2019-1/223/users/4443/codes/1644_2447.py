#Leitura dos valores de preco e pagamento
x = float(input("preco: "))
y = float(input("pagamento: "))

#Calculo da diferenca ou troco
if(x > y):
	print("Falta "+ str(round(x - y, 2)))
if(y >= x):
	print("Troco de " + str(round(y - x, 2)))