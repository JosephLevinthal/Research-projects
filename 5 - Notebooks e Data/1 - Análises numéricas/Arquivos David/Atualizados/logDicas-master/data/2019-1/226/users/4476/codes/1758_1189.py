c

s = input("digite: ")
n = s.replace( " ", "")
inv = ""
i = -1
while (i >= -len(n)):
	inv = inv + n[i]
	i = i - 1
print(n.upper())
if(inv == n):
	print(1)
else:
	print(0)
