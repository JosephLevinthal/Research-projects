i=int(input("idade: "))
mc=float(input("indice de massa corporal: "))
if i<45 and mc<22 and (i>0 or i<=130) and mc>0 :
	print("Entradas:",i,"anos e ICM",mc)
	print("Risco: Baixo")
elif i<45 and mc>=22 and i>=0 or i<=130 and mc>0 :
	print("Entradas:",i,"anos e ICM",mc)
	print("Risco: Medio")
elif i>=45 and mc<22 and (i>=0 or i<=130) and mc>0 :
	print("Entradas:",i,"anos e ICM",mc)
	print("Risco: Medio")
elif i>=45 and mc>=22 and (i>=0 or i<=130) and mc>0 :
	print("Entradas:",i,"anos e ICM",mc)
	print("Risco: Alto")
else:
	print("Entradas:",i,"anos e ICM",mc)
	print("Dados invalidos")