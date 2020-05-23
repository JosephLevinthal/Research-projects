acaiQtde = float(input("Quantidade de acai: "))
salgadoQtde = int(input("Quantidade de salgado: "))
valorPago = float(input("Valor pago pelo cliente: "))

acai = 0.024
salgado = 3

valorTotal = (acai * acaiQtde) + (salgado * salgadoQtde)

if valorPago > valorTotal:
	mensagem = 'Sim'
else:
	mensagem = 'Nao'

print (round(valorTotal,2))
print (mensagem)
