from numpy import*
x=array(eval(input("numeros:")))
soma=0
p=1
for i in range(size(x)):
	soma+=x[i]
media=soma/size(x)
for i in range(size(x)):
	p=p*abs(x[i]-media)
	j=p**(1/size(x))

print(round(j,3))