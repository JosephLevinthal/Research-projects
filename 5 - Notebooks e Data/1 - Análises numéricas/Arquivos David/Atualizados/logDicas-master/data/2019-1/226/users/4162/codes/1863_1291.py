from numpy import*
from numpy.linalg import*
mt=array(eval(input("insira um vetor de entrada: ")))
c=array([[50,60,40],[30,40,20],[10,15,8]])
r= dot(inv(c),mt.T)
a=(r)[0]
b=(r)[1]
c=(r)[2]
a1=round((a),1)
b1=round((b),1)
c1=round((c),1)
print("regular:",a1)
print("ortopedico:",b1)
print("infantil:",c1)
if min(r)==a:
	print("regular")
elif min(r)==b:
	print("ortopedico")
elif min(r)==c:
	print("infantil")