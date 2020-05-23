c=input("tipo de dano:")
N=int(input("valor do dano:"))
nt=int(input("Numeros de turnos:"))

if(N>=1 and N<=4 or c.upper()=="CAUDA" and c.upper()=="CUSPE" and c.upper()=="PATADA"):
	if(c.upper()=="CAUDA"):
		s=N*nt
	elif(c.upper()=="CUSPE"):
		s=2*N*nt
	else:
		s=2*N-5*nt
else:
	s="Entrada invalida"
print(s)