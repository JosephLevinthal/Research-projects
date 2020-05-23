# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
import math
R = float(input("Digite o raio:"))

A = math.pi * R * R
V = math.pi * R * R * R * 4/3
print(round(A,3),round(V,3))