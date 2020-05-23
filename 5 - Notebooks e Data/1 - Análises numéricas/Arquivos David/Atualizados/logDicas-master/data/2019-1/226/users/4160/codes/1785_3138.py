from numpy import *
n = array(eval(input("Vetor: ")))
i=0
m=0
while(i<size(n)):
	m = m + n[i]**7
	i = i +1
x = m/size(n)
y = x**(1/7)
print(round(y,2))