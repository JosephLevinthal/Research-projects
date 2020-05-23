# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
H = float(input())
h = float(input())
r = float(input())
pi = 3.14159265359
if H<=0 or h<=0 or r<=0 or H<h or H<2*r:
	print("Entradas:",H ,",", h ,",", r)
	print("Entradas invalidas")
else:
	v = (4/6)*pi*(r**3)+(h-r)*pi*r**2
	print("Entradas:",H ,",", h ,",", r)
	print("Volume:",round(v*1000,3),"litros")