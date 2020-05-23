from numpy import*
from numpy.linalg import*

x=array([[8,3,1],
			[5,12,10],
			[1,3,2]])
mt=array(eval(input("")))

a=dot(inv(x), mt)

print("ametista:", round(a[0],0))
print("esmeralda:", round(a[1],0))
print("safira:", round(a[2],0))

if  a[0]>a[1] and a[0]>a[2]:
		print("ametista")
elif a[1]>a[0] and a[1]>a[2]:
		print("esmeralda")
else:
	print("safira")