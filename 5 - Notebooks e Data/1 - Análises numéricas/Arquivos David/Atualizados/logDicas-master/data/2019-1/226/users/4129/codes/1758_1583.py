from numpy import*
n = input("numeros: ")

i =0
c = 3
f = ""
while(i < len(n)):
	a = n[i:c]
	f = f+a+"."
	i = i + 3
	c = c + 3
print(f[:-1])
	