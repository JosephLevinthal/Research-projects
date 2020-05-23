# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
H = float(input("Digite a altura: "))
h = float(input("Digite o nivel de combustivel: "))
r = float(input("Digite o raio: "))
print("Entradas:" ,H, "," ,r, "," ,h)

if(h < 0 or H < 0 or r < 0):
	vol = -1
	print("Entrada invalidas")
elif(h < r):
	vol = (1./3) * pi * h**2 * (3 * r - h)
elif(h < H - r):
	vol = (2./3) * pi * r**3 + pi * r**2 * (h - r)
elif(h <= H):
	vol = (4./3) * pi * r**3 + pi * r**2 * (H - 2 * r) - (1/3) * pi * (H - h)**2 * (3 * r - H + h )
else:
	vol = -1
	print("Entrada invalidas")

msg = round(vol, 6)
print("Volume:" , msg , "litros")
	