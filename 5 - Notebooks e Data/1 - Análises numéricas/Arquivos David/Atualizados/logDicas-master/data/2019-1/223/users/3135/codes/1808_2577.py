a=input("Insira sua frase")
b="AaEeIiOoUu"
for i in range(0,len(b)):
	a=a.replace(b[i],"")
print(a)