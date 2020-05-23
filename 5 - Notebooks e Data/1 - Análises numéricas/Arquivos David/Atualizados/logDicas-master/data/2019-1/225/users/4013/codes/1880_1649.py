from numpy import*
s = input("string:") .split(",")
p=0
c=0
m=0
v=0
a=0
for i in range(size(s)):
	if(s[i] == "P"):
		p = p + 1
	elif(s[i] == "C"):
		c = c+1
	elif(s[i] == "M"):
		m =m +1
	elif(s[i] == "V"):
		v=v+1
	else:
		a = a+1
q = zeros(5, dtype=int)
q[0]=p
q[1]=c
q[2]=m
q[3]=v
q[4]=a
print(max(q))
print(q)