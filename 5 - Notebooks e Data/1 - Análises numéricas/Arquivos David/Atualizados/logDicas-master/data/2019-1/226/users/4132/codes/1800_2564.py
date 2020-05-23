from numpy import *
v = array(eval(input("Digite: ")))
v2 = array(eval(input("Digite: ")))

x = zeros(3,dtype=int)

for i in range(size(v)):
	if v[i]>v2[i]:
		x[0]+=1
	elif(v[i]==v2[i]):
		x[1]+=1
	elif v[i]<v2[i]:
	   x[2]+=1
print(x)


