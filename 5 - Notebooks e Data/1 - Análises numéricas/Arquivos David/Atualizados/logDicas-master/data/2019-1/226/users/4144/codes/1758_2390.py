from numpy import *
p = array(eval(input("digite os presentes: ")))
f = array(eval(input("digite os faltosos: ")))
a = max
i = 0
mes = 1
while(p[i] != max(p)):
	mes = mes + 1
	i = i + 1
print(mes)