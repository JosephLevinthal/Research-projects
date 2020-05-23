from numpy import*
from numpy.linalg import*

k = array(eval(input()))
k = k * 60
g = array([[10,12,15],[6,8,12],[12,12,18]])

s = dot(inv(g),k.T)
print("cadeira:" ,round(s[0],0))
print("bau:" ,round(s[1],0))
print("mesa:",round(s[2],0))

if s[0]== max(s):
	print("cadeira")
elif s[1]== max(s):
	print("bau")
else:
	print("mesa")
	