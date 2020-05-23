from numpy import*
x=array(eval(input("digite um vetor: ")))
h=0
m=0
while(size(x)>h):
	m=m+(x[h]**(-1))
	h=h+1
m=(m/size(x))
m=(m**-1)
print(round(m,2))