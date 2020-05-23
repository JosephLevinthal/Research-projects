from numpy import *

time_casa = array(eval(input("Gols realizados: ")))
time_adv = array(eval(input("Gols sofridos: ")))
resultado = zeros(3, dtype=int)

for x,y in zip(time_casa,time_adv):
	if(x > y):
		resultado[0] += 1
	elif(x < y):
		resultado[2] += 1
	else:
		resultado[1] += 1

print(resultado)