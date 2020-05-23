# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
import math

vinicial=float(input("Informe a velocidade inicial :"))
angulo=float(input("Informe a angulo lancamento :"))
dporco=float(input("Informe a distancia do porco :"))
gravidade=9.8

dlancamento = ((vinicial**2)* math.sin(2*math.radians(angulo)))/gravidade

if(abs(dporco-dlancamento)<0.1):
	print("sim")
else:
	print("nao")



