from numpy import*

n = array(eval(input()))
nm = array(eval(input()))
i = 0
j = k = l = m = o = p = 0
while i<size(n):
	if n[i]<0:
		j += 1
	if n[i]>=6:
		k += 1 
	if n[i]<6 and n[i]>=0:
		l += 1
	if n[i]==max(n):
		m = nm[i]
	if n[i]>=0:
		o += n[i]
		p += 1
	i+=1
print(j)
print(k)
print(l)
print(round(o/p,2))
print(m)