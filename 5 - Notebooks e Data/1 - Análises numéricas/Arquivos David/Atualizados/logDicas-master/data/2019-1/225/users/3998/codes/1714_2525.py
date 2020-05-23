x = int(input())
l= 1
s = 0 #var acumuladora
while(l <= x):
	if(x%l==0):
		s = s + 1
		print(l)
	l=l+1
if(s>1):
	msg="divisores"
else:
	msg="divisor"
print(s,msg)