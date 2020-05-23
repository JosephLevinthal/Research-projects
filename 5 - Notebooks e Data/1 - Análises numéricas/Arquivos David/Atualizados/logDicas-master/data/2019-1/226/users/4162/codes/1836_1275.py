from numpy import*
from numpy.linalg import*
n=array(eval(input("insira as faltas: ")))
t=shape(n)[0]
mt=zeros(t,dtype=int)
for i in range(t):
	mt[i] = sum(n[i,:])
print(mt)