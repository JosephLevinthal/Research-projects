# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
numero = int(input("numero com 4 algarismo: "))
primeiro_algarismo = numero // 1000
segundo_algarismo = (numero % 1000) // 100
terceiro_algarismo =((numero % 1000) % 100) // 10
quarto_algarismo = (((numero % 1000) % 100) % 10)
somatorio_algarismo = primeiro_algarismo + segundo_algarismo + terceiro_algarismo + quarto_algarismo
print(somatorio_algarismo)
