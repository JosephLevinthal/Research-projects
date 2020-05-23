from numpy import *

cont = zeros(3, dtype=int)

t = array(eval(input("gols efetuados: ")))
ta = array(eval(input("gols sofridos: ")))

for i in range(size(t)):
	if t[i] > ta[i]:
		cont[0] = cont[0] + 1
	elif t[i] == ta[i]:
		cont[1] = cont[1] + 1
	elif t[i] < ta[i]:
		cont[2] = cont[2] + 1
print(cont)
