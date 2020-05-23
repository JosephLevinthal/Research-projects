# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

# Ler o valor do raio
from math import*
r = float (input ("entrar com o valor do raio:" ))

# valores da area do circulo e o volume da esfera
area_cir = pi*(r**2)
vol_esf = (4/3)*pi*(r**3)

# impressao area do circulo e o volume da esfera
print(round (area_cir,3))
print(round (vol_esf,3))

