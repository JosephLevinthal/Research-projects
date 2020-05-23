from numpy import*
from numpy.linalg import*
mat=array([[8,3,1],[5,12,10],[1,3,2]])
v=array(eval(input("digite: ")))
v=v.T
q=dot(inv(mat),v.T)
print("ametista:",round(q[0],0))
print("esmeralda:",round(q[1],0))
print("safira:",round(q[2],0))

if(q[0]==max(q)):
	print("ametista")
elif(q[1]==max(q)):
	print("esmeralda")
else:
	print("safira")

