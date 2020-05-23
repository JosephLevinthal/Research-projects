from numpy import*
x=array(eval(input("vetor positivo: ")))
h=0
m=0
while(size(x)>h):
	m=m+(x[h]**0.166666)
	h=h+1
m=(m/size(x))
m=(m**6)
print(round(m, 2))

