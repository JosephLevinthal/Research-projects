from numpy import*
v = array(eval(input()))
i = j = 0
while i<len(v):
	if v[i]>0:
		j+=1
	i+=1
vn = zeros(j, dtype=int)
i = j = 0
while i<len(v):
	if v[i]>0:
		vn[j] = v[i]
		j += 1
	i+=1
print(vn)
