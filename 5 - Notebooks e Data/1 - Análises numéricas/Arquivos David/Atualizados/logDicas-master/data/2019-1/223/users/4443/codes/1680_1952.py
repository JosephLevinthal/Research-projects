#Leitura do salario bruto:
s = float(input("Digite o valor do salario bruto: "))

# desconto previdenciario
if(s <= 1659.38):
	ns = s*0.92
elif(1659.39 <= s <= 2765.66):
	ns = s*0.91
elif(2765.67 <= s <= 5531.31):
	ns = s*0.89
elif(s > 5531.31):
	ns = s-608.44

sb_ir = ns
if(sb_ir <=1903.98):
	sl = sb_ir
elif(1903.99 <= sb_ir <= 2826.65):
	sl = sb_ir*0.925
elif(2826.66 <= sb_ir <= 3751.05):
	sl = sb_ir*0.85	
elif(3751.1 < sb_ir <= 4664.68):
	sl = sb_ir*0.775	
elif(sb_ir > 4664.68):
	sl = sb_ir*0.725
	
print("Salario liquido = R$", round(sl, 2))

