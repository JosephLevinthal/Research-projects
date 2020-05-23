from numpy import*
from numpy.linalg import*

a=array(eval(input("Digite a matriz: ")))
a=a

for i in range(4):
	a[:,i]=sorted(a[:,i],reverse=True)
print(a)	