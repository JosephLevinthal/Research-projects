# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
H=float (input ("altura do tanque: "))
h=float (input ("nivel de combustivel: "))
r=float (input ("raio dos bojos semiesfericos: "))
print ("Entradas:",H,",",h,",",r)
if (H>0 and h>0 and r>0 and H>h and H>2*r):
    if (h < r):
        v= (1/3)*pi*(h**2)*(3*r-h)
    elif (h < H-r):
        v= (2/3)*pi*(r**3) + pi*(r**2)*(h-r)
    elif (h <= H):
        v= 4/3*pi*(r**3)+pi*(r**2)*(H-2*r)- (1/3)*pi*((H-h)**2)*(3*r-H+h)
    print ("Volume:",round (1000*v,3),"litros")
else:
    print ("Entradas invalidas")
