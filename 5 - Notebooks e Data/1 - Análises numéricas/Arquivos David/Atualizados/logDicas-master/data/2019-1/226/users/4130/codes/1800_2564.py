from numpy import *

ngp = array(eval(input("Numero de gols pro por partida: ")))
ngc = array(eval(input("Numero de gols contra por partida: ")))

x = zeros(3, dtype = int)

for i in range(size(ngp)):
	if(ngp[i] > ngc[i]): #Vitoria
		x[0] = x[0] + 1
	elif(ngp[i] == ngc[i]): #Empate
		x[1] = x[1] + 1
	elif(ngp[i] < ngc[i]): #Derrota
		x[2] = x[2] + 1
print(x)