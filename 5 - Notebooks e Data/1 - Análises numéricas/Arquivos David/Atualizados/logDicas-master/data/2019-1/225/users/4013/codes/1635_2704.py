n = float(input("nota do aluno:"))
m = input("S / N :")
if ( m == "S" ):
	nota_final = n + (n * (10/100)) 
else:
	nota_final = n 
print(nota_final)