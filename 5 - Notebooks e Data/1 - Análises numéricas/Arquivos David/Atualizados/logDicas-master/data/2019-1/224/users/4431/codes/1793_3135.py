from numpy import*
x=array(eval(input("Digite um vetor: ")))
h=0
m=0
while(size(x)>h):
	m=m+(x[h]**0.5)
	h=h+1
m=(m/size(x))	
m=(m**2)
print(round(m,2))


	
