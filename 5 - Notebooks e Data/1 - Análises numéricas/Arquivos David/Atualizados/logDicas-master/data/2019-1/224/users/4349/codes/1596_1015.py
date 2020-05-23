# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input("digite: "))
b = int(input("digite: "))
c = int(input("digite: "))
v1 = min(a, b, c)
v2 = max(a, b, c)
intermediario = a + b + c - v1 - v2
print(v1)
print(intermediario)
print(v2)