from numpy import*
from numpy.linalg import*

v = array(eval(input("vetor: ")))
m = array([
	[4,5,2],
	[3,2,2],
	[2,3,3]
])
m = m
d = dot(inv(m),v.T)
print("grande:",round(d[0],0))
print("medio:",round(d[1],0))
print("pequeno:",round(d[2],0))
m = max(d)
if d[0] == m:
	print("grande")
if(d[1]==m):
	print("medio")
if(d[2]==m):
	print("pequeno")