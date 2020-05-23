# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input("numero 1: "))
b = int(input("numero 2: "))
c = int(input("numero 3: "))

menor = min(a, b, c)
maior = max(a, b, c)

print(menor)
print((a + b + c) - menor - maior)
print(maior)