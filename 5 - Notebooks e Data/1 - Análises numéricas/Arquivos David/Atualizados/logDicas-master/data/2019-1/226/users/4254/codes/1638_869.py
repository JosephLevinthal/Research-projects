# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
p = float(input("Digite o preco: "))

if(p >= 200):
	desc = (p - ((p*5)/100))
else:
	desc = p
print(round(desc,2))