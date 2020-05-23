x = int(input("insira o numero x:"))

soma = 0


while(x != 0):
	soma = soma + x
	x = int(input("insira x:"))

if(soma > 0):
	msg = "Acima"
elif(soma == 0):
	msg = "Inicial"
else:
	msg = "Abaixo"
print(soma)
print(msg)


