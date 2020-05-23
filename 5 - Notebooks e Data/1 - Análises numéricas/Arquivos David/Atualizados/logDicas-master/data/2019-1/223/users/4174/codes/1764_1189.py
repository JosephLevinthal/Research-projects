from numpy import*
a = input("digite uma string:")
b = ""
i = 0
while(i < len(a)):
	if(a[i] != " "):
		b = b + a[i]
	i = i + 1
print(b.upper())

c = ""
i = -1 
while(i >= -len(a)):
	if(a[i] != " "):
		c = c + a[i]
	i = i - 1
n = 0
if(c == b):
	n = n + 1
print(n)