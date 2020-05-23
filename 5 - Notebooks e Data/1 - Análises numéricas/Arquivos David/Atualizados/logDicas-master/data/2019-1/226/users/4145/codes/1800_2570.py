from numpy import*
x=array(eval(input("vetor: ")))
m=sum(x)/size(x)
p=1
for i in range(size(x)):
	p= abs(x[i]-m)*p
print(round(p**(1/size(x)),3))	
