a = input("digite uma sequencia de caracteres: ").upper()
print(a.replace(' ', ''))
if (a[0:] == a[::-1]):
	print("1")
else:
	print("0")

