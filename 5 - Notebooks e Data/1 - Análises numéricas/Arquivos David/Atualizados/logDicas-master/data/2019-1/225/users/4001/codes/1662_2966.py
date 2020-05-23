opcao = input("S/N? ")
ing = float(input("Valor do ingresso: "))
n = int(input("Qtd de ingressos? "))
# Desconto
n2 = (ing - (ing * 20/100)) * n
n3 = ing * n
if(opcao == "S"):
	msg = n2
else:
	msg =  n3
print(round(msg, 2))