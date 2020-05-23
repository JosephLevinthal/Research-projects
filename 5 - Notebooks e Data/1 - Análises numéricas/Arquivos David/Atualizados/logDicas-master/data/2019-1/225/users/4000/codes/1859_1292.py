from numpy import*
from numpy.linalg import*
x = array(eval(input("M:")))
y = array([[8,3,1], [5,12,10], [1,3,2]])
n = dot(inv(y), x.T)
print("ametista:", round(n[0], 0))
print("esmeralda:", round(n[1], 0))
print("safira:", round(n[2], 0))
if n[0] == max(n):
	print("ametista")
elif n[1] == max(n):
	print("esmeralda")
else:
	print("safira")
