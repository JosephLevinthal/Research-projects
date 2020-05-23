ext = float(input("digite o numero de horas extras:"))
fal = float (input("digite o numero de horas que o funcionario faltou:"))

H = (ext) - (1/4) * (fal)

if( H > 400 ):
    grat = 500.00
   
elif( H <= 400):
    grat = 100.00
   
print(ext,"extras e",fal,"de falta")
print("R$",round(grat,2))


