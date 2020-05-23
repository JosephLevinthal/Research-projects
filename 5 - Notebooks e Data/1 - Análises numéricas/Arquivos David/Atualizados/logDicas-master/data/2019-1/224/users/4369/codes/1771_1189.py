c = str(input("Digite uma string: ")) .upper()
print(c.replace(' ', '')) 
if c[0:] == c[::-1]:
	print(1)
else:
	print(0)