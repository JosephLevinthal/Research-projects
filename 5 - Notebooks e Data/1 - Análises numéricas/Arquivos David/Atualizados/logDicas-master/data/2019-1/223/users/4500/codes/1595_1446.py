# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

comprar = float(input("Quantos litros comprou: "))

doar =comprar * (2/3)

resto = comprar - doar

print(round(resto, 3))
