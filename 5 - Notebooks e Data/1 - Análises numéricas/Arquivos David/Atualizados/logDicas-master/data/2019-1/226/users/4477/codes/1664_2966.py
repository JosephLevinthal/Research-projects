mulher = input("E mujlher ou nao e?! ")
valor_ingresso = float(input("Determine o valor do ingresso: "))
quantidade_ingresso = float(input("Determine o valor do ingresso: "))

desconto = 0.2 * valor_ingresso

if mulher.upper() == "S":
	ingresso = (valor_ingresso - desconto) * quantidade_ingresso
else:
	ingresso = (valor_ingresso) * quantidade_ingresso 
	
print(round(ingresso, 2))