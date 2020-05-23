grana = float(input('Quanto em dinheiro? '))
qtick = int(input('Quantos tickets serao comprados? '))
valort = float(input('Qual o valor dos tickets? '))
qpasses = int(input('Quantos passes serao comprados? '))
valorp = float(input('Qual o valor dos passes? '))

compras = qtick*valort+qpasses*valorp
if (grana>=compras):
	mensagem = 'suficiente'
	
else:
	mensagem = 'insuficiente'
	
print(mensagem.upper())