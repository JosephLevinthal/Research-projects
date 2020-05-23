from numpy import *
from numpy.linalg import*
mat=array([[10,12,15],[6,8,12],[12,12,18]])
vet=array(eval(input()))
vet=vet*60


a=dot(inv(mat),vet.T)
print("cadeira:",round(a[0],0))
print("bau:",round(a[1],0))
print('mesa:',round(a[2],0))
if a[0]==max(a):
	print("cadeira")
elif a[1]==max(a):
	print("bau")
elif a[2]==max(a):
	print('mesa')