from numpy import*
v1=array(eval(input()))
v2=array(eval(input()))
soma=0
i=0
while(i<size(v1)):
	calc=(v1[i]-v2[i])**2
	soma=soma+calc
	i=i+1
soma=(soma)**0.5
print(round(soma,4))