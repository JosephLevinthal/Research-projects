from numpy import*
v=array(eval(input("digite o numero:")))
i=0
soma=0
while(i<size(m)):
	if(i<m[i]):
		soma=soma+((v[0]**(-1)+v[1]**(-1)+v[2]**(-1)+...+v[n-1]**(-1))**(-1))/n
	i=i+1
print(round(soma,2))