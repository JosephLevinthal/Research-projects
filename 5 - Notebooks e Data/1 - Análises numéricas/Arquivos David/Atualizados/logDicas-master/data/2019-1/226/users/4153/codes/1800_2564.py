from numpy import *

# numero de gols em cada partida
ng = array(eval(input("Insira: ")))
# numero de gols do time adv.
ga = array(eval(input("Insira: ")))

x = zeros(3, dtype=int)

for i in range(size(ng)):
	if(ng[i]>ga[i]):
		x[0] = x[0] + 1
	elif(ng[i] == ga[i]):
		x[1] = x[1] + 1
	elif(ng[i] < ga[i]):
		x[2] = x[2] + 1
print(x)