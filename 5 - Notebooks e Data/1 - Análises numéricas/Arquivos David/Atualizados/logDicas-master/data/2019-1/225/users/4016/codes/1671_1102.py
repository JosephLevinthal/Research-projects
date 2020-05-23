# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
H=float(input("altura total do tanque:"))
h=float(input("nível de combustivel do tanque:"))
r=(float(input("raio dos bojos semieféricos inferior e superior:")))
print("entradas: " H,",",h,",",r)
from math import*
if((H>0)and(h>0)and(r>0)and(H>2*r)):
	if(H==r):
		vol=((4/3)*pi*(r**3))/2
		print("volume:",(round((vol*1000),3)),"litros")
	elif(h<r):
		vol=