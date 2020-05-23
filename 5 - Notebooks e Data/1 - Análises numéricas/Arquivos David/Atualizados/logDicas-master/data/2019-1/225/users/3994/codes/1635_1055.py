# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
v = float(input(" Digite velocidade"))
a = radians(float(input(" Digite angulo")))
D = float(input(" Digite distancia horizontal"))
R = ((v**2) * (sin(2*a)))/9.8
h=abs(D-R)
if(h<=0.1):
	mensagem = " sim "
else:
	mensagem = " nao"
print(mensagem)
