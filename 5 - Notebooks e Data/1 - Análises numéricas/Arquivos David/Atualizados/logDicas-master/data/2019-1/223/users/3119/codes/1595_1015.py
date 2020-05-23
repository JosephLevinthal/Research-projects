# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

a = int(input("digite o numero a: "))
b = int(input("digite o numero b: "))
c = int(input("digite o numero c: "))

minimo = min(a,b,c)
maximo = max(a,b,c)
medio = (a + b +c) - minimo - maximo

print(minimo)
print(medio)
print(maximo)
