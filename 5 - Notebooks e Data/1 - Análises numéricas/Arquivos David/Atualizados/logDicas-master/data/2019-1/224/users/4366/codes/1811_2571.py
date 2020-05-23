s = input("digite uma palavra com a letra a: ")
a = ""
for ch in s:
	if ch != "a" and ch != "A":
		a = a + ch
print(a)