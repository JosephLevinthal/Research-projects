total_ast = int(input("metade dos asteriscos na primeira linha: ")) * 2
ast = "*"

# Primeira linha de asteriscos
ast_linha_1 = ast * total_ast
print(ast_linha_1)

# Quantidade de asteriscos (de cada lado) nas proximas  linha  
QA2 = (len(ast_linha_1)- 2)//2

oo = "oo"
mult = 1 #multiplica os "oo"
ll = (ast * QA2 ) + (oo * mult ) + (ast * QA2 )

for ch in range(0,len(ast_linha_1)):
	if (QA2 <= len(ll)-1 and (mult <= (len(ast_lin