from numpy import*
x=array(eval(input("Digite um vetor:")))
h=0
m=0
while(size(x)>h):
	m=m+(log(x[h]+1))
	h=h+1
m=(m/size(x))
m=(exp(m)-1)
print(round(m,2))
	