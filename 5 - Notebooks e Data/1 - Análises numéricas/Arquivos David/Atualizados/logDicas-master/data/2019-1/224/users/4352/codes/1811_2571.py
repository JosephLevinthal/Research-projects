s = str(input("digite algo que contenha a letra a: "))
ss = ""
for ch in s:
	if(ch != "a" and ch != "A"):
		ss = ss + ch
print(ss)