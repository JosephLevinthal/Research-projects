from numpy import*
num = input("num: ")
i = 0 
j = 3
p = "."
tri = ""
while(i < len(num)):
	if(i < (len(num)-4)):
		tri = tri + num[i:j] + p
	else:
		tri = tri + num[i:j]
	i = i + 3
	j = j + 3
print(tri)

	
		
		


