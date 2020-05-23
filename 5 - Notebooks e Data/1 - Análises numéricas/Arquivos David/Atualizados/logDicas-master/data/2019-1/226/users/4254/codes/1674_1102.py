# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
H= float(input("Digite a altura total do tanque: "))
h= float(input("Digite o nivel do combustivel do tanque: "))
r= float(input("Digite o raio dos bojos: "))
from math import*

print("Entradas:",H,",",h,",",r)
ve=((4/3)*pi*(r**3))
vc=((pi/3)*((2*r - h)**2)*(3*r - (2*r-h)))
vci= pi*(r**2)*(h-r)

if(H<0 or h<0 or r<0 or H<=h or H<=2*r):
	print("Entradas invalidas")
elif(h<=r):
	V=((ve -vc)*1000)
	print("Volume:",round(V,3),"litros")
elif(h>r and (H-h)>r):
	V=(((ve/2)+vci)*1000)
	print("Volume:",round(V,3),"litros")
elif(h>r and (H-h)<=r):
	V=(((ve+vci)-vc)*1000)
	print("Volume:",round(V,3),"litros")
	
	
	
	