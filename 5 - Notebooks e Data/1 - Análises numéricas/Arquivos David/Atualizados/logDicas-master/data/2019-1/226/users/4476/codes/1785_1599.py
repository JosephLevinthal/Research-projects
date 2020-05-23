from numpy import *

vc = array(eval(input("digite os valores: ")))

i = 0

while (i < size(vc)):
	if (vc[i] > 80):
		a = (vc[i] * (15/100))
		vc[i] = vc[i] - a
	i = i + 1
print(round(sum(vc), 2))