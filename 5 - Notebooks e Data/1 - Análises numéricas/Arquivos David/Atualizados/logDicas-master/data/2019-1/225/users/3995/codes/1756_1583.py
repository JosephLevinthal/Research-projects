
v=str(input("numero multiplo de 3:"))

c =0
i = 1
s = ""

while(c < len(v)):
	if (i == 4):
		i = 1
		s = s + "."
	s = s + v[c]
	i=i+1
	c = c +1
print(s)