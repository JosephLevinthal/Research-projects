# Ao testar sua solução, não se limite ao caso de exemplo.
E = float(input("numero de h extras: "))
F = float(input("numero de h faltou: "))
print(E ,"extras e", F ,"de falta")

H = E - 1/4*(F)
if(H != 0):
	if(H > 400): 
		G = 500.0
		print("R$", round(G, 2))
	elif(H <= 400):
		G = 100.0
		print("R$", round(G, 2))
	else: 
		("nao faltoso")
else: 
	print("nao faltoso")