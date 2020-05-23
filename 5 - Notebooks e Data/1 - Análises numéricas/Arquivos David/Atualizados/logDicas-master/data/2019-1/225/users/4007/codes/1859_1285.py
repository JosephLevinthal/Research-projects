from numpy import*
from numpy.linalg import*
v = array(eval(input("embalagens:")))
t = array([[4 ,5 ,2],[3 ,2 ,2],[2 ,3 ,3]])
a = v.T
s = inv(t)
x = dot(s, a)
print("grande:",round(x[0], 0))
print("medio:",round(x[1], 0))
print("pequeno:",round(x[2], 0))

if (x[0] == max(x)):
	print("grande")
elif(x[1] == max(x)):
	print("medio")
elif(x[2] == max (x)):
	print("pequeno")
