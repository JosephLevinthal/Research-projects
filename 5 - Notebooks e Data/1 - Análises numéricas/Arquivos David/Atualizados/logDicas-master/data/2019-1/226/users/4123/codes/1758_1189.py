from numpy import*
x = input()
x = x.replace(" ","")
i = 0
r = 1
while i<len(x):
	if x[i]!=x[-i-1]:
		r=0
		break
	i+=1
print(x.upper())
print(r)
	