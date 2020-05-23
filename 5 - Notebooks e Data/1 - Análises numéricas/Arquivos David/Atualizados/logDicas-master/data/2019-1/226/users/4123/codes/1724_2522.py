n = i = int(input())
t = 1.5
while(i>0):
	if n == i-1:
		t = 1+t
	else:
		t = 1 + i/(2*i+1)*(t)
	i -= 1
pi = 2*t
print(round(pi,10))