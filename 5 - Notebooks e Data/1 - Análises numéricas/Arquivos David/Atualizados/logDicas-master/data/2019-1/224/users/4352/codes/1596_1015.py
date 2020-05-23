# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

x = int(input("digite: "))
y = int(input("digite: "))
z = int(input("digite: "))
v1 = min(x, y, z)
v2 = max(x, y, z)
intermediario = x + y + z - v1 - v2
print(v1)
print(intermediario) 
print(v2)
