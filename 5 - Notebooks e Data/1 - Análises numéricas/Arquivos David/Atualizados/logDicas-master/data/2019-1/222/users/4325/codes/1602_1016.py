# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
ladoA = float(input("Lado A:"))
ladoB = float(input("Lado B:"))
ladoC = float(input("Lado C:"))
semi = ((ladoA+ladoB+ladoC)/2)
arena = (semi*(semi-ladoA)*(semi-ladoB)*(semi-ladoC))
area = (sqrt(arena))
print(round(area,5))