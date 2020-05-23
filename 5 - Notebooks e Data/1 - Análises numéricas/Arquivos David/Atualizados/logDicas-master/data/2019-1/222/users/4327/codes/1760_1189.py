v = input("Digite: ")

w = v.replace(" ","").upper()
s = ""

i = 0
p = 0
while i <= len(w):
	if i > 0:
		s = s + w[-i]
	i = i + 1
print(w)
if s == w:
	print(1)
else:
	print(0)