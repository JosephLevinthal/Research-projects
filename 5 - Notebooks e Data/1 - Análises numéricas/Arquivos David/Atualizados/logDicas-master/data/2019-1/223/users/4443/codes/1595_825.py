# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

# Leitura do raio a partir do teclado:
r = float(input("Insira o valor para o raio do circulo: "))

# Calculo da area do circulo:
from math import pi
area = pi*(r**2)
print(round(area, 3))

# Calculo do volume do circulo:
volume = 4/3*pi*(r**3)
print(round(volume, 3))