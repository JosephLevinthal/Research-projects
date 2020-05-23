from numpy import*

n = array(eval(input()))
i = j = 0
while i<len(n):
	if n[i]>99:
		print(i)
		j+=1
	i+=1
print(j)