from numpy import*
v1=input()
i=0
while(i<len(v1)-3):
	i=i+3
	v1=v1[:i]+"."+v1[i:len(v1)]
	i=i+1
print(v1)
