n=float(input("termo inserido :"))
t=1
k=2
pi=3
si=1
while (t < n):
	t= t + 1
	pi=pi+(4/(k*(k+1)*(k+2))) * si
	k=k+2
	si= si * (-1)
print(round(pi,8))