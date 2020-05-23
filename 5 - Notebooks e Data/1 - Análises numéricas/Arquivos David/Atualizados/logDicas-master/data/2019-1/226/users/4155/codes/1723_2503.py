n = int(input("n: "))
soma = 4
i = 1
v = 1
s = -1
while(n > i):
	soma = soma + (4*s/(v + 2))
	i = i + 1
	v = v + 2
	s = s*(-1)
print(round(soma, 8))