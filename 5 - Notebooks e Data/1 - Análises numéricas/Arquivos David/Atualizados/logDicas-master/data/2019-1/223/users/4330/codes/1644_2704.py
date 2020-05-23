nota=float(input("nota parcial: "))
bonus=input("alunorecebera bonus de ? (S/N)")

if ( bonus.upper () == "N" ):
	nota = nota

else:
	nota = nota + ( nota * 0.1 )
		
print(nota)