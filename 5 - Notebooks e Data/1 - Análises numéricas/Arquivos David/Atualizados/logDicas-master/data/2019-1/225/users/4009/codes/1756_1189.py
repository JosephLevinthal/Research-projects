from numpy import *

bolsonaro = input("hcsdchsv: ").upper()
bolsonaro = bolsonaro.replace('','')

hdtv= (".")
cont= -1
haddadnao= 1
ustra= 0

while (cont >= -len(bolsonaro)):
	hdtv = hdtv + bolsonaro[cont]
	if(bolsonaro[ustra]) != (bolsonaro[cont]):
		haddadnao= 0 
	ustra = ustra + 1
	cont= cont - 1
	
print(bolsonaro)
print(haddadnao)