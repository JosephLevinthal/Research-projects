from numpy import *

golpro = array(eval(input("")))
golcon = array(eval(input("")))

x = zeros(3, dtype = int)

for i in range(size(golpro)):
	
	if golpro[i] > golcon[i]:
		x[0] += 1
	elif golpro[i] == golcon[i]:
		x[1] += 1
	elif golpro[i] < golcon[i]:
		x[2] += 1

print(x)
