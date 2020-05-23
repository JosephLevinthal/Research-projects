from numpy import*
a = array(eval(input("presenca: ")))
b = array(eval(input("faltosos: ")))

mes = 1
i = 0
while(a[i] != max(a)):
	mes = mes + 1
	i = i + 1
print(mes)