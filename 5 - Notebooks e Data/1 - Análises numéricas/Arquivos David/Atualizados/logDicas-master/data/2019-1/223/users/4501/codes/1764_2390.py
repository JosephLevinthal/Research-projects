from numpy import *
pre = array(eval(input("Digite o numero de presentes a cada mes: ")))
falt = array(eval(input("Digite o numero de faltantes a cada mes: ")))
freq = pre - falt
mes = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
i = 0
while(freq[i] != max(freq)):
	i = i+1
print(mes[i]) 