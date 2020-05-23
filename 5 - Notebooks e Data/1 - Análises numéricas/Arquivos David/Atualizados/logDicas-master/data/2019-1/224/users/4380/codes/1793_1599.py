from numpy import *
vc=array(eval(input("custo dos itens: ")))
p=0
m
while (p<size(vc)):
	if (vc[p]>80):
		vc[p]=vc[p]*0.15
	p=p+1
print(float(round(sum(vc),2)))	