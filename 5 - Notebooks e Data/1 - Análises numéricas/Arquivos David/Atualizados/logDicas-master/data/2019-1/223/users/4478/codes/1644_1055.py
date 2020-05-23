# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
import math
v0 = float(input("velocidade incial: "))
alfa = math.radians(float(input("angulo alfa: ")))
D =  float(input("distancia: "))
R1 = (v0**2*math.sin(2*alfa)) 
R = R1/9.8
X = abs(D - R)
if():
	Mensagem = "sim"
else:
	mensagem = "nao"
print(mensagem)