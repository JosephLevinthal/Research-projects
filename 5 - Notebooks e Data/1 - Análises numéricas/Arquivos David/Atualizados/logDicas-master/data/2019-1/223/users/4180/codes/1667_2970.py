t = float(input( "Tempo de Investimento: " ))
Qf = 1500*t
Qi = 1500

from math import * 

i = (sqrt(Qf/Qi**1/t)-1)

if ( i <= (0.01)):
	print("Real")
	
else:
	print("Irreal")
