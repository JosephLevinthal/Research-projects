# Ao testar sua solução, não se limite ao caso de exemplo.
x=float(input("horas extras:"))
y=float(input("numero de horas nao trabalhadas:"))
H=(x)-1/4*(y)
print(x,"extras","e",y,"de falta")
if(H>400):
	print("R$ ",round(500.00,2))
if(H<=400):
	print("R$",round(100.00,2))
	
	