from math import*

na = int(input())
nb = int(input())
pa = float(input())
pb = float(input())

t = 0

while(na < nb):
	na = na + ((na * pa) / 100)
	nb = nb + ((nb * pb) / 100)
	t = t + 1
	
print(t)