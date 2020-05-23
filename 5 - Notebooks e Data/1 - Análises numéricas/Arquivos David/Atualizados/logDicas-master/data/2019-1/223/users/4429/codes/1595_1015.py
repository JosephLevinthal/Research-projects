# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a=(int(input("digite o numero a: ")))
b=(int(input("digite o numero b: ")))
c=(int(input("digite o numero c: ")))

r=((a+b+c)-min(a,b,c)-max(a,b,c))
print(min(a,b,c))
print(r)
print(max(a,b,c))
	