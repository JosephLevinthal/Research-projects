
a = input("tipo do ataque:")
a = a.upper()
n = int(input("valor do dado"))
c = int(input("numero de turnos"))
if (a=="PATADA"):
   f= ((2*n)-5)*c
elif (a=="CUSPE"):
   f= (2*n)*c
elif (a=="CAUDA"):
   f=n*c
elif (n<1):
	f="Entrada invalida"
elif (n>4):
	f="Entrada invalida"

print(f)
