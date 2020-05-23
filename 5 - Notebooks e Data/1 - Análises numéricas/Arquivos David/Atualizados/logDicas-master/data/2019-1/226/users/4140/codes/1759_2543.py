from numpy import*
v1=array(eval(input()))
i=-3
a=str(v1[-1])
b=str(v1[-2])+str("x")
soma=str(v1[i])+str("x") +str('^')+str(abs(i)-1)
while(abs(i)<size(v1)):
	i=i-1
	if(v1[i]!=0):
		soma=str(v1[i])+str("x")+str('^')+str(abs(i)-1)+str(" + ") +str(soma)
print(soma,"+",b,"+",a)