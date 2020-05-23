from numpy import*
from numpy.linalg import*
a=array(eval(input("notas: ")))
b=int(input("n.alunos: "))
c=0
for i in range(a.shape[0]):
	c=(a[i,1]+c)shape(a)[0]
	if(c>=5):
		print("PASSOU")
		print("REPROVOU")
		
	