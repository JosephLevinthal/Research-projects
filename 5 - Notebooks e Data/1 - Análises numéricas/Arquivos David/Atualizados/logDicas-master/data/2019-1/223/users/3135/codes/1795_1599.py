from numpy import*
c= array(eval(input("Insira o valor das compras:")))
i=0
p=0.15

ct=0
while(i < size(c)):
	if (c[i] > 80):
		d= c[i] * p
		c[i]=c[i]-d
	i=i+1
	ct=sum(c)
print(round(ct,2))