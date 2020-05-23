n = int(input("Numero:"))
i = n
v = ""
while i > 0:
	v = "*" * i
	i = i - 1
	print(v)
while i != n + 1:
	v = "*" * i
	i = i + 1
	print(v)