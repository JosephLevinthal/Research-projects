# Ao testar sua solução, não se limite ao caso de exemplo.
x=float(input("numero de hrs trabalhadas extras: "))
y=float(input("numero de hrs nao trabalhadas: "))
H=x-1/4*y
A=500
B=100
if(x>0):
	if(H>400):
		print(x,"extras","e",y,"de","falta")
		print("R$",float(A))
	elif(H<=400):
		print(x,"extras","e",y,"de","falta")
		print("R$",float(B))