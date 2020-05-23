nota = float(input())
b = input("recebe bonificacao se sim digita S caso contrario digite N")

if( b == 'S' ):
	print(nota + nota*0.1)
else:
	print(nota)
