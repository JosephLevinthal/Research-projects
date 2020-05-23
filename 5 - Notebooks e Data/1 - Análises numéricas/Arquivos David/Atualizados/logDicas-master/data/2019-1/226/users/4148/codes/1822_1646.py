from numpy import*


n = array(eval(input('')))
j = 0
for i in n:
	if(i<=50):
		j = j + 1
print(j)


t = zeros(j, dtype=int)
x = 0
g = 0
for u in range(size(n)):
	if(u<=50):
		t[x]=n[g]
		x+=1
	g+=1
print(t)		