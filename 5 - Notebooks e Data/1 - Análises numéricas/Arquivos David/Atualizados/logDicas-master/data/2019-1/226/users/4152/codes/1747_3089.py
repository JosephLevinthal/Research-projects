num = int(input("Digite aqui o numero representante do movimento: "))
soma = 0 #Acumuladora
while (num != 0):
	soma = soma + num
	num = int(input("Digite aqui o numero representante do movimento: "))
if (soma == 0):
	msg = "Inicial"
elif (soma > 0):
	msg = "Direita"
else:
	msg = "Esquerda"
print(soma)
print(msg)