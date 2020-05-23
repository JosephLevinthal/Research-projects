sucos = float(input("qual a quantidade de sucos? "))
salgados = float(input("qual a quantidade de salgados? "))
dinheiro = float(input("dinheiro disponivel? "))
suco = 3
salgado = 3.50
total = (suco * sucos) + (salgado *salgados)
if(total < dinheiro):
   msg = "Sim"
else:
	msg = "Nao"
print(round(total, 2))
print(msg)