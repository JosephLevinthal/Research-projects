txt = input("FRASE: ")

txt1 = txt.upper()
txt1 = txt1.replace(" ", "")
print(txt1)

txt2 = ""
i = 0
while (i < len(txt1)):
	txt2 = txt2 + txt1[-1 - i]
	i += 1
if (txt2 == txt1):
	print("1")
else:
	print("0")