qtdAtual = int(input("Insira a quantidadde inicial de pirarucus no tanque: "))
percent = float(input("Insira o percentual de crescimento mensal sobre os pirarucus: "))

cap = 8000
meses = 0

while(qtdAtual > 0 and qtdAtual < cap):
	venda = int(input("Insira a quantidade de pirarucus retirados para a venda: "))
	qtdAtual = qtdAtual + (qtdAtual * (percent / 100)) - venda
	meses = meses + 1
	
if(qtdAtual <= 0):
	print("ZERO")
elif(qtdAtual >= cap):
	print("MAXIMO")

print(meses)