from numpy import * 
v = array(eval(input("Vetores: ")))

i = 0
j = 0

while(i < size(v)):
	if(v[i] >= 0):
		j = j + 1
	i = i + 1
	
k = 0 
l = 0

v2 = zeros(j, dtype = int)
while(k < size(v)):
	if(v[k] >= 0):
		v2[l] = v[k]
		l = l + 1
	k = k + 1
print(v2)