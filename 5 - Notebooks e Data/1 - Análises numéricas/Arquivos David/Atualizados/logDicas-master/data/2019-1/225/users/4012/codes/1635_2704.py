nota = float(input("digite a nota: "))
boni = input("bonificacao? (S/N):")
a = 10 / 100 

if (boni == "S"):
	final = nota + (nota * a) 
else:
	final = nota
	
print(float(final))
 