from numpy import*
from numpy.linalg import*

var = array(eval(input()))
carros = [[8,10,16],[2,3,5],[1,2,3]]
sub = dot(inv(carros),var.T)
print("centurion:",round(sub[0],1))
print("tribune:",round(sub[1],1))
print("senator:",round(sub[2],2))
if sub[0] == min(sub):
	print("centurion")
elif sub[1] == min(sub):
	print("tribune")
elif sub[2] == min(sub):
	print("senator")