from numpy import*
v = array(eval(input("vetor: ")))
i = 0
t = []
while (i < size(v)):
	if(v[i] >= 0):
		t.append(v[i])
	i = i + 1
print(str(t).replace(',',''))

	

