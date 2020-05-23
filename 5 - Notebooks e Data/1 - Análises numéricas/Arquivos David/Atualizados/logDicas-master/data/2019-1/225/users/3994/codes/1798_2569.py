from numpy import*
x = array(eval(input("Digite o numero: ")))
soma = 0 
d=0
for i in range(size(x)):
	soma = soma + x[i]
media =  soma/size(x)
for i in range(size(x)):
	d = d+(x[i]-media)**2
	q = size(x)-1
	a = (d/q)**0.5
print(round(a,3))
	
	