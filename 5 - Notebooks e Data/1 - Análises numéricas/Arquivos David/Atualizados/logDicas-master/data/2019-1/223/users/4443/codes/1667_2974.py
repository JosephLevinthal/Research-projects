#Leitura da quantidade de acai
acai = float(input("quanto de acai? "))
salgado = int(input("quantos salgados? "))
pgto = float(input("valor pago: "))

kg = acai/1000

#Calculo
preco = (kg*24.00 + salgado*3.00)
preco = round(preco, 2)
print(preco)

if(pgto > preco):
	print("Sim")
else:
	print("Nao")