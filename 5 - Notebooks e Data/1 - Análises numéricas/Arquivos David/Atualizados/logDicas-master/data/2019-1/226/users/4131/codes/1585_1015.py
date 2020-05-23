# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a= int(input("valor:"))
b= int(input("valor:"))
c= int(input("valor:"))
print(min(a,b,c))
print((a+b+c)-min(a,b,c)-max(a,b,c))
print(max(a,b,c))