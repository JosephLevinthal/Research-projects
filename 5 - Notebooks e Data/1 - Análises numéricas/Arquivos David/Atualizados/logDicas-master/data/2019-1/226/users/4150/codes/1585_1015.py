# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

a = int(input("valor 1: "))
b = int(input("valor 2: "))
c = int(input("valor 3: "))


minimo = (min(a,b,c))
maximo = (max(a,b,c))
intermediario1 = (a+b+c)
intermediario = intermediario1 - ( minimo+maximo)

print(minimo)
print(intermediario)
print(maximo)
