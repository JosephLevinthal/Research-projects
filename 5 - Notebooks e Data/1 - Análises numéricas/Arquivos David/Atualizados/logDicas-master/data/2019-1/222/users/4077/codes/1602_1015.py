# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a= int(input("6"))
b= int(input("2"))
c= int(input("4"))
minimo= min(a,b,c)
maximo= max(a,b,c)
medio= (a + b + c) - maximo - minimo
print(minimo)
print(medio)
print(maximo)
