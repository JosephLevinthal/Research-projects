# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
import math
raiotanque = float(input("Raio do Tanque : "))
colunaar = float(input("Coluna de ar : "))
opcao = int(input("Calculo ( 1 )-Ar / ( 2 )-Combustivel"))

vesfera = (4*math.pi*raiotanque**3)/3
vcalota = (math.pi*colunaar**2*(3*raiotanque-colunaar))/3
vcombustivel = vesfera-vcalota

if(opcao == 1):
	print(round(vcalota,4))
else:	
	print(round(vcombustivel,4))
