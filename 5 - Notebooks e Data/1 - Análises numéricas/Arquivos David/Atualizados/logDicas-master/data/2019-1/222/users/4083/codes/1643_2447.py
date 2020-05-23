a = float(input("Digite o preco: "))
b = float(input("Digite a pagamento: "))

devedor = (a - b)
troco = (b - a)
if  (a > b):
     print("Falta",devedor)
	
else:
    print("Troco de ",troco)
