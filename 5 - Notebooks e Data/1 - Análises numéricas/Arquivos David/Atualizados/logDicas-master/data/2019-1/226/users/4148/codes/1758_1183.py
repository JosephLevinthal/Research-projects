from numpy import*
v = array(eval(input("vetor: ")))


i=0
n=0

while (i < size(v)):
	if v[i]<0:
		n = n + 1
	i = i + 1
	
t = size(v) - n 
tf= zeros(t, dtype=int)

i = 0
j = 0

while j < size(v):
	if v[i] > 0:
		vf[j]=v[i]
		j = j + 1
	i = i + 1

print(vf)