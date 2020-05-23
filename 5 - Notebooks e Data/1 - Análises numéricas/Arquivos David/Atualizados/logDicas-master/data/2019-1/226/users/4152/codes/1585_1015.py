# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
x = int(input("Valor 1: "))

y = int(input("Valor 2: "))

z = int(input("Valor 3: "))

ultimo = max(x,y,z)

primeiro = min(x,y,z)

intermediario = (x + y + z) - (primeiro + ultimo)

print(primeiro)

print(intermediario)

print(ultimo)