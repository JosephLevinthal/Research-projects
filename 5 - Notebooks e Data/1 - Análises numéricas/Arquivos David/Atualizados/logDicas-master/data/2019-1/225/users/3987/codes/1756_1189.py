s = input("Digite uma string: ").upper()
s=s.replace(' ','')
inv = ""
i = -1
b = 1
c = 0
while i >= -len(s):
	inv = inv + s[i]
	if(s[c]) != (s[i]):
		b = 0
	c = c + 1
	i = i - 1
print(s)
print(b)