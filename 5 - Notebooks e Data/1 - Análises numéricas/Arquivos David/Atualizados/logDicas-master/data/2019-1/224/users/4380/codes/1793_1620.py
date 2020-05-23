from numpy import *
t=array(eval(input("tempo do banho: ")))
perc=array(eval(input("porcentagem de abertura: ")))
p=0
agua=0
while (p<size(t)):
	agua=agua+(0.05)*perc[p]*t[p]
	p=p+1
print(float(round(sum(agua),2)))