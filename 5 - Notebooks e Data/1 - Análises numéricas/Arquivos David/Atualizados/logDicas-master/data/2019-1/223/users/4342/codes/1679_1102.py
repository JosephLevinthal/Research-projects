#calcular o volume de combustivel
#primeiro colocar as variaveis
#verificar se entradas sao validas; var>0 e H>h e 2*r
#colocar a str na frente das variaveis
#h pode ser abaixo do meio;no meio; acima do meio
#se h acima do meio, V= Vcil-Vcalota
from math import *
var1=float(input("altura total do tanque:"))
var2=float(input("nivel de combustivel:"))
var3=float(input("raio do bojo:"))
vcil=(((pi)*((var3)**2))*var1)
vcalota=(((pi)/3)*((var2)**2)*((3*var3)-var2))
vesf=(4/3*((pi)*(var3**3)))
var=(vesf-vcalota)
V=(vcil-var)*1000
V2=((vcil/2)-vcalota)*1000
V3=(var)*1000

if((var1>0) and (var2>0) and (var3>0)):
	print(("Entradas:"), var1,",",var2,",",var3)
else:
	print(("Entradas:"),var1,var2,var3)
	print("Entradas invalidas")
if(var2>1):
	print("Volume:",(round(V, 3)),"litros")
elif(var2==1):
	print("Volume:",(round(V2, 3)),"litros")
elif(var2<1):
	print("Volume:",(round(V3, 3)),"litros")
	
	