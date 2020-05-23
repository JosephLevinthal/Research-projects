from numpy import*
b = array(eval(input("a:")))
for j in range(4):
	v=zeros(4)
	k=0
	for i in range(4):
		v[k]= b[i,j]
		k = k+1
	v= sorted(v, reverse = True)
	k=0
	for i in range(4):
		b[i,j]= v[k]
		k = k+1
print(b)

	