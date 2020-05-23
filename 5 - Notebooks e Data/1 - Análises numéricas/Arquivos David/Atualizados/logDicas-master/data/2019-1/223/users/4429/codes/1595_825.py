# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import pi
r = float(input("Insira o valor para o raio do circulo: "))
area = pi*(r**2)
print(round(area, 3))

# Calculo do volume do circulo:
volume = 4/3*pi*(r**3)
print(round(volume, 3))
