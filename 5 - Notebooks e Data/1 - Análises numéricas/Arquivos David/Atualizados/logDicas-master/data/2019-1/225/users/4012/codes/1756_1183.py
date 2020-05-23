from numpy import*
v = array(eval(input("vetor: ")))
i = 0
j = 0
k = 0
while (k < size(v)):
	if(v[k]>0):
		i = i +1
	k = k + 1
k = 0
t = arange(i)
while(k<size(v)):
	if(v[k]>0):
		t[j]=v[k]
		j = j + 1
	k = k +1
print(t)