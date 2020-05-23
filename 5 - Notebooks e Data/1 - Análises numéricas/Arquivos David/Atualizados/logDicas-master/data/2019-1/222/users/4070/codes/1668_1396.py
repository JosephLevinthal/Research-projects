conta = float(input("consumido:"))

if (conta <= 300):
   mensagem = (conta * 0.1) + conta

else :
	mensagem = (conta * 0.06) + conta

print(round(mensagem, 2))