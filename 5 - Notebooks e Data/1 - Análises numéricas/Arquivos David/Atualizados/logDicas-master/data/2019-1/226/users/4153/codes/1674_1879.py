# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("insira as horas extras: "))
y = float(input("insira as horas nao trabalhadas: "))

print(x,"extras e",y,"de falta")

H = x - (0.25 * y)
a = 100.00
b = 500.00
if(H <= 400):
	print("R$",a)
else:
	print("R$",b)