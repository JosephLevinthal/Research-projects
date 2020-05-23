from numpy import *
v1 = array(eval(input("gols: ")))
v2 = array(eval(input("gols sofridos: ")))

new = zeros(3, dtype = int)

for i in range(size(v1)):
	if(v1[i] > v2[i]):
		new[0] = new[0] + 1
	elif(v1[i] == v2[i])