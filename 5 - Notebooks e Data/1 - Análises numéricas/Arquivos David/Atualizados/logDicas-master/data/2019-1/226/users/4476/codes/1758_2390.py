from numpy import *

v1 = array(eval(input("P: ")))
v2 = array(eval(input("F: ")))

a = max
i = 0
mes = 1

while (v1[i] != max(v1)):
	mes = mes + 1
	i = i + 1
print(mes)