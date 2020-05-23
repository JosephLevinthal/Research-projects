from numpy import *
n = array(eval(input("digite :")))
i=0
p1 = 0 
while(i<size(n)):
	p1 = p1 + (n[i])**(5)
	i = i +1
M = ((p1)/size(n))**(1/5)
print(round(M,2))