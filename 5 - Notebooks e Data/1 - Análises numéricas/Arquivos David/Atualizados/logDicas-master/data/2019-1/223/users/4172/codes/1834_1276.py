from numpy import*
from numpy.linalg import*



x=array(eval(input("")))

a=zeros(x.shape[1], dtype=int)

for j in range(x.shape[1]):
	a[j]=sum(x[:,j])
for j in range(x.shape[1]):
	if a[j]==max(a):
		if j+1==1:
			print("1")
		if j+1==2:
			print("2")
		if j+1==3:
			print("3")
		if j+1==4:
			print("4")
		if j+1==5:
			print("5")
		if j+1==6:
			print("6")
		if j+1==7:
			print("7")
		