from numpy import*
from numpy.linalg import*

mat = array([[8,10,16],[2,3,5],[1,2,3]])

vet= array(eval(input("digite: ")))

r = dot(inv(mat),vet.T)

print("centurion:",round(r[0],0))
print("tribune:",round(r[1],0))
print("senator:",round(r[2],0))

if r[0]==min(r):
	print("centurion")
elif r[1]==min(r):
	print("tribune")
else:
	print("senator")
