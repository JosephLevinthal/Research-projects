from numpy import*
n = input("caracteres numericos: ")
i = 0 
j = 3
p = "."
tri = ""
while(i < len(n)):
	if(i < (len(n)-4)):
		tri = tri + n[i:j] + p
	else:
		tri = tri + n[i:j]
	i = i + 3
	j = j + 3
print(tri)