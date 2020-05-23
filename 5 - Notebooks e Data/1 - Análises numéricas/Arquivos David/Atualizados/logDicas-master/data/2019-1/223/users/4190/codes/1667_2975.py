qsu = int(input('Qual a quantidade de sucos? '))
qsa = int(input('Qual a quantidade de salgados? '))
grana = float(input('Qual o valor disponivel? '))

suco = qsu*3
salg = qsa*3.50
total = suco + salg

if (grana>=total):
	mensagem = 'Sim'
else:
	mensagem = 'Nao'
	
print(round(total,2))
print(mensagem)