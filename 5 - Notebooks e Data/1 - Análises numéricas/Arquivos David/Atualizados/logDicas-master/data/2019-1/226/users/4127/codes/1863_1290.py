from numpy import*
from numpy.linalg import*

k= array(eval(input("digite seu vetor")))
k=k*60
a= array([[10,12,15],[6,8,12],[12,12,18]])
d= dot(inv(a),k.T)


print("cadeira:",round(d[0],0))
print("bau:",round(d[1],0))
print("mesa:",round(d[2],0))

if max(d)==d[0]:
	print("cadeira")
if max(d)==d[1]:
	print("bau")
if(max(d)==d[2]):
	print("mesa")
	