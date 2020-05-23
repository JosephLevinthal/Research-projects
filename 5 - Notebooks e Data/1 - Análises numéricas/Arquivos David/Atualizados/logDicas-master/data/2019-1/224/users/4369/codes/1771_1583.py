from numpy import*
v = str(input("Digite sei la: "))
c = ""
i = 0 
while i < len(v):
	if (i + 1) % 3 == 0 and i < len(v) - 1:
		c = c + str(v[i]) + "."
	else:
		c = c + str(v[i])
	print(c)
