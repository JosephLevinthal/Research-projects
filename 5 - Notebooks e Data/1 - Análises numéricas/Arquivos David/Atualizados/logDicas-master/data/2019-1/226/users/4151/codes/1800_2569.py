from numpy import*
x=array(eval(input("digite um vetor: ")))
m=sum(x)/size(x)
d=0
n=size(x)
for i in range(size(x)):
	d=(((x[i]-m)**2)/(n-1))+d
	
print(round(d**(1/2),3))
	
	
	
