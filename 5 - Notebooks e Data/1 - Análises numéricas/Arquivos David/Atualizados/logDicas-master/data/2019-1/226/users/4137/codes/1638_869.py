# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
pcr = float(input("Preco do produto:"))

if( pcr >= 200 ):
	desc = pcr * (5/100)
	desc1 = pcr - desc
	msg = desc1
else:
	msg = pcr
print(round(msg, 2))	