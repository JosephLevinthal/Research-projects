from math import*
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
v0 = float(input("velocidade inicial: "))
a = radians(float(input("angulo do lancamento: ")))
d = float(input("distancia horizontal: "))
g = 9.8
r = ((v0**2)*sin(2*a))/g


if (abs(d - r) <= 0.1):
	men = "sim"
else:
	men = "nao"
print(men)