n=int(input("entrada: "))
s=0
t=1
e=1
while(e<=n):
	s=s+(-4/t)*((-1)**e)
	t=t+2
	e=e+1
print(round(s,8))