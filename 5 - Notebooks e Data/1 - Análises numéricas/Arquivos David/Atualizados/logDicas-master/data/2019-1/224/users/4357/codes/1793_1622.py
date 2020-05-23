from numpy import*
e=array(eval(input("digite o numero:")))
s=array(eval(input("digite o numero:")))
i=0
soma=0
while(i<size(e)):
	if(e[i]!= s[i]):
		soma=soma+(e[i]-s[i])
	i=i+1
print(soma)
		