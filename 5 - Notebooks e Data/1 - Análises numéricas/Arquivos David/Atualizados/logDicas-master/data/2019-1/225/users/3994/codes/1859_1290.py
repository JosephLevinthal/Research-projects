from numpy import*
from numpy.linalg import*
b = array(eval(input("Digite as horas:")))
b[0]= b[0]*60
b[1]= b[1]*60
b[2]= b[2]*60
v = array([[10,12,15],[6,8,12],[12,12,18]])
b = b.T
h = dot(inv(v),b)
#f= h[0]
h[0]= round(h[0],0)
h[1]= round(h[1],0)
h[2]= round(h[2],0)
#round(h,0)
#print(h) 
print("cadeira:",h[0])
print("bau:",h[1])
print("mesa:",h[2])

if(h[0]== max(h)):
	print("cadeira")
elif(h[1]== max(h)):
	print("bau")
else:
	print("mesa")


#print(max(h[
