str = input("Frase: ")

s = ""

for i in str:
	if (i.upper() != "A"):
		s = s+i
	
print(s)