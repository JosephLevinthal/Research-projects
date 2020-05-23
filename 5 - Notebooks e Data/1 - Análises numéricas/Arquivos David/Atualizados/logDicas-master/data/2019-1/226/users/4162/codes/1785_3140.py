from numpy import*
n=array(eval(input("insira n numeros reais positivos: ")))
de=size(n)
i=0
d=0
while i!=de:
	d=d+n[i]**5
	i=i+1
m=d/de
r=m**(1/5)
print(round(r,2))