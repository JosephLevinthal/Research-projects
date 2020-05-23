n = int(input("digite numero: "))
resto = n%100
formula = n%resto

if(formula==0):
	mensagem = "SIM"
else:
	mensagem = "NAO"

print(mensagem)