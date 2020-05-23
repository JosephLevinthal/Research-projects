# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
n = int(input("numero: "))
a1 = int(n // 1000)
n = int(n % 1000)
a2 = int(n // 100)
n = int(n % 100)
a3 = int(n / 10)
n = int(n % 10)
a4 = int(n / 1)
Soma = a1 + a2 + a3 + a4
print(Soma)