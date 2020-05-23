# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
raio = float(input("digite raio: "))
altura = float(input("digite altura: "))
numero = int(input("digite numero: "))
combustivel = (4*pi*(raio**3))/3
ar = (pi*(altura**2)*(3*raio-altura))/3
if(numero ==1):
	mensagem = ar
else:
	mensagem = combustivel - ar
print(round(mensagem, 4))