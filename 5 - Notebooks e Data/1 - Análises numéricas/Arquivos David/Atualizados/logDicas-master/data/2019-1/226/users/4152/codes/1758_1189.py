from numpy import*

n = input("Palindromo: ")
x = n.replace(" ","")
i = -1
o = ""
xf = x.upper()
while(i >= -len(x)):
	o = o + xf[i]
	i = i - 1
print(xf)
if (o == xf):
	print(1)
else:
	print(0)