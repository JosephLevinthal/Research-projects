from numpy import*
from numpy.linalg import*
vet=array(eval(input("entre com o vetor xyz:")))

vetm=vet*60

mat=array([[10,12,15],
			  [6,8,12],
			  [12,12,18]])

re=dot(inv(mat),vetm.T)
a=shape(re)[0]

for i in range(a):
	if(i==0):
		print("cadeira:",round(re[i],0))
	elif(i==1):
		print("bau:",round(re[i],0))
	elif(i==2):
		print("mesa:",round(re[i],0))
if(max(re)==re[0]):
	print("cadeira")
elif(max(re)==re[1]):
	print("bau")
elif(max(re)==re[2]):
	print("mesa")

