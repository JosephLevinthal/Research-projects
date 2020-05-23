# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
a = float(input('altura total: '))
b = float(input('nuvel do tanque: '))
c = float(input('raio dos bojos: '))
print('Entradas:',a,',',b,',',c)
if (a>0) and (b>0) and (c>0) and (a>b) and (a>(2*c)):
	if b<= c:
		v = (pi/3)*(b**2)*(3*c-b)
		print('Volume:',round(v*1000,3),'litros')
	elif (c<b and b<= a-c):
		v = (4*pi*(c**3)/6)+(pi*(c**2)*(b-c))
		print('Volume:',round(v*1000,3),'litros')
	elif (b>a-c):
		v = ((4*pi*(c**3))/6)+((pi/3)*((c**2)*(b-c))*2)
		print('Volume:',round(v*1000,3),'litros')
else:
	print('Entradas invalidas')