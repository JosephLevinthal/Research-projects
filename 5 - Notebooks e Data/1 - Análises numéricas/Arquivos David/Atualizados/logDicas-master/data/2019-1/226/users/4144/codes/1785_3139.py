from numpy import *
a = array(eval(input("digite o vetor: ")))
i = 0
num = 0
while(i<size(a)):
	num = num + (a[i])**(1/3)
	i = i + 1
m = (num/size(a))**3
print(round(m,2))
