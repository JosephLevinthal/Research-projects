# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
vel=float(input("velocidade: "))
ang=float(input("angulo do vetor: "))
distancia=float(input("distancia: "))
ace=9.8
r= (  ((vel)**2)  *  sin(2*   radians(ang)  )  )  /ace
if(abs(distancia-r) <0.1 ):
	mensagem="sim"
	print(mensagem)
else:
	mensagem="nao"
	print(mensagem)
	
