from numpy import*

m = int(input("mumero de soma:"))
i = 0 
f = 0 
g = 0
v = zeros(m ,dtype= int) 
while(i != m):
	v[i] = v[i] + i
	g = g + i
	i = i + 1
	f = f + g
	
	
print(f)