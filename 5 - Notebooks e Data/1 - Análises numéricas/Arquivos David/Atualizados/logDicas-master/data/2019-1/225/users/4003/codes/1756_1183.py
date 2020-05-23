from numpy import *

n1 = array(eval(input("digite um numero: ")))
a=0 #quant. de elemento nao negativo
b=0 #copilador
c=0 #controlar a posicao de entrada do vetor

while(c<size(n1)):
	if(n1[c]>0):
		a=a+1
	c=c+1
c=0
v=arange(a)
while(c<size(n1)):
	if(n1[c]>0):
		v[b]=n1[c]
		b=b+1
	c=c+1
print(v)
	
	
