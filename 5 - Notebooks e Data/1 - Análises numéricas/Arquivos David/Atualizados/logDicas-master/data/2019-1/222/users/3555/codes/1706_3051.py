consumo = float(input())
if(0<= consumo <= 150):
	t = 1
if(150< consumo <= 250):
	t = 2
if(250 < consumo <= 350):
	t = 3
if(350 < consumo ):
	t=4
	
if(t == 1):
	valor = consumo*0.6  + 5
if(t == 2):
	valor = consumo*0.65 + 8
if(t == 3):
	valor = consumo*0.7 + 12 
if(t==4):
	valor = consumo*0.75 + 16

print(valor)