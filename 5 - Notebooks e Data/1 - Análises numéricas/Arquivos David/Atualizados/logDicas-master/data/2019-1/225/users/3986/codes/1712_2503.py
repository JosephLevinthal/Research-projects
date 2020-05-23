n=int(input("termo: "))
t=0
c=4
pi=0
nl=1
si=1
while (t < n) :
	t=t + 1
	pi=pi+ (c/nl) * si
	si= si * (-1)
	nl=nl + 2
	
print(round(pi,8))