# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *

r = float(input("Raio do tanque: "))
h = float(input("Altura do tanque: "))

sn = input("1 indica o volume de ar, 2 indica o volume de combustivel: ")
volAR = ((pi * (h ** 2)) * (3 * r - h)) / 3
volCOMB = ((4 * pi * (r ** 3)) / 3) - ((pi * (h ** 2)) * (3 * r - h)) / 3

if(sn == "1"):
	mensagem = volAR
if(sn == "2"):
	mensagem = volCOMB
	
print(round(mensagem, 4))