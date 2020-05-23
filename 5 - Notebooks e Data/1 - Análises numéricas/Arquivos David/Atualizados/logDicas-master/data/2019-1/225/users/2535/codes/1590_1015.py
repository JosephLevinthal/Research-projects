# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

x = int(input())
y = int(input())
z = int(input())

print(min(x,y,z))
print(x + y + z - min(x,y,z) - max(x,y,z))
print(max(x,y,z))