from numpy import *
g = array(eval(input("vetor: ")))
i = 0
t = []
while(i<size(g)):
	if(g[i]>=0):
		t.append(g[i])
	i = i + 1
print(str(t).replace(',', ''))