from numpy import *
v = array(eval(input("Digite: ")))
v2 = array(eval(input("Digite: ")))
h = int(input("Diigte: "))
x = zeros(3,dtype=int)
for i in range(size(v)):
	if(v[i] >= 5) and (v2[i]*100)/h>=75:
		x[0]+=1
	elif(v[i]>=5 and (v2[i]*100)/h  < 75):
		x[2]+=1
	elif(v[i] < 5) and (v2[i]*100)/h>=75:
		x[1]+=1
print(x)