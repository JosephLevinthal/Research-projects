from numpy import*
x=array(eval(input("digite o numero:")))
a=1
b=sum(x)/size(x)
for i in x:
	a=a*abs(i-b)
d=(a)**(1/size(x))
print(round(d,3))