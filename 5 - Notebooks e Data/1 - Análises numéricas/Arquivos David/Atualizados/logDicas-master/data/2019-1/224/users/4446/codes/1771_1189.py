s=input("digite a frase: ").upper()

print(s.replace(' ', ''))

if( s[0:]==s[::-1]):
	print("1")
else:
	print("0")