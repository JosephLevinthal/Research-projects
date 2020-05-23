from numpy import *
n = array(eval(input("Digite um conjunto de n numeros reais positivos: ")))
i=0
num = 0
while(i<len(n)):
	num = num + n[i]**-1
	i = i+1
q = num/len(n)
mh = q**-1
print(round(mh,2))

