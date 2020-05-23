# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
numero = int(input("Digite um numero de 4 algarismos: "))
primeiro_algarismo = numero // 1000
segundo_algarismo = (numero % 1000) // 100
terceiro_algarismo = ((numero % 1000) % 100) // 10
quarto_algarismo = (((numero % 1000) % 100) % 10)
soma_algarismos = primeiro_algarismo + segundo_algarismo + terceiro_algarismo + quarto_algarismo
print(soma_algarismos)
