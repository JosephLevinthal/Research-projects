# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
p=float(input("preco:"))
o=p*5
u=o/100
d=p-u
if(p>=200):
	p=d

else:
	p=p

print(round(p,2))