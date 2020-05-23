from numpy import*

e=array(eval(input()))
s=array(eval(input()))

a=s[0]+e[0]
x = 1
while(x<size(s)):
	a = a - s[x] + e[x]
	x+=1
print(a)
