# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input("digite um valor a: "))
b = int(input("digite um valor b: "))
c = int(input("digite um valor c: "))
print(min(a, b, c), a+b+c-min(a, b, c)-max(a, b, c), max(a, b, c))
