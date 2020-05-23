
valor = float(input("Digite o valor: "))
quant_tickets = int(input("Digite a quantidade de tickets: "))
valor_tickets = float(input("Digite o valor dos tickets: " ))
quant_passes = int(input("Digite a quantidade de tickets: "))
valor_passes = float(input("Digite o valor dos tickets: "))

resultado = valor - ( (quant_tickets * valor_tickets) + (quant_passes * valor_passes))

if(resultado < 0):
	mensagem = "INSUFICIENTE"
else:
	mensagem = "SUFICIENTE"
	
print(mensagem)