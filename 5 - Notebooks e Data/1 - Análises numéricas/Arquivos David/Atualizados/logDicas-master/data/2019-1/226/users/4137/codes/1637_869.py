# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
pcr = float(input("Qual o preco da conta:"))

if (pcr >= 200):
	dsc = pcr * (5/100)
	pcr = pcr - dsc
		
print(round(pcr, 2))