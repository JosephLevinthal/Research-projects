from numpy import *
t=array(eval(input("digite o tempo do banho: ")))
a=array(eval(input("digite o percentual de abertura: ")))
i=0
c=0
while(i<size(t)):
	lc=5* (a[i]/100)
	c=c+lc*t[i]
	i=i+1
print(round(c, 2))