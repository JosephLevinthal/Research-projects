temp = input("C/F: ")
valor = float(input("Temperatura: "))

if (temp.upper() == "F"):
	t = (5*(valor - 32))/9
else:
	t = ((9*valor/5) + 32)
	
print(t)