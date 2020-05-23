# Ao testar sua solução, não se limite ao caso de exemplo.
e = float(input("O numero de horas extras: "))
f = float(input("O numero de horas que o funcionario faltou: "))

h = e - (1/4 *f)

print (e, "extras", "e", f , "de falta"  )

if (h>0):
	if(h>400):
		g = 500.0
		print("R$", g)
	else:
		g = 100.0
		print ("R$", g)