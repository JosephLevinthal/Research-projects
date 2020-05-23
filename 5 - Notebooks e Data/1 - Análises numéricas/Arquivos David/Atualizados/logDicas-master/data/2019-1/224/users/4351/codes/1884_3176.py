from numpy import*
nome=input("digite a string aqui: ").upper()
vogais=0
consoantes=0
for ch in nome:
	if (ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U"):
		vogais= vogais + 1
	else:
		consoantes=consoantes + 1
print(vogais)
print(consoantes)