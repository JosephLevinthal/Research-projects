from numpy import*

m = array(eval(input("")))
acu = 0.0
for i in range(len(m)):
	for j in range(len(m)):
		if(i!=j):
			acu+= m[i][j]
print(round(acu, 2))