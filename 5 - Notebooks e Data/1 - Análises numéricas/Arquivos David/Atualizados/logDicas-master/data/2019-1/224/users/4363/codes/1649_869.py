# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

a = float(input("preco da compra:"))
if (a>200):
 a = a-a*(5/100)
else:
 a = a

print(round(a,2))
