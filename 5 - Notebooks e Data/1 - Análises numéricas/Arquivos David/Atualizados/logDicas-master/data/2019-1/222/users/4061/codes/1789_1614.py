from numpy import *

alimentos = array(eval(input("digite alimentos: ").upper()))
quant = array(eval(input("digite quantidade: ").upper()))

banana = 0
bife = 0
feijoada = 0
omelete = 0
tomate = 0
cont = 0
while(cont < size(alimentos)):
	if(alimentos[cont].upper() == "BANANA"):
		banana = banana + (quant[cont]*0.97)
	if(alimentos[cont].upper() == "BIFE"):
		bife = bife + (quant[cont]*2.95)
	if(alimentos[cont].upper() == "FEIJOADA"):
		feijoada = feijoada +(quant[cont]*1.27)
	if(alimentos[cont].upper() == "OMELETE"):
		omelete = omelete +(quant[cont]*1.04)
	if(alimentos[cont].upper() == "TOMATE"):
		tomate = tomate +(quant[cont]*0.2)
	cont = cont + 1
total = banana + bife + feijoada + omelete + tomate
print(round(total,2))