h= float(input("Insira a altura:"))
g= input("Insira o genero: (M/F)")

if (g.upper() == "M"):
	w=(72.7*h)-58
else:
	w=(62.1*h)- 44.7

print(round(w,2))