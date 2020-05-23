from numpy import*
v1= array(eval(input("vetor")))
i=0
t=0
n= size(v1)
while (i<n):
	if(v1[i]>99):
		print(i)
		t=t+1
		i=i+1
	else:
		i=i+1

print(t)